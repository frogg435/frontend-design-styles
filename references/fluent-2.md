# Microsoft Fluent 2（Windows 11 / Microsoft 365）

> 数据来源：Fluent 2 官方 Design Tokens（fluent2.microsoft.design）、Fluent UI React v9 的 `webLightTheme` / `webDarkTheme`。Fluent 2 是 Metro → Fluent(2017) → Fabric 之后的统一版本，落地在 Windows 11、Teams、Office、Microsoft 365。

## 1. 设计气质

五大原则：**Light（光）、Depth（深度）、Motion（动效）、Material（材质）、Scale（尺度）**。

落到实现上：
- **生产力优先**：信息密度高，控件紧凑（默认控件高 32px，比 iOS/Material 都小），有 small / medium / large 三档尺寸。
- **材质系统**：Mica（采样桌面壁纸的静态染色，用于窗口背景）、Acrylic（实时模糊，用于浮层/导航面板）、Smoke、Solid。
- **小圆角 + 精确描边**：控件 4px、浮层 8px；控件底边描边比其他三边深 1px，模拟极微弱的立体感——这是 WinUI 3 的招牌细节。
- **克制动效**：150–250ms，减速曲线，不炫技。
- **令牌三层结构**：Primitive（原始色阶）→ Alias（语义角色，如 `colorNeutralBackground1`）→ Component（组件专有令牌）。**组件只消费 Alias**。

## 2. 颜色令牌

### 中性色

| 令牌 | 亮色 | 暗色 | 用途 |
|---|---|---|---|
| `colorNeutralBackground1` | `#FFFFFF` | `#292929` | 默认表面 |
| `colorNeutralBackground2` | `#FAFAFA` | `#1F1F1F` | 次级表面 |
| `colorNeutralBackground3` | `#F5F5F5` | `#141414` | 三级表面 |
| `colorNeutralBackground4` | `#F0F0F0` | `#0A0A0A` | 四级表面 |
| `colorNeutralBackground5` | `#EBEBEB` | `#000000` | 五级表面 |
| `colorNeutralBackground6` | `#E6E6E6` | `#333333` | 六级表面 |
| `colorNeutralForeground1` | `#242424` | `#FFFFFF` | 主文字 |
| `colorNeutralForeground2` | `#424242` | `#D6D6D6` | 次文字 |
| `colorNeutralForeground3` | `#616161` | `#ADADAD` | 三级文字 |
| `colorNeutralForeground4` | `#707070` | `#999999` | 四级文字 |
| `colorNeutralForegroundDisabled` | `#BDBDBD` | `#5C5C5C` | 禁用文字 |
| `colorNeutralStroke1` | `#D1D1D1` | `#666666` | 主描边 |
| `colorNeutralStroke2` | `#E0E0E0` | `#525252` | 次级描边 |
| `colorNeutralStroke3` | `#F0F0F0` | `#3D3D3D` | 极弱描边 |
| `colorNeutralStrokeDisabled` | `#E0E0E0` | `#424242` | 禁用描边 |
| `colorNeutralShadowAmbient` | `rgba(0,0,0,0.12)` | `rgba(0,0,0,0.24)` | 环境阴影 |
| `colorNeutralShadowKey` | `rgba(0,0,0,0.14)` | `rgba(0,0,0,0.28)` | 主阴影 |

### 品牌色

Microsoft 品牌主色 `#0F6CBD`（`colorBrandBackground`）。完整品牌色是 **16 档色阶**（shade10 → shade160，从 L\*=5 到 L\*=98），用 `createLightTheme(brandRamp)` 生成整套主题。

| 令牌 | 亮色 | 暗色 |
|---|---|---|
| `colorBrandBackground` | `#0F6CBD` | `#115EA3` |
| `colorBrandBackgroundHover` | `#115EA3` | `#0F6CBD` |
| `colorBrandBackgroundPressed` | `#0C3B5E` | `#0C3B5E` |
| `colorBrandBackgroundSelected` | `#0F548C` | `#1A5B96` |
| `colorBrandForeground1` | `#0F6CBD` | `#479EF5` |
| `colorBrandForeground2` | `#115EA3` | `#62ABF5` |
| `colorBrandForegroundLink` | `#0F6CBD` | `#479EF5` |
| `colorBrandStroke1` | `#0F6CBD` | `#479EF5` |
| `colorCompoundBrandBackground`（开关/勾选） | `#0F6CBD` | `#479EF5` |
| `colorNeutralForegroundOnBrand` | `#FFFFFF` | `#FFFFFF` |

品牌色阶示例（蓝色，供 `createLightTheme` 使用）：

