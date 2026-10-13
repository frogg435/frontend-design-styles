# Apple Human Interface Guidelines（iOS / iPadOS）

> 数据来源：Apple 官方 HIG 的 Typography 与 Color 页面（iOS 15–18 快照）。色值是官方语义色，字阶是 Dynamic Type 默认（Large）档。

## 1. 设计气质

三条核心原则：**Clarity（清晰）**——任何尺寸下文字可读、图标精确、装饰克制；**Deference（顺从）**——UI 让位于内容，内容填满屏幕；**Depth（深度）**——用图层、半透明材质和动效传达层级。

落到实现上就是：大量留白、克制的色彩（彩色只出现在有意义的交互元素上）、内容区与导航区靠**材质模糊**而非边框区分、分组列表（inset grouped）作为主力容器。

## 2. 颜色令牌（完整）

### 系统色（语义强调色）

| 名称 | 亮色 | 暗色 | 用途 |
|---|---|---|---|
| `systemRed` | `#FF3B30` | `#FF453A` | 错误、破坏性操作 |
| `systemOrange` | `#FF9500` | `#FF9F0A` | 警告、中等强调 |
| `systemYellow` | `#FFCC00` | `#FFD60A` | 注意、提示 |
| `systemGreen` | `#34C759` | `#30D158` | 成功、确认 |
| `systemMint` | `#00C7BE` | `#63E6E2` | 健康、金融 |
| `systemTeal` | `#30B0C7` | `#40CBE0` | 信息类 |
| `systemCyan` | `#32ADE6` | `#64D2FF` | 媒体控制、活力强调 |
| `systemBlue` | `#007AFF` | `#0A84FF` | **默认 tint**：链接、选中态、主操作 |
| `systemIndigo` | `#5856D6` | `#5E5CE6` | 创意、高级功能 |
| `systemPurple` | `#AF52DE` | `#BF5AF2` | 娱乐、功能高亮 |
| `systemPink` | `#FF2D55` | `#FF375F` | 社交、生活类 |
| `systemBrown` | `#A2845E` | `#AC8E68` | 自然、有机 |
| `systemGray` | `#8E8E93` | `#8E8E93` | 次要文字、禁用态（**明暗同值**） |

### 灰阶

| 名称 | 亮色 | 暗色 |
|---|---|---|
| `systemGray2` | `#AEAEB2` | `#636366` |
| `systemGray3` | `#C7C7CC` | `#48484A` |
| `systemGray4` | `#D1D1D6` | `#3A3A3C` |
| `systemGray5` | `#E5E5EA` | `#2C2C2E` |
| `systemGray6` | `#F2F2F7` | `#1C1C1E` |

### 文字层级（Label）

| 名称 | 亮色 | 暗色 | 说明 |
|---|---|---|---|
| `label` | `#000000` | `#FFFFFF` | 主文字 |
| `secondaryLabel` | `rgba(60,60,67,0.60)` | `rgba(235,235,245,0.60)` | 次要文字 |
| `tertiaryLabel` | `rgba(60,60,67,0.30)` | `rgba(235,235,245,0.30)` | 三级/占位 |
| `quaternaryLabel` | `rgba(60,60,67,0.18)` | `rgba(235,235,245,0.18)` | 最低强调 |
| `placeholderText` | `rgba(60,60,67,0.30)` | `rgba(235,235,245,0.30)` | 输入框占位 |

### 背景

| 名称 | 亮色 | 暗色 | 用途 |
|---|---|---|---|
| `systemBackground` | `#FFFFFF` | `#000000` | 根背景 |
| `secondarySystemBackground` | `#F2F2F7` | `#1C1C1E` | 分组容器背景 |
| `tertiarySystemBackground` | `#FFFFFF` | `#2C2C2E` | 分组内的卡片 |
| `systemGroupedBackground` | `#F2F2F7` | `#000000` | 分组列表页面底 |
| `secondarySystemGroupedBackground` | `#FFFFFF` | `#1C1C1E` | 分组列表的单元格 |
| `tertiarySystemGroupedBackground` | `#F2F2F7` | `#2C2C2E` | — |

### 填充与分隔

