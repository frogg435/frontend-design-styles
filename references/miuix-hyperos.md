# MIUIX / Xiaomi HyperOS 设计语言

> 数据来源：MIUIX 开源组件库（`compose-miuix-ui/miuix`，Apache-2.0）的 `Colors.kt` / `TextStyles.kt` 默认令牌，以及小米官方 HyperOS 设计规范（MiSans 字体、小部件规范）。MIUIX 是 HyperOS 设计语言在 Compose Multiplatform 上的官方开源实现，其默认色板与字阶可直接作为 Web 端的还原基准。

## 1. 设计气质

- **圆润通透**：大圆角、卡片式分组、大量浅灰分层，很少用阴影堆叠。
- **蓝色科技感**：主色是明快的小米蓝 `#3482FF`，占屏比高（按钮、开关、选中态、链接都用它）。
- **色阶分层而非阴影分层**：亮色下靠 `#FFFFFF → #F7F7F7 → #E8E8E8` 三档灰白拉开层次；暗色下靠 `#000000 → #242424 → #2D2D2D`。
- **信息密度中等偏低**，喜欢大间距和分组卡片。
- **MiSans 字体**：小米自研可变字体，字重层级常用 Medium（次要）/ Demibold（主要）区分主次。

## 2. 颜色令牌（完整）

### 亮色 lightColorScheme()

| 令牌 | 值 | 用途 |
|---|---|---|
| `primary` | `#3482FF` | 主色：主按钮、开关开启、选中态 |
| `onPrimary` | `#FFFFFF` | 主色上的文字/图标 |
| `primaryVariant` | `#3482FF` | 主色变体 |
| `onPrimaryVariant` | `#AECDFF` | 主色变体上的文字 |
| `primaryContainer` | `#5D9BFF` | 主色容器（较浅的主色填充） |
| `onPrimaryContainer` | `#FFFFFF` | 主色容器上的文字 |
| `secondary` | `#E6E6E6` | 次级按钮底色 |
| `onSecondary` | `#FFFFFF` | — |
| `secondaryVariant` | `#F0F0F0` | 次级变体 |
| `onSecondaryVariant` | `#303030` | 次级填充上的文字 |
| `secondaryContainer` | `#F0F0F0` | 次级容器 |
| `onSecondaryContainer` | `#A9A9A9` | 次级容器上的文字 |
| `tertiaryContainer` | `#EAF2FF` | 浅蓝容器（标签、提示底） |
| `onTertiaryContainer` | `#3482FF` | 浅蓝容器上的文字（蓝色） |
| `error` | `#E94634` | 错误/危险 |
| `onError` | `#FFFFFF` | — |
| `errorContainer` | `#FDF6F4` | 错误提示底 |
| `onErrorContainer` | `#410002` | 错误提示文字 |
| `background` | `#FFFFFF` | 页面底色 |
| `onBackground` | `#000000` | 页面文字 |
| `onBackgroundVariant` | `#8C93B0` | 页面次级文字（偏蓝灰） |
| `surface` | `#F7F7F7` | 表面（次级背景区） |
| `onSurface` | `#000000` | 表面上的文字 |
| `surfaceVariant` | `#FFFFFF` | 表面变体（卡片默认底色，白） |
| `surfaceContainer` | `#FFFFFF` | 容器表面 |
| `surfaceContainerHigh` | `#E8E8E8` | 高强调容器（分段控件底、禁用底） |
| `surfaceContainerHighest` | `#E8E8E8` | 最高强调容器 |
| `onSurfaceSecondary` | `rgba(0,0,0,0.80)` | 二级文字 |
| `onSurfaceVariantSummary` | `rgba(0,0,0,0.60)` | 摘要文字 |
| `onSurfaceVariantActions` | `rgba(0,0,0,0.40)` | 操作/辅助文字 |
| `onSurfaceContainerVariant` | `#959595` | 容器上三级文字 |
| `onSurfaceContainerHigh` | `#A2A2A2` | — |
| `disabledOnSurface` | `#B2B2B2` | 禁用文字 |
| `disabledPrimary` | `#C2D9FF` | 禁用主色底 |
| `disabledOnPrimary` | `#F3F8FF` | 禁用主色上的文字 |
| `disabledSecondary` | `#F0F0F0` | 禁用次级底 |
| `disabledOnSecondary` | `#FCFCFC` | — |
| `outline` | `#D9D9D9` | 描边、输入框边框 |
| `dividerLine` | `#E0E0E0` | 分隔线 |
| `windowDimming` | `rgba(0,0,0,0.30)` | 弹窗遮罩 |
| `sliderBackground` | `rgba(0,0,0,0.06)` | 滑轨底 |
| `sliderKeyPoint` | `rgba(163,179,205,0.30)` | 滑块刻度 |
| `sliderKeyPointForeground` | `#6EB5FF` | 滑块刻度前景 |

### 暗色 darkColorScheme()

