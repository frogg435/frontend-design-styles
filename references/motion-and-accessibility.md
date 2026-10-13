# 动效与无障碍

## 一、四体系动效令牌对照

### 时长

| 语义 | MIUIX | Apple HIG | Material 3 | Fluent 2 |
|---|---|---|---|---|
| 极快（微反馈） | 100ms | 100ms | 50–100ms | 50–100ms |
| 快（状态切换） | 150ms | 150–200ms | 150–200ms | 150ms |
| 常规（默认） | 250ms | 250ms | 300ms | 200ms |
| 慢（转场） | 300–350ms | 300–400ms | 350–400ms | 300–400ms |
| 超慢（全屏） | 400ms | 400–500ms | 450–600ms | 500ms |

**通用规律**：进入动效长（decelerate），退出动效短（accelerate，约为进入的 2/3）。

### 曲线

| 体系 | 默认曲线 | 备注 |
|---|---|---|
| MIUIX | `cubic-bezier(0.4, 0, 0.2, 1)` | 展开类可带轻微过冲 `cubic-bezier(0.34, 1.2, 0.64, 1)` |
| Apple HIG | `cubic-bezier(0.25, 0.1, 0.25, 1)` | 转场用弹簧 `cubic-bezier(0.32, 0.72, 0, 1)`；**从不用 linear** |
| Material 3 | `cubic-bezier(0.2, 0, 0, 1)` | Emphasized 进出：`(0.05,0.7,0.1,1)` / `(0.3,0,0.8,0.15)` |
| Fluent 2 | `cubic-bezier(0.33, 0, 0.67, 1)` | Decelerate `(0.1,0.9,0.2,1)`，Accelerate `(0.7,0,1,0.5)` |

### 各体系动效特征

| 体系 | 该做 | 不该做 |
|---|---|---|
| MIUIX | 按压回弹 `scale(0.96)`、卡片展开、开关滑动 | 长时间缓动（会显得迟钝） |
| Apple HIG | 弹簧物理、共享元素转场、材质模糊渐变、Sheet 拖拽跟手 | linear、突然出现无过渡 |
| Material 3 | 容器变换（FAB → 全屏）、共享轴转场、涟漪（Ripple） | 修改 FAB 的形状或位置逻辑 |
| Fluent 2 | Connected Animation（FLIP）、克制的 150–250ms 反馈、滚动揭示 | 装饰性动画、炫技动效 |

### 必须降级

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

降级不等于"删掉所有反馈"——保留即时状态变化（颜色、边框），去掉位移和缩放。

## 二、无障碍硬性要求

### 对比度

| 内容 | 最低对比度 |
|---|---|
| 正文文字（< 18pt 或 < 14pt 粗体） | 4.5:1 |
| 大号文字（≥ 18pt 或 ≥ 14pt 粗体） | 3:1 |
| UI 组件与图形（边框、图标、开关） | 3:1 |
| 焦点指示器 | 3:1，且与相邻色有区分 |
| 禁用态文字 | 豁免（但仍应可辨认） |

**实操提醒**：四套体系的官方低强调文字色（如 `tertiaryLabel` 30% 不透明度、`on-surface-variant`）在某些背景上会低于 4.5:1。如果那行文字是用户**必须读**的内容，换更深的层级；只用于装饰或占位才用最低档。

### 键盘与焦点

- 所有可交互元素必须可 Tab 到达，顺序符合阅读顺序。
- 用 `:focus-visible` 定制焦点环，**不要** `outline: none` 而不给替代。
- 弹层内做焦点陷阱，Esc 关闭，关闭后焦点归位。
- 提供"跳到主内容"链接。
- 自定义控件（开关、滑块、标签页）用真实语义元素或补 `role` + `aria-*` + 键盘处理，不要用 `div` + `onclick`。

### 语义与结构

