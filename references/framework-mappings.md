# 框架映射层

SKILL.md 承诺在用户指定框架时切换实现方式。本文给出四种常见落地的映射规则与模板，令牌值一律取自 `assets/tokens/*.css`，**不要在这里重新发明数值**。

## 通用原则

1. 语义令牌是唯一事实来源。任何框架映射都只做"搬运"，不做"改值"。
2. **不要把令牌值内联进组件**。Tailwind 用 `@theme`，React 用令牌对象，Compose 用 `MaterialTheme`/`MiuixTheme`。
3. 框架映射文件必须和 `assets/tokens/*.css` 同步更新。改令牌时两边一起改。

## 1. Tailwind CSS v4

文件：`assets/mappings/tailwind.css`

```css
@import "tailwindcss";
@import "./assets/mappings/tailwind.css";
```

生成的工具类：

| 令牌 | 工具类 |
|---|---|
| `--color-mi-primary` | `bg-mi-primary` / `text-mi-primary` / `border-mi-primary` |
| `--radius-mi-card` | `rounded-mi-card` |
| `--font-ap` | `font-ap` |
| `--shadow-fl-16` | `shadow-fl-16` |

**暗色模式接入（关键）**：直接 `@import` 本文件时工具类引用的是写死的亮色值。要让 `dark:` 生效，改用 `@theme inline` 让工具类指回语义变量：

```css
@theme inline {
  --color-md-primary: var(--md-primary);
  --color-md-surface: var(--md-surface);
  /* … */
}
```

这样 `bg-md-primary` 输出 `background-color: var(--md-primary)`，明暗由 `assets/tokens/material-3.css` 的 `[data-theme="dark"]` 控制，只需切换 `data-theme` 属性。

**反模式**：在模板里写 `bg-[#6750A4]`。任意值语法会绕过令牌体系，`lint_tokens.py` 会报硬编码。

## 2. React / TypeScript

令牌对象 + CSS 变量双轨。**推荐 CSS 变量为主**（明暗切换零成本），令牌对象仅用于需要计算的场合。

```ts
// tokens.ts —— 由 assets/tokens/material-3.css 生成，勿手写数值
export const md = {
  color: {
    primary: "var(--md-primary)",
    onPrimary: "var(--md-on-primary)",
    surface: "var(--md-surface)",
    onSurface: "var(--md-on-surface)",
    outline: "var(--md-outline)",
    error: "var(--md-error)",
  },
  radius: { card: "var(--md-shape-md)", dialog: "var(--md-shape-xl)", full: "var(--md-shape-full)" },
  type: {
    bodyLarge: { fontSize: "var(--md-body-large)", lineHeight: "var(--md-body-large-lh)", letterSpacing: "var(--md-body-large-ls)" },
    labelLarge: { fontSize: "var(--md-label-large)", lineHeight: "var(--md-label-large-lh)" },
  },
  motion: { standard: "var(--md-easing-standard)", medium2: "var(--md-duration-medium2)" },
} as const;
```

```tsx
export function Button({ variant = "filled", ...rest }: Props) {
  return (
    <button
      className={`md-btn md-btn--${variant}`}
      style={{ borderRadius: md.radius.full, fontFamily: md.type.labelLarge.fontFamily }}
      {...rest}
    />
  );
}
```

**明暗切换**：在根节点上设 `data-theme="dark"`，CSS 变量自动换值，React 不需要重渲染。

**反模式**：`style={{ background: "#6750A4" }}`；或用 JS state 存主题导致全树重渲染。

## 3. Vue 3

与 React 同理，但更倾向直接用 CSS 变量 + `v-bind()`：

```vue
<script setup lang="ts">
const radius = "var(--md-shape-md)";
</script>

<template>
  <button class="md-btn">确定</button>
</template>

<style scoped>
.md-btn { border-radius: v-bind(radius); background: var(--md-primary); color: var(--md-on-primary); }
</style>
```

单文件组件里**直接写 `var(--md-…)` 即可**，不必经过 JS。scoped 样式不会破坏令牌继承。

## 4. Jetpack Compose（Android / Compose Multiplatform）

四套体系都有官方 Compose 实现，**优先用官方库，不要自己造 `MaterialTheme`**：