| 令牌 | 值 | 用途 |
|---|---|---|
| `primary` | `#277AF7` | 暗色主色（比亮色更深一档） |
| `onPrimary` | `#FFFFFF` | — |
| `primaryVariant` | `#0073DD` | — |
| `onPrimaryVariant` | `#99C7F1` | — |
| `primaryContainer` | `#338FE4` | — |
| `onPrimaryContainer` | `#FFFFFF` | — |
| `secondary` | `#505050` | — |
| `onSecondary` | `#FFFFFF` | — |
| `secondaryVariant` | `#434343` | — |
| `onSecondaryVariant` | `#D9D9D9` | — |
| `secondaryContainer` | `#434343` | — |
| `onSecondaryContainer` | `#7C7C7C` | — |
| `tertiaryContainer` | `#2B3B54` | 暗色浅蓝容器 |
| `onTertiaryContainer` | `#4788FF` | — |
| `error` | `#F12522` | — |
| `errorContainer` | `#2E0603` | — |
| `onErrorContainer` | `#FFDAD6` | — |
| `background` | `#242424` | **页面底色是深灰不是纯黑** |
| `onBackground` | `rgba(255,255,255,0.90)` | — |
| `onBackgroundVariant` | `#787E96` | — |
| `surface` | `#000000` | 表面退到纯黑，形成对比 |
| `onSurface` | `#F2F2F2` | — |
| `surfaceVariant` | `#242424` | 卡片底色，与背景同色靠描边区分 |
| `surfaceContainer` | `#242424` | — |
| `surfaceContainerHigh` | `#242424` | — |
| `surfaceContainerHighest` | `#2D2D2D` | — |
| `onSurfaceSecondary` | `rgba(255,255,255,0.80)` | — |
| `onSurfaceVariantSummary` | `rgba(255,255,255,0.50)` | — |
| `onSurfaceVariantActions` | `rgba(255,255,255,0.40)` | — |
| `onSurfaceContainerVariant` | `#737373` | — |
| `onSurfaceContainerHigh` | `#666666` | — |
| `disabledOnSurface` | `#666666` | — |
| `disabledPrimary` | `#253E64` | — |
| `disabledOnPrimary` | `#677993` | — |
| `disabledSecondary` | `#3F3F3F` | — |
| `disabledOnSecondary` | `#797979` | — |
| `outline` | `#404040` | — |
| `dividerLine` | `#393939` | — |
| `windowDimming` | `rgba(0,0,0,0.60)` | — |
| `sliderBackground` | `rgba(255,255,255,0.15)` | — |
| `sliderKeyPointForeground` | `#5DAAFF` | — |

**注意暗色的反直觉之处**：`background` 是 `#242424`（深灰），`surface` 是 `#000000`（纯黑）。这是 HyperOS 的特征——大面积用深灰避免 OLED 上的拖影，需要"沉下去"的层级才用纯黑。**不要写成常见的那套"背景纯黑、卡片 #1C1C1E"**。

## 3. 排版

字体栈：

```css
--md-font: "MiSans", "MiSans VF", "HarmonyOS Sans SC", "PingFang SC",
           "Source Han Sans SC", -apple-system, "Segoe UI", Roboto, sans-serif;
```

MIUIX `TextStyles` 默认字阶（单位 sp，Web 端 1sp ≈ 1px）：

| 样式 | 字号 | 行高 | 字重 | 用途 |
|---|---|---|---|---|
| `title1` | 32 | — | — | 页面大标题 |
| `title2` | 24 | — | — | 页面标题 |
| `title3` | 20 | — | — | 区块标题 |
| `title4` | 18 | — | — | 小标题 |
| `headline1` | 17 | — | — | 强调正文 |
| `headline2` | 16 | — | — | 次级强调正文 |
| `subtitle` | 14 | — | **Bold** | 列表项副标题 |
| `body1` | 16 | — | — | 正文（主要） |
| `body2` | 14 | — | — | 正文（次要） |
| `main` | 17 | — | — | 通用文本（默认） |
| `paragraph` | 17 | 1.2em | — | 段落（带行高） |
| `button` | 17 | — | — | 按钮文字 |
| `footnote1` | 13 | — | — | 脚注/辅助 |
| `footnote2` | 11 | — | — | 最小号说明 |

**实现要点**：库里的默认字阶只定义了字号，字重由组件按场景施加。HyperOS 视觉规范里的层级约定是——**主要信息用 Medium 及以上字重，次要信息用 Medium 且降低不透明度**（官方小部件规范：主要信息 MiSans Demibold，次要信息 MiSans Medium + 40% 透明度）。Web 还原建议：

| 层级 | 字号 | 字重 | 颜色 |
|---|---|---|---|
| 页面标题 | 32 | 600 | `--md-on-surface` |
| 区块标题 | 20–24 | 600 | `--md-on-surface` |
| 列表主标题 | 17 | 500 | `--md-on-surface` |
| 列表副标题 / 摘要 | 14 | 400 | `--md-on-surface-secondary` |
| 辅助说明 | 13 | 400 | `--md-on-surface-variant-summary` |
| 段落正文 | 16–17 | 400 | `--md-on-surface` |

