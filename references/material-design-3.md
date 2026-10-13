# Google Material Design 3（Material You）

> 数据来源：Material Design 3 官方色彩系统、Type Scale Tokens、Shape、Elevation、Motion 规范。基线配色以种子色 `#6750A4` 生成；Android 12+ 的动态取色（Dynamic Color）会在运行时替换为壁纸衍生色，但**角色名不变**。

## 1. 设计气质

M3 的核心变化是**从"用阴影表达层级"转向"用色调表达层级"**（tonal elevation）。所有颜色由 HCT 色彩空间从一个种子色生成 13 阶色调梯（tone 0–100），组件消费的是**角色（role）**而不是具体色值——所以亮暗模式只是换一套色调映射，不需要两套设计。

第二个特征是**表达力**：大圆角、大字号、pill 形状按钮、FAB。第三是**个性化**：动态取色让 UI 随用户壁纸变化。

**最重要的一条实现纪律：组件里永远只写角色变量，不写 hex。**

## 2. 颜色角色（明暗完整映射）

### 强调色三组

| 角色 | 亮色 | 暗色 |
|---|---|---|
| `primary` | `#6750A4` | `#D0BCFF` |
| `on-primary` | `#FFFFFF` | `#381E72` |
| `primary-container` | `#EADDFF` | `#4F378B` |
| `on-primary-container` | `#21005D` | `#EADDFF` |
| `secondary` | `#625B71` | `#CCC2DC` |
| `on-secondary` | `#FFFFFF` | `#332D41` |
| `secondary-container` | `#E8DEF8` | `#4A4458` |
| `on-secondary-container` | `#1D192B` | `#E8DEF8` |
| `tertiary` | `#7D5260` | `#EFB8C8` |
| `on-tertiary` | `#FFFFFF` | `#492532` |
| `tertiary-container` | `#FFD8E4` | `#633B48` |
| `on-tertiary-container` | `#31111D` | `#FFD8E4` |

### 错误色（静态，不随动态取色变化）

| 角色 | 亮色 | 暗色 |
|---|---|---|
| `error` | `#B3261E` | `#F2B8B5` |
| `on-error` | `#FFFFFF` | `#601410` |
| `error-container` | `#F9DEDC` | `#8C1D18` |
| `on-error-container` | `#410E0B` | `#F9DEDC` |

### 表面色

| 角色 | 亮色 | 暗色 | 用途 |
|---|---|---|---|
| `background` | `#FFFBFE` | `#1C1B1F` | 页面底 |
| `on-background` | `#1C1B1F` | `#E6E1E5` | — |
| `surface` | `#FFFBFE` | `#1C1B1F` | 默认背景、卡片、面板 |
| `on-surface` | `#1C1B1F` | `#E6E1E5` | 任意 surface 上的文字/图标 |
| `surface-variant` | `#E7E0EC` | `#49454F` | 次级表面 |
| `on-surface-variant` | `#49454F` | `#CAC4D0` | 低强调文字（占位、提示） |
| `surface-container-lowest` | `#FFFFFF` | `#0F0D13` | 最低强调容器 |
| `surface-container-low` | `#F7F2FA` | `#1D1B20` | 低强调容器 |
| `surface-container` | `#F3EDF7` | `#211F26` | 默认容器（导航区） |
| `surface-container-high` | `#ECE6F0` | `#2B2930` | 高强调容器（对话框） |
| `surface-container-highest` | `#E6E0E9` | `#36343B` | 最高强调容器 |
| `surface-dim` | `#DED8E1` | `#141218` | 两主题下最暗表面 |
| `surface-bright` | `#FFFBFE` | `#3B383E` | 两主题下最亮表面 |

### 反色与描边

| 角色 | 亮色 | 暗色 | 用途 |
|---|---|---|---|
| `inverse-surface` | `#313033` | `#E6E1E5` | 与周围对比的浮层（Snackbar）底 |
| `inverse-on-surface` | `#F4EFF4` | `#313033` | 反色表面上的文字 |
| `inverse-primary` | `#D0BCFF` | `#6750A4` | 反色表面上的可操作文字 |
| `outline` | `#79747E` | `#938F99` | 重要边界：输入框边框、焦点环 |
| `outline-variant` | `#CAC4D0` | `#49454F` | 装饰性分隔线、弱边框 |
| `scrim` | `#000000` | `#000000` | 遮罩（用 32% 不透明度） |
| `shadow` | `#000000` | `#000000` | 阴影 |

### 状态层（State Layer）

所有可交互表面在交互态叠加 **`on-*` 色**（即该表面上的前景色）的透明层：

| 状态 | 不透明度 |
|---|---|
| Hover | 8% |
| Focus | 10% |
| Pressed | 10% |
| Dragged | 16% |

CSS 实现：`background: color-mix(in srgb, var(--md-on-surface) 8%, transparent)` 叠在底色上，或用伪元素。

## 3. 排版（15 级 Type Scale）

