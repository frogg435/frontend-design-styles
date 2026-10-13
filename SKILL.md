---
name: frontend-design-styles
description: 前端界面设计风格的实现与还原助手，覆盖 Xiaomi MIUIX/HyperOS、Apple HIG、Google Material Design 3、Microsoft Fluent 2 四套设计语言。当用户要求"用某个设计风格做页面/组件"、"做一套 iOS 风格的界面"、"Material Design 3 风格的后台"、"Windows 11 风格桌面应用"、"HyperOS/MIUI 风格 App"，或在四种风格之间选型、对比、生成设计令牌（颜色/字阶/圆角/阴影/动效/间距）并输出可运行的前端代码（HTML/CSS/JS、React、Vue、Tailwind、Compose/Kotlin 映射）时使用。也用于审查现有界面是否符合某一设计语言。
---

# Frontend Design Styles

把四种主流设计语言**忠实地**落到前端代码里。核心不是"看起来差不多"，而是用**语义令牌 + 组件形态 + 动效曲线**三层一致地还原，让成品能被该平台用户认出"这就是 iOS / 这就是 Material / 这就是 Windows"。

## 何时用 / 不用

**用**：用指定设计风格生成或改造界面；四种风格选型对比；产出设计令牌与主题文件；按设计语言做视觉审查。

**不用**：用户没有风格倾向、只想快速要个"好看的页面" → 先问一句要不要指定风格，或走 `references/style-router.md` 的推荐逻辑；纯后端/算法任务与本技能无关。

## 四种风格指纹速查

这是最高辨识度的几个特征。做任何实现前先确认这张表，细节再查对应 reference。

| | **MIUIX / HyperOS** | **Apple HIG** | **Material Design 3** | **Fluent 2** |
|---|---|---|---|---|
| 主色 | `#3482FF`（亮）/ `#277AF7`（暗） | `#007AFF` / `#0A84FF` | 角色化，基线 `#6750A4` | `#0F6CBD` |
| 字体 | MiSans | SF Pro（<20pt Text，≥20pt Display） | Roboto / Roboto Flex | Segoe UI Variable |
| 正文基准 | 16–17px | 17pt | 16sp（body-large） | 14px（body-1） |
| 圆角语言 | **16dp 统一圆角 + squircle**（与 iOS 同源，按钮非胶囊） | 连续曲率圆角（squircle），容器 10–20pt | 12dp 卡片 / 28dp FAB & 弹窗 / 全圆按钮 | 小圆角，控件 4px、弹窗 8px，嵌套 −2px |
| 层次手法 | 色阶分层（`#FFFFFF` / `#F7F7F7` / `#E8E8E8`），几乎不用重阴影 | 材质模糊（translucency）+ 分组列表 + 内容压过 UI | 色调叠加（tonal overlay）优先，阴影次之 | 材质（Mica / Acrylic）+ 低调多层阴影 |
| 动效 | 轻快、带弹性回弹，200–300ms | 弹簧物理，200–300ms，无 linear | 强调曲线 `cubic-bezier(0.2,0,0,1)`，按时长令牌分级 | 快而克制，150–250ms，`easyEase` |
| 触控/点击目标 | ≥ 48dp | ≥ 44×44pt | ≥ 48dp | 控件高 32px（紧凑/舒适模式） |
| 一句话气质 | 圆润、通透、蓝色科技感 | 克制、留白、内容优先 | 色彩表达力强、层次靠色调 | 生产力、清晰、桌面原生 |

## 工作流

**Step 1 · 定风格。** 用户已指定 → 直接用。未指定 → 读 `references/style-router.md`，按产品形态/平台/密度给出 1 个推荐 + 1 个备选，让用户确认。

**Step 2 · 读令牌。** 打开对应参考文档，把颜色、字阶、间距、圆角、阴影、动效**全部读一遍**再动手，不要凭印象写：

- MIUIX / HyperOS → `references/miuix-hyperos.md`
- Apple HIG → `references/apple-hig.md`
- Material Design 3 → `references/material-design-3.md`
- Fluent 2 → `references/fluent-2.md`

**Step 3 · 落令牌。** 直接复制 `assets/tokens/<style>.css` 作为语义令牌层（已含明/暗双主题），**不要**把 hex 写进组件样式里。深色模式通过 `[data-theme="dark"]` 或 `prefers-color-scheme` 切换。

**Step 4 · 搭组件。** 按 `references/components-playbook.md` 里该风格的组件规格实现（按钮变体、输入框、卡片、导航、弹层、开关、列表）。每个交互态（hover / focus / pressed / selected / disabled）都要有，不能只做默认态。

