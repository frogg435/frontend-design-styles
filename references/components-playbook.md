# 组件实现对照手册

同一批核心组件在四套体系下的实现规格。**先定位风格，再读对应列。**

## 通用原则

1. **组件 CSS 里只出现 `var(--token)`**，不出现字面量。
2. **每个交互态都要写**：`default / hover / focus-visible / active / disabled / selected`。只做默认态是最常见的偷工减料。
3. 焦点样式用 `:focus-visible`（不是 `:focus`），保证键盘可见、鼠标点击不出现。
4. 尺寸用 `rem` 或令牌变量，不用魔法数字。
5. 组件自带 `box-sizing: border-box`。

## 1. 按钮

| | MIUIX | Apple HIG | Material 3 | Fluent 2 |
|---|---|---|---|---|
| 高度 | **40px（minWidth 58px）** | 44–50pt | 40dp | 32px（默认） |
| 圆角 | **16px（squircle，非胶囊）** | 10–14pt（主体渐胶囊） | pill（full） | 4px |
| 内边距 | 20px 水平 | 16–20pt 水平 | 24dp 水平 | 12px 水平 |
| 文字 | 17px / 500 | 17pt / Semibold | label-large 14/500/0.1 | 14px / 600 |
| 主按钮底 | `#3482FF` | `#007AFF` | `primary` | `#0F6CBD` |
| 次要按钮 | 浅灰底 `#E6E6E6` | 灰底 `rgba(120,120,128,0.12)` | tonal：`secondary-container` 底 | 描边：白底 + 1px 边框 |
| 三级按钮 | 纯文字蓝 | 纯文字 tint 色 | outlined / text | subtle（透明底，hover 出灰） |
| hover | 底色深一档 | `opacity` 略降 | 叠 `on-primary` 8% | 品牌色深一档 |
| pressed | 底色 `primary-variant` + `scale(0.96)` | `opacity: 0.7` | 叠 `on-primary` 10% | 品牌色更暗 + 无 scale |
| disabled | `disabledPrimary` 底 + `disabledOnPrimary` 文字 | `opacity: 0.35` | 底/文字都降到 12%/38% 不透明度 | `colorNeutralBackgroundDisabled` + `colorNeutralForegroundDisabled` |
| **独有细节** | 按压回弹是强特征 | 主按钮在 iOS 26 趋于胶囊；有 Filled / Gray / Tinted / Plain 四种 | 有 Tonal / Elevated / Outlined / Text 五种变体 | **底边描边比其他三边深 1px** |

## 2. 输入框 / 文本框

| | MIUIX | Apple HIG | Material 3 | Fluent 2 |
|---|---|---|---|---|
| 高度 | 44–48px（多行 56px） | 36–44pt | 56dp | 32px |
| 圆角 | **16px** | 10pt | Filled 顶 4dp / Outlined 四角 4dp | 4px |
| 静止底 | `#F7F7F7` | `tertiarySystemFill` | Filled：`surface-container-highest`；Outlined：透明 | 白底 + 1px 边框 |
| 边框 | 无 | 无 | Outlined 1px `outline` | 1px `colorNeutralStroke1`，**底边加深** |
| 聚焦 | **2px 边框转 `#3482FF`**（常态 0） | tint 色光标 + 微外发光 | 2px `primary` 边框/指示条，标签变 `primary` | 四边转品牌色 2px |
| 占位文字 | `onSurfaceVariantActions`（40% 黑） | `placeholderText` | `on-surface-variant` | `colorNeutralForeground4` |
| 标签 | 前置标签（非浮动） | 无浮动标签 | 浮动标签（Filled 内 / Outlined 骑在边框上） | 常驻顶部标签 + 输入框 |
| 错误态 | 边框 `#E94634` | 下方 `systemRed` 提示 | 边框 + 辅助文字转 `error` | 边框 `#C50F1F` + 下方错误文字 |
| **独有细节** | 与整体大圆角语言一致 | 系统搜索框是 36pt 胶囊 | 双向浮动标签动画 | 底边加粗是签名 |