```
10:  #020305   40:  #1B2E54   80:  #4F72B8   120: #B1CCF2
20:  #0D1525   50:  #24427C   90:  #6E8FD3   130: #C7DAF9
30:  #14203A   60:  #2E549E   100: #87A8E6   140: #DCECFB
              70:  #3A68B8   110: #9CBCF0   160: #FAFCFF
```

### 状态色

| 令牌 | 亮色 | 说明 |
|---|---|---|
| `colorPaletteRedBackground3` | `#C50F1F` | 危险/错误 |
| `colorPaletteGreenBackground3` | `#107C10` | 成功 |
| `colorPaletteYellowBackground3` | `#FDE300` | 警告底（配深色文字） |
| `colorPaletteDarkOrangeBackground3` | `#DA3B01` | 警告/注意 |
| `colorStatusInfoBackground` | `#0078D4` | 信息 |
| `colorPaletteRedForeground1` | `#B10E1C` | 错误文字（亮色） |

## 3. 排版（Type Ramp）

字体栈：

```css
--font-display: "Segoe UI Variable Display", "Segoe UI", "Microsoft YaHei",
                "PingFang SC", system-ui, sans-serif;
--font-body: "Segoe UI Variable Text", "Segoe UI", "Microsoft YaHei",
             "PingFang SC", system-ui, sans-serif;
--font-mono: "Cascadia Code", "Cascadia Mono", Consolas, ui-monospace, monospace;
```

Segoe UI Variable 有 Display / Text 两个光学尺寸变体，小尺寸用 Text、大尺寸用 Display。

| 样式 | 字号 | 行高 | 字重 | 用途 |
|---|---|---|---|---|
| `display` | 68 | 92 | 700 | Hero 标题（极少用） |
| `largeTitle` | 40 | 52 | 600 | 页面标题 |
| `title1` | 32 | 40 | 600 | — |
| `title2` | 28 | 36 | 600 | 区块标题 |
| `title3` | 24 | 32 | 600 | 卡片标题、子区块 |
| `subtitle1` | 20 | 28 | 600 | — |
| `subtitle2` | 16 | 22 | 600 | — |
| `body1` | 14 | 20 | 400 | **默认正文** |
| `body1Strong` | 14 | 20 | 600 | 强调正文 |
| `body2` | 12 | 16 | 400 | 次级正文 |
| `caption1` | 12 | 16 | 400 | 说明、元数据 |
| `caption1Strong` | 12 | 16 | 600 | 强调说明 |
| `caption2` | 10 | 14 | 400 | 极小文字、角标 |

对应的原始字号令牌：

| 令牌 | 字号 | 行高 |
|---|---|---|
| `fontSizeBase100` | 10 | 14 |
| `fontSizeBase200` | 12 | 16 |
| `fontSizeBase300` | 14 | 20 |
| `fontSizeBase400` | 16 | 22 |
| `fontSizeBase500` | 20 | 28 |
| `fontSizeBase600` | 24 | 32 |
| `fontSizeHero700` | 28 | 36 |
| `fontSizeHero800` | 32 | 40 |
| `fontSizeHero900` | 40 | 52 |
| `fontSizeHero1000` | 68 | 92 |

字重：`regular 400` / `medium 500` / `semibold 600` / `bold 700`。标题几乎都是 **Semibold**，这是 Fluent 的辨识特征（对比 iOS 标题用 Regular）。

## 4. 间距、圆角、尺寸

**间距令牌**（横向 / 纵向各一套，值相同）：

| 令牌 | 值 |
|---|---|
| `XXS` | 2px |
| `XS` | 4px |
| `SNudge` | 6px |
| `S` | 8px |
| `MNudge` | 10px |
| `M` | 12px |
| `L` | 16px |
| `XL` | 20px |
| `XXL` | 24px |
| `XXXL` | 32px |

**圆角**：

| 令牌 | 值 | 用途 |
|---|---|---|
| `borderRadiusNone` | 0 | 全宽区域 |
| `borderRadiusSmall` | 2px | 小标签 |
| `borderRadiusMedium` | **4px** | **控件（按钮/输入框/复选框）** |
| `borderRadiusLarge` | **6px** | 卡片 |
| `borderRadiusXLarge` | **8px** | **对话框、Flyout、窗口** |
| `borderRadiusCircular` | 10000px | 胶囊、头像 |

嵌套圆角：外层 8px → 内层 6px → 再内层 4px，**每次减 2px**。不要混搭圆角和直角。

**控件尺寸**：

| 尺寸 | 高度 |
|---|---|
| small | 24px |
| medium | **32px（默认）** |
| large | 40px |

## 5. 海拔与阴影