| 名称 | 亮色 | 暗色 |
|---|---|---|
| `systemFill` | `rgba(120,120,128,0.20)` | `rgba(120,120,128,0.36)` |
| `secondarySystemFill` | `rgba(120,120,128,0.16)` | `rgba(120,120,128,0.32)` |
| `tertiarySystemFill` | `rgba(118,118,128,0.12)` | `rgba(118,118,128,0.24)` |
| `quaternarySystemFill` | `rgba(116,116,128,0.08)` | `rgba(118,118,128,0.18)` |
| `separator` | `rgba(60,60,67,0.29)` | `rgba(84,84,88,0.60)` |
| `opaqueSeparator` | `#C6C6C8` | `#38383A` |

**关键实现规则**：永远优先用语义色，不要用固定 hex。暗色模式不是亮色的反转——亮色用**阴影**表达层级，暗色用**发光/更亮的表面**表达层级，阴影在暗色下基本不可见。

## 3. 排版

字体栈：

```css
--font-sans: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display",
             "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", sans-serif;
--font-rounded: ui-rounded, "SF Pro Rounded", var(--font-sans);
--font-mono: ui-monospace, "SF Mono", SFMono-Regular, Menlo, monospace;
```

SF Pro 有光学尺寸：**< 20pt 用 SF Pro Text**（字距更松、笔画更结实），**≥ 20pt 用 SF Pro Display**（字距更紧、细节更精致）。`-apple-system` 会自动处理，Web 上不用手动切换。

### Dynamic Type 默认（Large）字阶

| 样式 | 字号 | 行高 | 字重 | 用途 |
|---|---|---|---|---|
| Large Title | 34 | 41 | Regular 400 | 页面大标题（强调态 Bold） |
| Title 1 | 28 | 34 | Regular 400 | 一级标题（强调态 Bold） |
| Title 2 | 22 | 28 | Regular 400 | 二级标题（强调态 Bold） |
| Title 3 | 20 | 25 | Regular 400 | 三级标题（强调态 Semibold） |
| Headline | 17 | 22 | **Semibold 600** | 行标题、卡片标题 |
| Body | 17 | 22 | Regular 400 | 正文（强调态 Semibold） |
| Callout | 16 | 21 | Regular 400 | 短辅助文字 |
| Subhead | 15 | 20 | Regular 400 | 支持性行文字 |
| Footnote | 13 | 18 | Regular 400 | 元数据、时间戳 |
| Caption 1 | 12 | 16 | Regular 400 | 标签 |
| Caption 2 | 11 | 13 | Regular 400 | 最小号说明 |

### Dynamic Type 全尺寸档

12 档：`xSmall / Small / Medium / Large（默认）/ xLarge / xxLarge / xxxLarge` + 无障碍档 `AX1–AX5`。Body 在 AX5 下可放大到约 **310%**，Large Title 约 155%。

Web 实现用 `rem` + `clamp()` 模拟，或用 `font: -apple-system-body` 系列。至少做到：**正文可随用户字号缩放，且不回流出裁剪**。

标准档相对 Large 的比例：xSmall ≈ 0.82，Small ≈ 0.88，Medium ≈ 0.94，xLarge ≈ 1.06，xxLarge ≈ 1.12，xxxLarge ≈ 1.18。

### 字重

| 字重 | 值 | 用途 |
|---|---|---|
| Regular | 400 | 正文 |
| Medium | 500 | 按钮、强调 |
| Semibold | 600 | 副标题、Headline |
| Bold | 700 | 标题、关键信息 |
| Heavy/Black | 800/900 | 罕见，营销页 |

**反面**：小尺寸下不要用 Light 及以下字重，可读性崩坏。Caption 2（11pt）只用于时间戳、角标，不要用于用户需要阅读的正文。

## 4. 布局与间距

- **8pt 栅格**：间距取 8 / 16 / 24 / 32。
- **安全区**：`env(safe-area-inset-top/right/bottom/left)` 必须处理，内容不得进状态栏和 Home Indicator 区域。
- **页面水平边距**：16pt（紧凑）或 20pt（常规）。
- **最小点击目标：44×44pt**（硬性要求，不可低于）。
- 分组列表：单元格高 ≥ 44pt，组内单元格之间留 1px `separator`（左缩进 16pt 对齐文字），组间留 24–35pt。
- 内容行长 45–75 字符。

## 5. 形状与材质

**圆角**：Apple 用**连续曲率**（squircle），不是标准几何圆角。Web 上无法完全复刻，用 `border-radius` 近似，但要注意：

- 容器圆角 10–20pt（卡片、按钮、输入框常见 10–12pt，气泡/大卡片 16–20pt）。
- 嵌套圆角：`内层 = 外层 − 内边距`。
- 小组件、图标容器可用 6–8pt。

