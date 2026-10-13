#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lint_tokens.py —— 设计令牌合规校验

把 SKILL.md 里的人工自检清单变成可执行的检查，产出后跑一遍即可。

用法
    python3 scripts/lint_tokens.py <文件...> [--style 风格] [--min-contrast 4.5]

参数
    --style         miuix | apple | material | fluent。省略时自动识别文件中出现的风格。
    --min-contrast  正文对比度阈值，默认 4.5（WCAG AA）。大号文字用 3.0。

检查三项
    1. 硬编码色值  —— 令牌定义之外的裸 hex / rgb() / hsl()，应改为 var(--token)
    2. 对比度      —— 同一规则块内前景色与背景色的 WCAG 对比度
    3. 核心令牌    —— 该风格必须具备的语义令牌是否出现在文件中

退出码：0 = 通过；1 = 有 error 级问题；2 = 用法错误。
"""

import argparse
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOKEN_DIR = os.path.join(HERE, "..", "assets", "tokens")

# 每种风格必须具备的核心语义令牌
REQUIRED = {
    "miuix": ["--mi-primary", "--mi-on-primary", "--mi-surface", "--mi-on-surface",
              "--mi-background", "--mi-outline"],
    "apple": ["--ap-tint", "--ap-label", "--ap-bg", "--ap-separator", "--ap-fill"],
    "material": ["--md-primary", "--md-on-primary", "--md-surface", "--md-on-surface",
                 "--md-outline", "--md-error"],
    "fluent": ["--fl-brand", "--fl-neutral-bg1", "--fl-neutral-fg1", "--fl-neutral-stroke1"],
}

# 各风格的 CSS 变量前缀（用于自动识别）
PREFIX = {"miuix": "mi", "apple": "ap", "material": "md", "fluent": "fl"}

TOKEN_DEF = re.compile(r"--[\w-]+\s*:")
COLOR_LIT = re.compile(r"(#[0-9a-fA-F]{3,8}\b|rgba?\(\s*[^)]*\)|hsla?\(\s*[^)]*\))")
BLOCK = re.compile(r"([^{}]+)\{([^{}]*)\}", re.S)
DECL = re.compile(r"(?:^|[;\s])(color|background|background-color)\s*:\s*([^;]+);", re.I)


def load_known_colors(style):
    """读取该风格令牌文件里的所有色值，作为‘合法色值’白名单。"""
    path = os.path.join(TOKEN_DIR, {"miuix": "miuix.css", "apple": "apple-hig.css",
                                    "material": "material-3.css", "fluent": "fluent-2.css"}[style])
    known = set()
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for m in COLOR_LIT.finditer(f.read()):
                known.add(norm_hex(m.group(1)))
    return known


def norm_hex(c):
    """把 #abc / #aabbcc / rgb() 归一化为 '#rrggbb'（含 alpha 的原样小写返回）。"""
    c = c.strip().lower()
    if c.startswith("#"):
        h = c[1:]
        if len(h) == 3:
            return "#" + "".join(ch * 2 for ch in h)
        if len(h) == 4:
            return "#" + "".join(ch * 2 for ch in h)
        return "#" + h[:6]
    m = re.match(r"rgba?\(\s*([\d.]+)[\s,]+([\d.]+)[\s,]+([\d.]+)", c)
    if m:
        return "#%02x%02x%02x" % (int(float(m.group(1))), int(float(m.group(2))), int(float(m.group(3))))
    return c


def to_rgb(c):
    c = norm_hex(c)
    if re.fullmatch(r"#[0-9a-f]{6}", c):
        return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))
    return None


def luminance(rgb):
    def ch(v):
        v /= 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = map(ch, rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(c1, c2):
    a, b = to_rgb(c1), to_rgb(c2)
    if not a or not b:
        return None
    l1, l2 = luminance(a), luminance(b)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def detect_styles(text):
    found = [s for s, p in PREFIX.items() if re.search(r"--%s-[\w-]+\s*:" % p, text)]
    return found or list(PREFIX)


def lint_file(path, style, min_contrast):
    with open(path, encoding="utf-8") as f:
        text = f.read()

    styles = [style] if style else detect_styles(text)
    problems = []          # (级别, 行号, 说明)
    lines = text.split("\n")

    # ---- 检查 1：硬编码色值 ----
    known = set().union(*[load_known_colors(s) for s in styles]) if styles else set()
    for i, line in enumerate(lines, 1):
        if TOKEN_DEF.search(line):          # 令牌定义行跳过
            continue
        for m in COLOR_LIT.finditer(line):
            if norm_hex(m.group(1)) not in known:
                problems.append(("error", i,
                                 "硬编码色值 `%s`，应改为 var(--%s-…)" %
                                 (m.group(1), PREFIX[styles[0]] if styles else "token")))

    # ---- 检查 2：对比度 ----
    for sel, body in BLOCK.findall(text):
        decls = {k.lower(): v.strip() for k, v in DECL.findall(body)}
        fg, bg = decls.get("color"), decls.get("background-color") or decls.get("background")
        if not fg or not bg:
            continue
        if "var(" in fg or "var(" in bg:
            continue                        # 变量无法静态求值
        ratio = contrast(fg, bg)
        if ratio is None:
            continue
        line_no = text[:text.find(body)].count("\n") + 1
        if ratio < min_contrast:
            level = "error" if ratio < 3.0 else "warn"
            problems.append((level, line_no,
                             "对比度 %.2f:1（%s on %s）低于 %.1f" %
                             (ratio, fg, bg, min_contrast)))

    # ---- 检查 3：核心令牌 ----
    for s in styles:
        missing = [t for t in REQUIRED[s] if t not in text]
        if missing:
            problems.append(("warn", 0,
                             "[%s] 缺少核心令牌：%s" % (s, "、".join(missing))))

    return styles, problems


def main():
    ap = argparse.ArgumentParser(description="设计令牌合规校验")
    ap.add_argument("files", nargs="+", help="要检查的 .html / .css 文件（支持 glob）")
    ap.add_argument("--style", choices=list(PREFIX), help="指定风格，省略则自动识别")
    ap.add_argument("--min-contrast", type=float, default=4.5, help="正文对比度阈值，默认 4.5")
    args = ap.parse_args()

    files = []
    for pat in args.files:
        files.extend(sorted(glob.glob(pat, recursive=True)) or [pat])
    files = [f for f in files if os.path.isfile(f)]
    if not files:
        print("没有找到可检查的文件。", file=sys.stderr)
        return 2

    total_err = total_warn = 0
    for f in files:
        styles, problems = lint_file(f, args.style, args.min_contrast)
        errs = [p for p in problems if p[0] == "error"]
        warns = [p for p in problems if p[0] == "warn"]
        total_err += len(errs)
        total_warn += len(warns)

        tag = "/".join(styles)
        flag = "FAIL" if errs else ("WARN" if warns else " OK ")
        print("\n[%s] %s  (%s)" % (flag, f, tag))
        for level, line, msg in problems:
            loc = "L%d" % line if line else "--"
            mark = "✗" if level == "error" else "!"
            print("   %s %-6s %s" % (mark, loc, msg))
        if not problems:
            print("   通过：无硬编码色值、对比度达标、核心令牌齐全")

    print("\n合计：%d error / %d warn" % (total_err, total_warn))
    if total_err:
        print("提示：组件样式里只应出现 var(--token)，不要写字面量颜色。")
    return 1 if total_err else 0


if __name__ == "__main__":
    sys.exit(main())