| 令牌 | 值 | 用途 |
|---|---|---|
| `shadow2` | `0 1px 2px rgba(0,0,0,0.14), 0 0 2px rgba(0,0,0,0.12)` | 卡片静止态 |
| `shadow4` | `0 2px 4px rgba(0,0,0,0.14), 0 0 2px rgba(0,0,0,0.12)` | 下拉 |
| `shadow8` | `0 4px 8px rgba(0,0,0,0.14), 0 0 2px rgba(0,0,0,0.12)` | 弹出层 |
| `shadow16` | `0 8px 16px rgba(0,0,0,0.14), 0 0 2px rgba(0,0,0,0.12)` | 对话框 |
| `shadow28` | `0 14px 28px rgba(0,0,0,0.24), 0 0 8px rgba(0,0,0,0.20)` | 教学提示、最高层 |
| `shadow64` | `0 32px 64px rgba(0,0,0,0.24), 0 0 8px rgba(0,0,0,0.20)` | 最大 |

每个阴影都是**双层**：一个定向主阴影 + 一个无偏移的环境微光。这是 Fluent 阴影的质感来源，不要简化成单层。

## 6. 材质（Mica / Acrylic）

| 材质 | 用途 | Web 近似 |
|---|---|---|
| **Mica** | 窗口/标题栏背景。采样桌面壁纸一次，**静态染色不实时模糊**，性能便宜 | `background: rgba(243,243,243,0.85)` + `backdrop-filter: blur(60px) saturate(125%)` |
| **Mica Alt** | 更不透明的变体 | `rgba(243,243,243,0.9)` |
| **Acrylic（Background）** | 导航面板，位于内容之下 | `background: rgba(252,252,252,0.60)` + `backdrop-filter: blur(30px) saturate(125%)` |
| **Acrylic（In-app）** | Flyout、菜单、浮层 | `background: rgba(252,252,252,0.60)` + `backdrop-filter: blur(60px) saturate(125%)` |
| **Smoke** | 内容上的暗色遮罩 | `rgba(0,0,0,0.30)` |
| **Solid** | 回退 | `colorNeutralBackground1` |

**材质选择决策**：窗口/标题栏 → Mica；导航面板 → Background Acrylic；浮层/菜单 → In-app Acrylic；平台不支持合成模糊 → 纯色回退 + 噪点纹理；用户关闭了"透明效果" → 纯色回退，无模糊无噪点。

**反模式**：把 Acrylic 用在可滚动内容区、列表项、主画布上。Acrylic 触发实时合成器模糊，在这些位置会导致掉帧。Acrylic 只用于**覆盖在内容之上的指挥面**（导航面板、命令栏、浮层）。

> Reveal Highlight（跟随鼠标的高光）是 **Fluent 1（2017）** 的特性，Fluent 2 已经移除。现代 Web 实现不要主动加。

## 7. 组件规格

| 组件 | 规格 |
|---|---|
| **Button（Primary）** | 高 32px，圆角 4px，内边距 12px，底 `colorBrandBackground`，文字白色 14px Semibold；**底边描边比其他三边深 1px**（`border-bottom: 1px solid rgba(0,0,0,0.16)`） |
| **Button（Secondary）** | 底 `colorNeutralBackground1`，1px `colorNeutralStroke1` 边框，文字 `colorNeutralForeground1` |
| **Button（Subtle）** | 默认透明底、无边框；hover 时出现 `colorSubtleBackgroundHover`（`#F5F5F5` / 暗色 `#383838`） |
| **Button（Transparent）** | 完全透明，仅文字，hover 时文字变 brand 色 |
| **TextBox** | 高 32px，圆角 4px，1px `colorNeutralStroke1`；**底边描边比其他三边粗/深**（`border-bottom-width: 2px` 或深一档色）；聚焦时四边转 2px `colorBrandStroke1`，并显示品牌色下划线 |
| **Dropdown / Combobox** | 同 TextBox，右侧 chevron 图标 |
| **Card** | 圆角 6px，底 `colorNeutralBackground1`，1px `colorNeutralStroke2`（或 `colorNeutralStroke1`），`shadow2`，内边距 12px |
| **Dialog** | 圆角 8px，底 `colorNeutralBackground1`，`shadow16`，宽 480px（默认），内边距 24px，标题 subtitle1 20px Semibold，按钮右对齐 |
| **Flyout / Menu** | 圆角 8px，底 `colorNeutralBackground1` + Acrylic，`shadow16`，项高 32px，圆角 4px，内边距 8px 12px |
| **Tooltip** | 圆角 4px，底 `colorNeutralBackground1`，1px `colorNeutralStroke1`，`shadow8`，文字 caption1 |
| **Checkbox** | 20×20px，圆角 4px，1px `colorNeutralStroke1`；选中底 `colorCompoundBrandBackground` + 白勾 |
| **Radio** | 20×20px，圆形，选中外环 brand 色 + 内点 10px |
| **Switch** | 40×20px 胶囊，滑块 12px 圆形（选中 14px）；开启轨道 `colorCompoundBrandBackground` |
| **Slider** | 轨道高 4px 圆角 2px，未填充 `colorNeutralStrokeAccessible`，填充 `colorCompoundBrandBackground`；滑块 20px 圆形白底 + 1px 边框 |
| **ProgressBar** | 高 2px，圆角 1px（细线风格） |
| **InfoBar** | 高 48px，圆角 4px，左侧 4px 强调色条 + 图标 + 文字 + 操作按钮；四种语义色 |
| **Navigation Rail** | 宽 48px（收起）/ 240px（展开），项高 32px，选中项左侧 3px 品牌色指示条 + `colorNeutralBackground1` 底 + 图标变品牌色 |
| **Tab（Pivot）** | 高 44px，文字 subtitle2，选中项底部 2px 品牌色圆角指示条（16px 宽） |
| **CommandBar** | 高 48px，底 `colorNeutralBackground2`，按钮为 Subtle 变体 |
| **Table / DataGrid** | 行高 32px（默认密度）/ 24px（紧凑），表头文字 caption1 Strong，行 hover `colorSubtleBackgroundHover`，行选中 `colorNeutralBackground1Selected` |