**材质（Material / Translucency）**：

| 材质 | 用途 | Web 近似 |
|---|---|---|
| Ultra Thin | 全屏遮罩层 | `backdrop-filter: blur(10px) saturate(180%)` + `rgba(255,255,255,0.5)` |
| Thin | 侧滑面板 | `blur(20px)` + `rgba(255,255,255,0.65)` |
| Regular | 导航栏、Tab 栏 | `blur(20px) saturate(180%)` + `rgba(249,249,249,0.78)` |
| Thick | 浮层、菜单 | `blur(30px)` + `rgba(255,255,255,0.85)` |
| Chrome | 工具栏 | 同 Regular，暗色下 `rgba(30,30,30,0.72)` |

暗色模糊底用 `rgba(30,30,30,0.72)` 一类深灰，不要用纯黑（会显得死板）。

## 6. 组件规格

| 组件 | 规格 |
|---|---|
| **导航栏（大标题）** | 高 96pt（大标题态）/ 44pt（内联态）；顶部 Large Title 34pt Bold，滚动约 50px 后收缩为 17pt Semibold 内联标题；滚动后加 1px `separator` 底边 + Regular 材质 |
| **底部 Tab 栏** | 高 49pt + 底部安全区；图标 25×25pt，标签 10pt；选中项 tint 色 |
| **Filled 按钮** | 高 44–50pt，圆角 10–14pt（iOS 26 起主按钮趋于胶囊），底色 = tint（默认 `#007AFF`），文字白色 17pt Semibold；按下 `opacity: 0.7` 或轻微 `scale(0.98)` |
| **Gray 按钮** | 底色 `rgba(120,120,128,0.12)`（亮）/ `rgba(120,120,128,0.24)`（暗），文字 tint 色 |
| **Tinted 按钮** | 底色 = tint 的 12–15% 透明版，文字 tint 色 |
| **Plain 按钮** | 无底无色块，文字 tint 色 17pt |
| **输入框 / 搜索框** | 高 36pt（系统搜索框）或 44pt；圆角 10pt；底色 `tertiarySystemFill`；占位文字 `placeholderText`；聚焦时出现 tint 色光标与 3–4pt 外发光 |
| **分组列表** | inset grouped：每张卡片圆角 10pt，白底（暗色 `#1C1C1E`），左右缩进 16pt；行内左图标（可选）+ 主文字 17pt + 右副文字 `secondaryLabel` + chevron；行高 ≥ 44pt |
| **开关（Switch）** | 51×31pt 胶囊，滑块 27pt 白色圆形带阴影；开启 `#34C759` |
| **分段控件** | 高 32pt，容器底 `tertiarySystemFill` 圆角 8–9pt，选中项白底 + 阴影 + 1px 边框 |
| **底部面板（Sheet）** | 顶部圆角 10–16pt，顶部 5×36pt 拖拽条（`systemFill` 色），有遮罩，向下拖拽关闭 |
| **Alert** | 宽 270pt 固定，圆角 14pt，Regular 材质，标题 17pt Semibold，正文 13pt，按钮横排 44pt 高 |
| **Action Sheet** | 底部弹出，圆角 14pt，每项 57pt 高，破坏性操作用 `systemRed`，取消项单独一卡片 |

## 7. 动效

| 场景 | 时长 | 曲线 |
|---|---|---|
| 按钮/控件状态 | 150–250ms | `cubic-bezier(0.25, 0.1, 0.25, 1)` |
| 页面转场 | 300–350ms | 弹簧物理，Web 用 `cubic-bezier(0.32, 0.72, 0, 1)` |
| Sheet 弹出 | 400–500ms | 弹簧 |
| 按压反馈 | 100ms | `transform: scale(0.96)` |

**禁止**用 `linear`。iOS 的动效是**减速曲线**（开始快结尾慢）为主，交互反馈可以带轻微过冲。

## 8. 常见错误

- ❌ 用 `#007AFF` 铺满整个界面。tint 色只用于可交互元素。
- ❌ 暗色模式用 `filter: invert()`，或用亮色的阴影层级。
- ❌ 点击目标小于 44×44pt。
- ❌ 用硬边框分隔区域。iOS 靠材质模糊 + 内缩分组。
- ❌ 圆角给小值（4px）。iOS 是大圆角 + 连续曲率。
- ❌ 页面内容没处理 `safe-area-inset`，被刘海/Home 指示条压住。
- ❌ 中文用 SF Pro 直接渲染，未配置苹方回退。
