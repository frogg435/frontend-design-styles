# frontend-design-styles

一个用于**前端界面设计**的 AI Skill，覆盖四套主流设计语言：

| 设计语言 | 归属 | 主色 |
|---|---|---|
| **MIUIX / HyperOS** | 小米 | `#3482FF` |
| **Apple HIG** | Apple | `#007AFF` |
| **Material Design 3** | Google | 角色化，基线 `#6750A4` |
| **Fluent 2** | Microsoft | `#0F6CBD` |

它的目标不是"看起来差不多"，而是用**语义令牌 + 组件形态 + 动效曲线**三层一致地还原，让成品能被该平台用户认出"这就是 iOS / 这就是 Material / 这就是 Windows"。

在线预览：**<https://frogg435.github.io/frontend-design-styles/>** —— 同一套组件在四种风格下的并列对照，可筛选风格、切换明暗主题。也可直接查看源码 [`assets/templates/showcase.html`](assets/templates/showcase.html)。

## 目录结构

```
frontend-design-styles/
├── SKILL.md                          风格指纹速查表 + 工作流 + 铁律 + 自检清单
├── references/
│   ├── style-router.md               选型决策树、形状语言谱系、混搭禁区
│   ├── miuix-hyperos.md              MIUIX/HyperOS 全量令牌
│   ├── apple-hig.md                  Apple HIG 全量令牌
│   ├── material-design-3.md          MD3 全量令牌
│   ├── fluent-2.md                   Fluent 2 全量令牌
│   ├── components-playbook.md        按钮/表单/卡片/导航/弹层… 逐风格实现对照
│   └── motion-and-accessibility.md   动效曲线 + 无障碍硬指标 + 审查清单
├── assets/
│   ├── tokens/{miuix,apple-hig,material-3,fluent-2}.css   可直接复制的语义令牌（含明暗双主题）
│   └── templates/showcase.html                             组件对照演示页（自包含单文件）
└── scripts/lint_tokens.py            令牌合规与对比度校验脚本
```

## 用法

把 `frontend-design-styles/` 放进 `~/.codebuddy/skills/` 即可被识别。之后向 AI 提出类似需求时会自动生效：

- 「用 Material Design 3 风格做一个后台数据看板」
- 「帮我做一个 iOS 风格的设置页」
- 「这个界面给我改成 Windows 11 / Fluent 2 的感觉」
- 「小米澎湃 OS 风格的卡片列表」

也可以直接用 CSS 令牌文件：单独使用时把 `[data-style="xxx"]` 选择器替换为 `:root`，或保留属性选择器以便多套风格在同一页面共存。

产出后可用校验脚本自查（详见下节）。

## 四套体系的差异速览

| | MIUIX | Apple HIG | Material 3 | Fluent 2 |
|---|---|---|---|---|
| 正文基准 | 16–17px | 17pt | 16sp | 14px |
| 圆角语言 | **16dp 统一 + squircle** | 连续曲率圆角 | 12dp 卡片 / 28dp 弹窗 / 全圆按钮 | 小圆角，控件 4px / 浮层 8px |
| 层次手法 | 色阶分层，几乎不用阴影 | 材质模糊 + 内缩分组列表 | 色调叠加优先，阴影次之 | Mica/Acrylic 材质 + 双层阴影 |
| 动效 | 轻快带弹性，200–300ms | 弹簧物理，从不用 linear | 强调曲线，按时长令牌分级 | 快而克制，150–250ms |
| 点击目标 | ≥ 48dp | ≥ 44pt | ≥ 48dp | 控件高 32px |
| 气质 | 圆润通透、蓝色科技感 | 克制、留白、内容优先 | 色彩表达力强 | 生产力、清晰、桌面原生 |

## 校验脚本

```bash
python3 scripts/lint_tokens.py --style miuix path/to/output.html
```

检查三项：是否残留硬编码色值、文字对比度是否达 WCAG AA、必需的语义令牌是否齐全。

## 数据来源

参考文档中的令牌全部来自第一手资料，不是凭印象整理的：

- **MIUIX / HyperOS**：读取开源组件库 [`compose-miuix-ui/miuix`](https://github.com/compose-miuix-ui/miuix)（Apache-2.0）的 `Colors.kt`（颜色）、`TextStyles.kt`（字阶），以及 `basic/Button.kt`、`Card.kt`、`TextField.kt` 中的 `Defaults` 常量（形状）。另参考官方 `docs/guide/squircle.md` 与小米 HyperOS 官方设计规范。
- **Apple HIG**：Apple 官方 Human Interface Guidelines 的 Typography 与 Color 页面（iOS 15–18 快照）。
- **Material Design 3**：M3 官方色彩系统、Type Scale Tokens、Shape、Elevation、Motion 规范。
- **Fluent 2**：Fluent 2 官方 Design Tokens，暗色值已与官方 `@fluentui/tokens` 包的 `webDarkTheme` 逐项比对一致。

> 说明：HyperOS 的部分间距与动效时长没有公开的 Web 数值表，参考文档中已明确标注为「Web 端建议值」，与有官方/源码来源的颜色、字阶、形状分开呈现，不与推测值混淆。

## 许可

本仓库代码与文档采用 **MIT** 许可证（见 [LICENSE](LICENSE)）。

仓库内引用的设计规范版权归各自权利人所有（Apple、Google、Microsoft、小米），此处仅作技术实现参考引用，不构成对相应设计体系的商标或版权主张。