字体栈：

```css
--font-plain: "Roboto Flex", Roboto, "Noto Sans SC", "Source Han Sans SC",
              "PingFang SC", "Microsoft YaHei", system-ui, sans-serif;
--font-mono: "Roboto Mono", ui-monospace, monospace;
```

Roboto 与 Roboto Flex 是开放字体；Google Sans 是 Google 私有字体，**第三方不得使用**（中文用 Noto Sans SC / 思源黑体）。

| Token | 字号 | 行高 | 字重 | 字距 | 用途 |
|---|---|---|---|---|---|
| `display-large` | 57 | 64 | 400 | -0.25 | 超大展示文字（极少用） |
| `display-medium` | 45 | 52 | 400 | 0 | 短而重要的文字 |
| `display-small` | 36 | 44 | 400 | 0 | — |
| `headline-large` | 32 | 40 | 400 | 0 | 页面标题 |
| `headline-medium` | 28 | 36 | 400 | 0 | 区块标题 |
| `headline-small` | 24 | 32 | 400 | 0 | 子区块标题 |
| `title-large` | 22 | 28 | 400 | 0 | App Bar 标题 |
| `title-medium` | 16 | 24 | 500 | 0.15 | 列表项标题 |
| `title-small` | 14 | 20 | 500 | 0.1 | Tab 标签 |
| `body-large` | 16 | 24 | 400 | 0.5 | **主正文** |
| `body-medium` | 14 | 20 | 400 | 0.25 | 次正文 |
| `body-small` | 12 | 16 | 400 | 0.4 | 说明文字 |
| `label-large` | 14 | 20 | 500 | 0.1 | 按钮文字 |
| `label-medium` | 12 | 16 | 500 | 0.5 | 导航标签、角标 |
| `label-small` | 11 | 16 | 500 | 0.5 | 极小标注 |

15 级不必全用，但**语义映射必须清晰**。中文本地化时把 letter-spacing 归零（Latin 字距破坏汉字节奏），行高可提高 0.1–0.2。

## 4. 形状（Shape）

| Token | 半径 | 典型用法 |
|---|---|---|
| `none` | 0 | 全宽容器 |
| `extra-small` | 4 | 菜单项、文本域顶部 |
| `small` | 8 | Chip |
| `medium` | **12** | **卡片默认** |
| `large` | 16 | FAB（标准） |
| `extra-large` | **28** | **FAB（大）、对话框、底部面板** |
| `full` | 9999 | 按钮（pill）、Chip（选中）、开关 |

嵌套规则：`内层 = 外层 − 内边距`。

## 5. 海拔（Elevation）

M3 的层级**首选色调叠加**（在表面色上叠加 5–14% 的 `primary` 色），阴影只作补充。

| Level | dp | 色调叠加不透明度 |
|---|---|---|
| 0 | 0 | 0% |
| 1 | 1 | 5% |
| 2 | 3 | 8% |
| 3 | 6 | 11% |
| 4 | 8 | 12% |
| 5 | 12 | 14% |

阴影近似值：

| Level | box-shadow |
|---|---|
| 1 | `0 1px 2px rgba(0,0,0,0.30), 0 1px 3px 1px rgba(0,0,0,0.15)` |
| 2 | `0 1px 2px rgba(0,0,0,0.30), 0 2px 6px 2px rgba(0,0,0,0.15)` |
| 3 | `0 1px 3px rgba(0,0,0,0.30), 0 4px 8px 3px rgba(0,0,0,0.15)` |
| 4 | `0 2px 3px rgba(0,0,0,0.30), 0 6px 10px 4px rgba(0,0,0,0.15)` |
| 5 | `0 4px 4px rgba(0,0,0,0.30), 0 8px 12px 6px rgba(0,0,0,0.15)` |

**实现优先顺序**：先换 `surface-container-*` 角色 → 再叠色调 → 最后才用阴影。

## 6. 间距与布局

4dp 基准，常用 `4 / 8 / 12 / 16 / 24 / 32 / 48 / 64`。

断点（Window Size Class）：

| 类别 | 宽度 | 布局 |
|---|---|---|
| Compact | < 600dp | 单列，底部 Navigation Bar |
| Medium | 600–839dp | 双列，Navigation Rail |
| Expanded | ≥ 840dp | 三列，Navigation Drawer |

触控目标 ≥ 48×48dp。

## 7. 组件规格