**错误提示写法**：错误信息必须是**文本**（不能只靠红色），并给输入框加 `aria-invalid="true"` 和 `aria-describedby` 指向错误文字。

## 3. 卡片

| | MIUIX | Apple HIG | Material 3 | Fluent 2 |
|---|---|---|---|---|
| 圆角 | **16px** | 10–20pt | 12dp | 6px |
| 底色 | 亮色 `#FFFFFF`（背景 `#F7F7F7`）；暗色 `#242424` | `secondarySystemGroupedBackground` | Filled：`surface-container-highest`；Outlined：`surface` | `colorNeutralBackground1` |
| 边框 | 暗色用 1px `#404040` | 无 | Outlined 用 1px `outline-variant` | 1px `colorNeutralStroke2` |
| 阴影 | 极轻或不用 | 不用（靠分组） | Elevated 用 level 1 | `shadow2`（双层） |
| 内边距 | 16px | 16pt | 16dp | 12px |
| 层级表达 | 色阶分层 | 分组 + 材质 | 色调叠加 | 描边 + 轻阴影 |

## 4. 导航

| | MIUIX | Apple HIG | Material 3 | Fluent 2 |
|---|---|---|---|---|
| 移动主模式 | 底部 Tab 栏 | 底部 Tab Bar | Navigation Bar | —（桌面体系） |
| 桌面主模式 | 侧边抽屉 | 侧栏 + 大标题栏 | Navigation Rail / Drawer | Navigation Rail / Navigation View |
| 顶部栏高度 | 56px | 44pt（内联）/ 96pt（大标题） | 64dp | 48px |
| 选中态 | 图标/文字变蓝 | 图标变 tint 色 + 标签 | 32×16dp 胶囊指示器 | 左侧 3px 品牌色条 + 图标变品牌色 |
| 独有行为 | — | **大标题→内联标题的滚动收缩** | 响应式：Bar → Rail → Drawer | 可收起/展开（48px ↔ 240px） |

**iOS 大标题收缩**实现要点：滚动 > 50px 时，标题字号从 34pt 过渡到 17pt，同时导航栏从 96pt 收缩到 44pt，加 1px 底边。用 `IntersectionObserver` 或 `scroll` 事件驱动 class 切换。

## 5. 弹层：对话框 / 底部面板 / 浮层

| | MIUIX | Apple HIG | Material 3 | Fluent 2 |
|---|---|---|---|---|
| 对话框圆角 | 20–28px | 14pt | 28dp | 8px |
| 对话框宽 | 80%（≤320px） | 270pt 固定 | 280–560dp | 480px 默认 |
| 底/材质 | `surfaceContainerHighest` | Regular 材质（模糊） | `surface-container-high` | `colorNeutralBackground1` + Acrylic |
| 阴影 | 轻 | 无（靠遮罩 + 材质） | level 3 | `shadow16`（双层） |
| 底部面板 | 顶部圆角 20–28px + 拖拽条 | 顶部圆角 10–16pt + 5×36pt 抓取条 | 顶部圆角 28dp + 32×4dp 拖拽条 | 少用（桌面体系） |
| 遮罩 | `rgba(0,0,0,0.30)` | `rgba(0,0,0,0.40)` | `scrim` 32% | Smoke `rgba(0,0,0,0.30)` |
| 按钮排布 | 取消左、确认右 | 横排等宽 / 竖排 | 右对齐文字按钮 | 右对齐，主按钮在右 |
| 无障碍 | 焦点陷阱 + Esc 关闭 | 同左 | 同左 | 同左 |

**所有弹层都要**：`role="dialog"` `aria-modal="true"`、打开时焦点移入、Tab 循环锁在内部、Esc 与点击遮罩关闭、关闭后焦点回到触发元素。

## 6. 开关 / 选择控件