中文加 letter-spacing 会破坏汉字节奏，中文段落保持 `letter-spacing: 0`，只有纯数字/英文标签可以加 `0.02em` 左右。

## 4. 形状、间距、动效

**圆角（HyperOS 视觉语言，Web 端推荐实现值）**：

| 元素 | 半径 |
|---|---|
| 按钮 | 高度/2（胶囊），常见 12–22px |
| 输入框 / 选择器 | 12px |
| 卡片 / 列表分组 | 16–20px |
| 对话框 / 底部面板 | 20–28px |
| 小型标签 Chip | 高度/2 或 8px |
| 图标容器 | 12px |
| 桌面小部件（官方规范） | 手机 42px / 折叠屏 38px / 平板 27px |

嵌套圆角遵循 `内层 = 外层 − 内边距`。

**间距**：8px 基准栅格，常用档位 `4 / 8 / 12 / 16 / 20 / 24 / 32 / 48`。页面左右边距手机 16px、平板 24px。列表项垂直内边距 12–14px。卡片内边距 16px。

**动效**：

| 场景 | 时长 | 曲线 |
|---|---|---|
| 按压反馈 | 100–150ms | `cubic-bezier(0.4, 0, 0.2, 1)` |
| 卡片展开 / 弹层 | 250–300ms | `cubic-bezier(0.34, 1.2, 0.64, 1)`（轻微过冲） |
| 页面转场 | 300–350ms | `cubic-bezier(0.4, 0, 0.2, 1)` |
| 开关 / 滑块 | 200ms | `cubic-bezier(0.2, 0, 0, 1)` |

按压反馈是 HyperOS 的强特征：控件按下时 `transform: scale(0.96)` 并伴随底色加深，松开回弹。

## 5. 组件规格

| 组件 | 规格 |
|---|---|
| **主按钮** | 高 44–48px，胶囊，底色 `--md-primary`，文字 `--md-on-primary` 17px；按下底色转 `--md-primary-variant` + scale 0.96；禁用底色 `--md-disabled-primary`，文字 `--md-disabled-on-primary` |
| **次级按钮** | 底色 `--md-secondary`（浅灰），文字 `--md-on-secondary-variant`；同尺寸同圆角 |
| **文字按钮** | 无底色，文字 `--md-primary` 17px |
| **输入框** | 高 44–48px，圆角 12px，底色 `--md-surface`（亮色 `#F7F7F7`），无边框或 1px `--md-outline`；聚焦时边框变 `--md-primary`；占位文字 `--md-on-surface-variant-actions` |
| **卡片** | 底色 `--md-surface-variant`（亮色白），圆角 16–20px，内边距 16px，**亮色下用 1px `--md-divider-line` 或不需要阴影**；暗色下靠 `--md-surface-variant` vs `--md-surface` 的色差或 1px `--md-outline` 区分 |
| **开关** | 轨道 52×32px 胶囊，滑块 24px 圆形白色带阴影；开启轨道 `--md-primary`，关闭 `--md-secondary`（亮色）或 `--md-surface-container-high`（暗色） |
| **分段控件** | 容器底色 `--md-surface-container-high`，圆角 = 容器高/2 − 内边距；选中项白底 + 轻微阴影 + 文字 `--md-on-surface` |
| **列表** | 分组卡片式：组内项白底，项间 1px `--md-divider-line`（左侧留 16px 缩进），组与组之间 16px 间距；每项高 ≥ 56px |
| **导航栏** | 顶部标题栏：标题居中或左对齐，高 56px，底色 `--md-background`，滚动时加 1px `--md-divider-line` 底边；底部 Tab 栏高 56–64px + 安全区 |
| **对话框** | 圆角 20–28px，宽 80%（最大 320px），内边距 24px，按钮右对齐（取消在左、确认在右），遮罩 `--md-window-dimming` |
| **底部面板** | 顶部圆角 20–28px，顶部 4px×36px 拖拽条（`--md-on-surface-variant-actions`），遮罩同上 |
| **提示条 / Toast** | 圆角 12–16px，底色 `--md-surface-container-highest`，内边距 12×16px |

## 6. 常见错误

- ❌ 暗色背景写成 `#000000`。HyperOS 是 `#242424`。
- ❌ 用 Material 的 `#6750A4` 紫或 iOS 的 `#007AFF`。小米蓝是 `#3482FF`。
- ❌ 给卡片加厚重阴影。HyperOS 靠色阶分层，阴影极轻或不用。
- ❌ 圆角用小值（2–4px）。HyperOS 是大圆角语言。
- ❌ 文字用纯 `#000000` 铺满所有层级。至少三档：`#000000` / 80% / 60% / 40%。
- ❌ 中文字体没配 MiSans 回退，落到默认衬线体。