- 一个页面一个 `<h1>`，标题层级不跳级。
- 图片有 `alt`，纯装饰图 `alt=""`。
- 表单控件有 `<label>`（或 `aria-label`），错误用 `aria-invalid` + `aria-describedby`。
- 状态变化用 `aria-live`（`polite` 用于提示，`assertive` 仅用于错误）。
- 用 `<button>` 做按钮、`<a>` 做跳转——不要反过来。

### 触控与指针

| 体系 | 最小目标尺寸 |
|---|---|
| MIUIX | 48×48dp |
| Apple HIG | **44×44pt**（硬性） |
| Material 3 | 48×48dp |
| Fluent 2 | 桌面 32px（可放宽到 24px 但需保证间距）；触屏模式 40px |

目标小于最低尺寸时，用伪元素扩大热区而不是放大视觉尺寸：

```css
.icon-btn::after {
  content: "";
  position: absolute;
  inset: -8px;   /* 视觉 32px → 热区 48px */
}
```

### 文字缩放

- 字号用 `rem`，尊重用户根字号设置。
- 布局在 200% 缩放（WCAG 1.4.4）下不出现内容丢失或横向滚动。
- iOS 要模拟 Dynamic Type 到 AX5（Body ≈ 310%），版式不能崩。
- 不要用 `px` 固定高度锁死文字容器。

### 颜色之外的信号

- 错误态不能只靠红色：加图标或文字说明。
- 图表不能只靠颜色区分系列：加形状、图案或直接标注。
- 链接在正文中不能只靠颜色区分：加下划线。

## 三、各体系特有的无障碍要点

| 体系 | 关键项 |
|---|---|
| MIUIX / HyperOS | 中文字号下限建议 12px；深色下 `#242424` 背景配白字对比度充足，但 `onSurfaceVariantActions`（40% 白）在深色上偏低，避免长文本使用 |
| Apple HIG | Dynamic Type 全 12 档测试；固定尺寸元素（Tab 栏、工具栏图标）实现 Large Content Viewer；VoiceOver 标签完整；减少动态效果设置尊重 |
| Material 3 | 状态层透明度不能替代对比度；动态取色后必须重新校验对比度（M3 的 HCT 生成已保证 tone 40/80 达标，但自定义种子要验）；必须验证 `on-*` 配对是否用对 |
| Fluent 2 | 系统"高对比模式"下所有描边转纯色可见边框；键盘导航是主路径（Windows 用户习惯）；透明度效果关闭时纯色回退；`colorNeutralStrokeAccessible` 专为 3:1 边框对比设计 |

## 四、交付前审查清单

**视觉一致性**
- [ ] 颜色全部走令牌，无硬编码
- [ ] 字阶梯级 ≤ 4 档，正文基准符合该体系
- [ ] 圆角体系自洽，嵌套圆角 = 外层 − 内边距
- [ ] 阴影/材质用法符合该体系
- [ ] 间距落在体系栅格上（8pt / 4dp / Fluent 间距令牌）

**完整性**
- [ ] hover / focus-visible / active / disabled / selected 齐备
- [ ] 明暗双主题都验证
- [ ] 空状态、加载态、错误态都有
- [ ] 长文本、超长数字、无数据都有兜底
- [ ] 窄屏（320px）到宽屏（1440px+）都不破版

**无障碍**
- [ ] 对比度达标（正文 4.5:1，UI 3:1）
- [ ] 焦点环可见且不被遮挡
- [ ] 点击目标尺寸达标
- [ ] Tab 顺序合理，弹层有焦点陷阱
- [ ] 语义元素与 ARIA 正确
- [ ] `prefers-reduced-motion` 已降级
- [ ] 200% 文字缩放下不丢失内容

**风格纯度**
- [ ] 没有混入其他体系的颜色、圆角、组件形态
- [ ] 该体系的签名细节已还原（Fluent 底边描边 / M3 pill 按钮 / iOS 材质 / HyperOS 色阶分层）

**中文**
- [ ] 字体栈含中文字体回退
- [ ] 中文段落 letter-spacing 已归零
- [ ] 中文行高相对拉丁提高 0.1–0.2
- [ ] 标题不出现孤字（可用 `text-wrap: balance`）