| | MIUIX | Apple HIG | Material 3 | Fluent 2 |
|---|---|---|---|---|
| Switch 尺寸 | 52×32px | 51×31pt | 52×32dp | 40×20px |
| 滑块 | 24px 圆形 | 27pt 圆形带阴影 | 24dp（选中 28dp） | 12px（选中 14px） |
| 开启色 | `#3482FF` | `#34C759` | `primary` | `#0F6CBD` |
| 关闭色 | `#E6E6E6` / 暗 `surfaceContainerHigh` | `systemFill` | `surface-variant` + `outline` 滑块 | `colorNeutralStrokeAccessible` |
| Checkbox | 圆角 6px | 圆角 6pt，选中 `#007AFF` | 18dp 圆角 2dp，选中 `primary` | 20px 圆角 4px，选中品牌色 |
| Radio | 圆形，选中蓝环 + 内点 | 同 | 20dp，选中 `primary` | 20px，选中品牌色 |
| Slider 轨道 | 4px 圆角 | 4pt | 4dp | 4px 圆角 2px |

## 7. 列表

| | MIUIX | Apple HIG | Material 3 | Fluent 2 |
|---|---|---|---|---|
| 结构 | 分组卡片 | inset grouped 卡片 | 平铺 + 分隔线 | 平铺表格行 |
| 行高 | ≥ 56px | ≥ 44pt | 56dp（两行）/ 48dp（单行） | 32px（默认密度） |
| 分隔线 | `#E0E0E0`（左侧缩进 16px） | `separator`（左侧缩进 16pt） | `outline-variant` | `colorNeutralStroke2` |
| 分组间距 | 16px | 24–35pt | — | — |
| 行 hover | 底色变 `#F7F7F7` | 无（触屏） | 叠 `on-surface` 8% | `colorSubtleBackgroundHover` |
| 行选中 | 整行浅蓝底 | 无 | `secondary-container` | `colorNeutralBackground1Selected` |

## 8. 反馈与提示

| 组件 | MIUIX | Apple HIG | Material 3 | Fluent 2 |
|---|---|---|---|---|
| 轻提示 | Toast，圆角 12–16px，`surfaceContainerHighest` | 无系统 Toast | Snackbar：`inverse-surface` 底，圆角 4dp | InfoBar：48px 高，左 4px 色条 |
| 消息条 | 顶部横幅 | 无 | Banner | InfoBar（error / warning / success / info） |
| 加载 | 圆形进度 + 蓝色 | 系统 spinner | 圆形 / 线性进度条 | 圆形 / 线性 ProgressBar（细线 2px） |
| 骨架屏 | 灰色圆角块 + 微光扫过 | 同 | 同 | 同 |

## 9. 图标与头像

| | MIUIX | Apple HIG | Material 3 | Fluent 2 |
|---|---|---|---|---|
| 图标风格 | 线性圆头，2px 描边 | SF Symbols，多字重可选 | Material Symbols（可变字重/填充） | Fluent System Icons（Regular / Filled 双态） |
| 图标尺寸 | 20–24px | 17–28pt | 24dp | 16 / 20 / 24 / 28 / 32px |
| 头像 | 圆形 | 圆形 | 圆形 | 圆形（单人）/ 圆角方形 | 
| 图标按钮点击区 | ≥ 48px | ≥ 44pt | ≥ 48dp | ≥ 32px（桌面） |

## 10. 状态完整性检查

每个组件交付前确认覆盖：

| 状态 | 是否必做 |
|---|---|
| default | ✅ |
| hover | ✅（桌面端必做） |
| focus-visible | ✅ |
| active / pressed | ✅ |
| disabled | ✅ |
| selected / checked | 有选中语义的组件必做 |
| loading | 异步组件必做 |
| error | 表单类必做 |
| empty | 列表/数据展示类必做 |
| dark theme | ✅ |
| RTL 镜像 | 有多语言需求时做（Fluent 与 M3 都有 RTL 规范） |
| 长文本溢出 | ✅（至少做截断或换行方案） |