| 体系 | 官方库 | 主题入口 |
|---|---|---|
| Material 3 | `androidx.compose.material3` | `MaterialTheme(colorScheme = …)` |
| MIUIX / HyperOS | [`top.yukonga.miuix.kmp:miuix`](https://github.com/compose-miuix-ui/miuix) | `MiuixTheme(colors = …)` |
| Apple HIG | 无官方 Compose 实现 | 自建 `AppleTheme`（映射见下） |
| Fluent 2 | 无官方 Compose 实现 | 自建 `FluentTheme` |

**MIUIX** —— 库已内置全部令牌，直接用默认值即可，不要覆写：

```kotlin
MiuixTheme(colors = if (isSystemInDarkTheme()) darkColorScheme() else lightColorScheme()) {
    // 组件自动取当前主题，颜色/字阶/形状都来自库内 Defaults
    Button(onClick = { }) { Text("确定") }   // 16dp 圆角、40dp 高，自动生效
}
```

**Material 3** —— 用 `lightColorScheme()` / `darkColorScheme()` 的参数覆写品牌色，**角色名不变**：

```kotlin
val scheme = lightColorScheme(
    primary = Color(0xFF1976D2),          // 只覆品牌相关角色
    onPrimary = Color.White,
)
MaterialTheme(colorScheme = scheme, typography = Typography(), shapes = Shapes()) { … }
```

**Apple HIG / Fluent 2 自建主题** —— 按 `assets/tokens/*.css` 的值建 `data class`，不要散落字面量：

```kotlin
data class AppleColors(
    val tint: Color,            // #007AFF / #0A84FF
    val label: Color,           // #000000 / #FFFFFF
    val labelSecondary: Color,  // rgba(60,60,67,.6) / rgba(235,235,245,.6)
    val bg: Color,              // #FFFFFF / #000000
    val bgGrouped: Color,       // #F2F2F7 / #000000
    val separator: Color,
)
val LocalAppleColors = staticCompositionLocalOf { lightAppleColors() }

@Composable fun AppleTheme(dark: Boolean = isSystemInDarkTheme(), content: @Composable () -> Unit) {
    CompositionLocalProvider(LocalAppleColors provides if (dark) darkAppleColors() else lightAppleColors()) {
        content()
    }
}
```

**形状注意**：MIUIX 与 iOS 都是连续曲率圆角。Compose 里 MIUIX 用库自带的 `squircleSurface`；自建 iOS 主题时用 `RoundedCornerShape` 只是回退，可叠加 `graphicsLayer` + 路径做 squircle。

## 5. SwiftUI / iOS 原生

```swift
extension Color {
    static let apTint      = Color(uiColor: .systemBlue)          // 自动适配明暗
    static let apLabel     = Color(uiColor: .label)
    static let apSeparator = Color(uiColor: .separator)
    static let apFill      = Color(uiColor: .systemFill)
}
// 能用系统语义色就用系统语义色，别手写 hex —— 苹果会随系统版本微调
```

排版用**样式**而非固定字号：`.font(.body)`、`.font(.headline)`，这样 Dynamic Type 全 12 档自动生效。写 `.font(.system(size: 17))` 会破坏无障碍缩放。

## 6. Flutter

M3 与 MIUIX 都有 Flutter 生态映射，但更建议 Web 端与原生端各自维护令牌源，用 **Style Dictionary / tokens studio** 之类的工具从同一份 JSON 生成 CSS 变量 + `ThemeData`，避免双份手写。

## 7. 映射时的常见错误

- ❌ Tailwind 里用 `bg-[#hex]` 任意值语法。
- ❌ React 里把明暗两套值都放进 JS，用条件运算切换——用 CSS 变量，一行 `data-theme` 搞定。
- ❌ Compose 里覆写 `MaterialTheme` 的所有 29 个角色，却只改了品牌色相关的几个。
- ❌ 自建 Apple/Fluent 主题时把令牌值散落在组件里，而不是收敛到一个 `Colors` data class。
- ❌ SwiftUI 用 `.font(.system(size:))` 固定字号，破坏 Dynamic Type。
- ❌ 框架映射文件与 `assets/tokens/*.css` 数值不一致（改令牌忘改映射）。