**Step 5 · 加动效 + 自检。** 按 `references/motion-and-accessibility.md` 补齐过渡，然后跑 `python3 scripts/lint_tokens.py <产物> --style <风格>`，再逐条过自检清单（见下）。

## 铁律

1. **不混风格。** 选了 Fluent 就别出现 iOS 的 `#007AFF`、Material 的 pill FAB 或 HyperOS 的大圆角卡片。混合是最常见的失败模式。
2. **令牌先行。** 组件 CSS 里只允许出现 `var(--xxx)`，不允许出现字面量颜色/字号/圆角值。
3. **明暗双主题一起做。** 四套体系都有官方暗色值，直接查表，不要用 `filter: invert` 或手动调暗糊弄。
4. **平台约定不可改。** 例如 iOS 的最小点击区 44pt、Material 的 state layer 不透明度、Fluent 的控件 1px 底边描边、HyperOS 的深色背景 `#242424`（不是纯黑 surface）。
5. **无障碍是硬指标。** 正文对比度 ≥ 4.5:1，UI 元素 ≥ 3:1，焦点环必须可见，尊重 `prefers-reduced-motion`。
6. **中文排版要单独处理。** Roboto / Segoe UI / SF Pro 都没有完整中文字形，中文界面必须回退到苹方 / 思源黑体 / MiSans 等中文字体，并下调 letter-spacing（拉丁字距不适用于中文）。

## 交付规范

- 默认产出**单文件可运行的 HTML**（内联 `<style>` + `<script>`），令牌以 `:root` CSS 变量组织，方便用户直接预览和复制。
- 用户指定框架时再切换，映射规则见 `references/framework-mappings.md`：Tailwind 用 `assets/mappings/tailwind.css`；React/Vue 用令牌对象 + CSS 变量；Compose 优先用官方库（MIUIX 用 `MiuixTheme`，M3 用 `MaterialTheme`）。
- 组件演示页可参考 `assets/templates/showcase.html`（同一套组件在四种风格下的并列呈现，可切换主题与明暗）。
- **产出后必跑校验**：`python3 scripts/lint_tokens.py <产物文件> --style <风格>`，三项检查（硬编码色值 / 对比度 / 核心令牌）不通过就修，再交付。
- 交付时说明：用了哪套体系、有哪些刻意偏离、暗色模式如何切换、字体回退栈是什么。

## 自检清单

做完逐条核对，不通过就修：

- [ ] 颜色全部来自令牌，无硬编码 hex
- [ ] 字阶层级不超过 4 档，正文基准字号符合该体系
- [ ] 圆角体系自洽（含嵌套圆角 = 外层 − 内边距）
- [ ] 阴影/材质用法符合该体系（Material 用色调叠加，Fluent 用 Mica/Acrylic，iOS 用模糊材质，HyperOS 用色阶）
- [ ] 所有交互态齐备：hover / focus-visible / active / disabled / selected
- [ ] 明暗双主题都验证过
- [ ] 点击目标尺寸达标
- [ ] 对比度达标，焦点环可见
- [ ] `prefers-reduced-motion` 下动效降级
- [ ] 中文字体回退正确、字距已调整
- [ ] 无其他体系串味

## 参考文件

| 文件 | 内容 |
|---|---|
| `references/style-router.md` | 四风格选型决策树、对比矩阵、混搭禁区 |
| `references/miuix-hyperos.md` | MIUIX 令牌全表 + HyperOS 视觉特征 + 组件规格 |
| `references/apple-hig.md` | 系统色全表 + Dynamic Type 12 级 + 材质 + 组件规格 |
| `references/material-design-3.md` | 29 个颜色角色明暗全表 + 15 级字阶 + 形状/海拔/状态层 |
| `references/fluent-2.md` | 中性色/品牌色阶 + Type Ramp + 控件尺寸 + Mica/Acrylic + 阴影令牌 |
| `references/components-playbook.md` | 按钮/输入/卡片/导航/弹层/开关/列表 的逐风格实现规格 |
| `references/motion-and-accessibility.md` | 四体系动效曲线与时长、无障碍硬性要求、审查清单 |
| `references/framework-mappings.md` | Tailwind / React / Vue / Compose / SwiftUI 的令牌映射规则 |
| `scripts/lint_tokens.py` | 可执行校验：硬编码色值、对比度、核心令牌齐全性 |
| `assets/mappings/tailwind.css` | Tailwind v4 `@theme` 令牌映射，四套体系可同页共存 |