| 组件 | 规格 |
|---|---|
| **Filled Button** | 高 40dp，圆角 full（pill），底 `primary`，文字 `on-primary` label-large；状态层叠加 `on-primary` 8/10/10% |
| **Tonal Button** | 底 `secondary-container`，文字 `on-secondary-container` |
| **Elevated Button** | 底 `surface-container-low`，文字 `primary`，level 1 阴影 |
| **Outlined Button** | 透明底，1px `outline` 边框，文字 `primary` |
| **Text Button** | 无底无框，文字 `primary`，左右内边距 12dp |
| **FAB** | 56×56dp，圆角 16dp，底 `primary-container`，图标 `on-primary-container`，level 3；大号 FAB 96×96dp 圆角 28dp |
| **Card — Filled** | 圆角 12dp，底 `surface-container-highest`，无阴影，内边距 16dp |
| **Card — Elevated** | 圆角 12dp，底 `surface-container-low`，level 1 阴影 |
| **Card — Outlined** | 圆角 12dp，底 `surface`，1px `outline-variant` 边框 |
| **Text Field — Filled** | 高 56dp，顶部圆角 4dp，底 `surface-container-highest`；聚焦时底部 2px `primary` 指示条 |
| **Text Field — Outlined** | 高 56dp，圆角 4dp，1px `outline` 边框；聚焦时 2px `primary` + 浮动标签变 `primary` |
| **Navigation Bar** | 高 80dp，底 `surface-container`；选中项 = 32×16dp 胶囊指示器（`secondary-container`）+ 图标 `on-secondary-container` |
| **Navigation Rail** | 宽 80dp，垂直排布，顶部 FAB 槽位 |
| **Navigation Drawer** | 宽 360dp，圆角 0 16dp 16dp 0，底 `surface-container-low`；选中项 = pill 形状 `secondary-container` |
| **Top App Bar** | 高 64dp，底 `surface`，滚动后转 `surface-container`；标题 title-large |
| **Chip** | 高 32dp，圆角 8dp，1px `outline`；选中态底 `secondary-container` + 无边框 + 前置勾选图标 |
| **Switch** | 轨道 52×32dp 圆角 full，滑块 24dp 圆形（选中时 28dp）；选中轨道 `primary`，滑块 `on-primary`；未选中轨道 `surface-variant`，滑块 `outline` |
| **Checkbox** | 18×18dp，圆角 2dp；选中底 `primary` + 白色勾 |
| **Radio** | 20dp 圆，选中外环 `primary` + 内点 10dp |
| **Dialog** | 圆角 28dp，底 `surface-container-high`，最小宽 280dp 最大 560dp，内边距 24dp，标题 headline-small，正文 body-medium，按钮右对齐 |
| **Bottom Sheet** | 顶部圆角 28dp，底 `surface-container-low`，顶部 32×4dp 拖拽条（`on-surface-variant`） |
| **Snackbar** | 圆角 4dp，底 `inverse-surface`，文字 `inverse-on-surface`，动作按钮 `inverse-primary`，宽 344dp 或全宽 − 32dp |
| **Menu** | 圆角 4dp，底 `surface-container`，level 2 阴影，项高 48dp |
| **Tooltip** | 圆角 4dp，底 `inverse-surface`，文字 `inverse-on-surface`，label-medium |

## 8. 动效

| 时长 Token | 值 | 用途 |
|---|---|---|
| `short1` | 50ms | 极小状态变化 |
| `short2` | 100ms | 图标状态切换 |
| `short3` | 150ms | 小元素进入 |
| `short4` | 200ms | 常用微交互 |
| `medium1` | 250ms | 小容器展开 |
| `medium2` | 300ms | **默认**：卡片展开、FAB 变换 |
| `medium3` | 350ms | 大容器 |
| `medium4` | 400ms | 复杂转场 |
| `long1–4` | 450–600ms | 全屏转场 |

曲线：

| 名称 | 值 |
|---|---|
| Standard | `cubic-bezier(0.2, 0, 0, 1)` |
| Emphasized decelerate | `cubic-bezier(0.05, 0.7, 0.1, 1)` |
| Emphasized accelerate | `cubic-bezier(0.3, 0, 0.8, 0.15)` |
| Linear | `cubic-bezier(0, 0, 1, 1)`（仅用于进度类） |

进入用 decelerate（长时长），退出用 accelerate（短时长，约为进入的 2/3）。

## 9. 动态配色

用种子色生成完整色板的方式：HCT 色彩空间，种子色取 tone 40 作为 `primary`（亮色）/ tone 80（暗色），其余角色按固定 tone 映射。Web 端可用 `@material/material-color-utilities` 的 `themeFromSourceColor()` 生成，或用 [Material Theme Builder](https://material-foundation.github.io/material-theme-builder/) 导出。

**无论用不用动态色，组件代码只引用角色名。**

## 10. 常见错误

- ❌ 组件里写死 `#6750A4`。必须用角色变量，否则动态取色失效、暗色崩坏。
- ❌ 用 Material 2 的 `#6200EE` / `#03DAC6`（M2 调色板已废弃）。
- ❌ 用纯阴影表达层级。M3 是色调优先。
- ❌ 圆角用小值。卡片 12dp、FAB/弹窗 28dp 是识别特征。
- ❌ 按钮做成小圆角。M3 按钮是 pill。
- ❌ 用 Google Sans 做商用项目字体。
- ❌ 中文没回退字体，落到 Roboto 显示方块或丑陋的默认衬线。