**Fluent 的招牌细节（务必实现）**：控件底边描边比其他三边深。WinUI 3 的 Button / TextBox / Dropdown 都靠这个细节获得"微微凸起"的实体感。

```css
.fluent-control {
  border: 1px solid var(--fluent-stroke-1);
  border-bottom-color: var(--fluent-stroke-accessible); /* 深一档 */
}
```

## 8. 动效

| 时长令牌 | 值 | 用途 |
|---|---|---|
| `durationUltraFast` | 50ms | 微状态变化 |
| `durationFaster` | 100ms | 交互反馈 |
| `durationFast` | 150ms | **常用**：hover、按下 |
| `durationNormal` | 200ms | **默认**：展开、切换 |
| `durationGentle` | 250ms | 平缓过渡 |
| `durationSlow` | 300ms | 转场 |
| `durationSlower` | 400ms | 大区域 |
| `durationUltraSlow` | 500ms | 复杂序列 |

曲线：

| 名称 | 值 |
|---|---|
| `curveAccelerateMax` | `cubic-bezier(1, 0, 1, 1)` |
| `curveAccelerateMid` | `cubic-bezier(0.7, 0, 1, 0.5)` |
| `curveDecelerateMax` | `cubic-bezier(0, 0, 0, 1)` |
| `curveDecelerateMid` | `cubic-bezier(0.1, 0.9, 0.2, 1)` |
| `curveEasyEase` | `cubic-bezier(0.33, 0, 0.67, 1)` |
| `curveLinear` | `cubic-bezier(0, 0, 1, 1)` |

进入用 decelerate，退出用 accelerate。**Connected Animation**：共享元素在三阶段内完成形变（Prepare 0ms 快照 → Animate 300ms decelerate 插值位置/尺寸/圆角/透明度 → Complete 0ms 交接）。Web 上用 FLIP 技术实现。

## 9. 响应式与密度

Fluent 2 用**容器查询**而非视口查询：组件适配**容器宽度**，不是窗口宽度。所以同一个 Card 在全宽布局、分栏面板、Teams 标签页里都不用改媒体查询。

```css
.card-host { container-type: inline-size; }
@container (min-width: 480px) { .card { flex-direction: row; } }
```

容器断点建议：Compact `< 320px` → Medium `320–639px` → Large `≥ 640px`。

**密度模式**：Fluent 支持 comfortable（默认）/ compact / spacious 三档，通过调整 `--spacingVerticalM` 一类令牌统一缩放控件内边距。数据密集型界面（Outlook、Excel）用 compact。

## 10. 常见错误

- ❌ 用 `@fluentui/react` v8 的样式语言（那是旧 Fluent，样式已变）。v9 才是 Fluent 2。
- ❌ 大圆角。Fluent 控件圆角 4px、浮层 8px，是**小圆角**体系。
- ❌ 漏掉控件底边描边这个细节，做出来就只是"普通的微软蓝界面"。
- ❌ 把 Acrylic 用在滚动内容区，导致掉帧。
- ❌ 用单层阴影。Fluent 阴影是双层（主阴影 + 环境光）。
- ❌ 标题用 Regular 字重。Fluent 标题几乎都是 Semibold 600。
- ❌ 忽略用户系统设置"透明度效果：关闭"，没做纯色回退。
- ❌ 中文字体没配微软雅黑/苹方回退。
