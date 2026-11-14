# Vivaldi macOS UI checklist

Validated on macOS with Vivaldi `8.3.4191.44` on 2026-11-14. UI labels can move
in later releases; prefer the described behavior over hard-coded click positions.

## 1. Tabs and navigation

Open `设置 > 标签页`.

- `标签栏位置`: 顶部
- `悬停时展开标签栏`: 关闭（在顶部布局中通常不可用）
- `关闭 10 个或更多标签需确认`: 开启
- `关闭最后一个标签页不关闭窗口`: 开启
- `标签循环`: 按最近使用顺序循环

Open `设置 > 键盘 > 标签页` only if the user wants a custom shortcut. Keep
`Control+Tab` and `Control+Shift+Tab` as the default cycling shortcuts.

For the validated top tab-bar layout, use the Vivaldi toolbar editor and keep
this order:

`TabButton` → `Extensions` → `Reload` → flexible spacer → `Back` → `Forward`
→ `AddressField`

The Reload, Back, and Forward controls must all remain present. If they are not,
edit only the affected toolbar instead of resetting unrelated toolbars.

## 2. Bookmark panel

Open `设置 > 面板`.

- `面板位置`: 右侧
- `显示面板开关`: 开启
- `悬浮面板`: 关闭
- `显示文件夹计数器`: 开启
- Bookmark panel width: approximately 260 px

Open `设置 > 外观 > 界面元素自动隐藏`.

- `启用界面元素自动隐藏`: 开启
- `面板`: 开启
- `地址栏`: 关闭
- `标签栏`: 关闭
- `状态栏`: 关闭
- `书签栏`: 关闭
- `全屏模式始终自动隐藏`: 开启

Expected behavior: hovering or using the right-side panel control exposes the
bookmarks panel; returning focus to the page collapses it. The address bar and
tab bar must remain available.

Use `Option+Command+B` (`⌥⌘B`) to open or close the bookmark panel.

## 3. Bookmarks

Open `设置 > 书签`.

- `显示书签栏`: 关闭
- `单击打开书签面板中的书签`: 开启

Optional organization:

- Create one top-level folder per context, for example `工作`, `学习`, `日常`.
- If the user wants one-click access from the Start Page, enable `快速拨号` on a
  bookmark folder and select it in the Start Page navigation.
- Do not add example or placeholder bookmarks unless the user asks for a demo.

## 4. Startup and restoration

Open `设置 > 一般 > 启动`.

- `启动时打开`: 上次会话
- `延迟加载恢复的标签页`: 开启
- `总是加载固定标签页`: 开启 when a small set of pinned tabs should be ready
  immediately
- Enabling workspaces requires `上次会话`

The goal is a fast startup without discarding the user's working context.

## 5. Appearance and theme

Open `设置 > 外观`.

- `用户界面紧凑度`: user preference; the validated baseline is regular density
- `使用单色设置图标`: 开启
- `显示标题栏`: 关闭
- `弱化背景窗口颜色`: 开启
- `开启动画效果`: 开启
- `界面缩放`: 100%

Use `设置 > 主题` next.

- `跟随系统`: 开启
- Light theme: `暖纸黄`
- Dark theme: `暖纸夜`
- Keep `青灰绿` and `雾紫石墨` as alternative dark themes
- Do not force the dark theme across all websites by default; it can break sites.

Create all four themes from the built-in Dark theme. Use the following values:

| Property | 暖纸黄 | 暖纸夜 | 青灰绿 | 雾紫石墨 |
|---|---|---|---|---|
| Background | `#f4efe4` | `#211d18` | `#191d1b` | `#1c1b20` |
| Foreground | `#2d2a25` | `#ede5d7` | `#e7f0eb` | `#ecebf2` |
| Highlight | `#c86e4d` | `#d58a5d` | `#66a68c` | `#7a6ccb` |
| Accent | `#e5b66e` | `#c9a86a` | `#86bca6` | `#9c92e2` |
| Window background | `#2e2f37` | `#2e2f37` | `#2e2f37` | `#2e2f37` |
| Color mode | Unified | Unified | Unified | Unified |
| Accent from active page | Off | Off | Off | Off |
| Background saturation limit | 75% | 75% | 75% | 75% |
| Contrast | 0 | 0 | 0 | 0 |
| Radius | 8 | 8 | 8 | 8 |

Set `暖纸黄` as the light schedule and `暖纸夜` as the dark schedule. The warm
cream palette is limited to light mode; dark mode uses a genuinely dark warm
brown palette.

## 6. Privacy and permissions

Open `设置 > 隐私与安全 > 广告和跟踪器拦截器`.

- Default level: 轻度
- Keep `阻止网站上滥用的广告` enabled
- Use per-site exceptions when a login, media player, or checkout fails

Open `设置 > 隐私与安全`.

- `要求网站不要跟踪我`: 开启
- `阻止超链接审计跟踪`: 开启
- `网络钓鱼和恶意软件防护`: 开启
- `使用 DNS 服务以助减少导航错误`: 开启
- Address-field and search-box suggestions: user preference; keep off if the
  user prioritizes privacy

Open `设置 > 隐私与安全 > 网站权限 > 全局权限`.

- `通知`: 阻止
- `位置`: 询问
- `麦克风`: 询问
- `摄像头`: 询问
- `Cookie`: 允许（默认）
- `JavaScript`: 允许（默认）
- `弹出窗口`: 阻止
- `自动全屏`: 阻止
- Third-party cookies: block in private windows only

Use site-specific exceptions for notifications or media permissions. Do not set
all permissions to maximum privacy; that commonly breaks normal browsing.

## 7. Performance and updates

Open `设置 > 性能`.

- `使用硬件加速`: 开启 unless the machine has reproducible GPU or video issues
- `节能`: 电池电量低于 20% 时启用
- `内存优化器`: 均衡优化
- `预读资源`: 开启

Open `设置 > 一般 > 更新`.

- `自动下载并安装更新`: 开启

## 8. Extensions and data

- Minimize extensions and avoid multiple blockers or duplicate tab managers.
- Prefer Vivaldi's built-in vertical tabs, tab stacks, workspaces, panels, and
  Quick Commands over extensions that duplicate them.
- Sync is optional and end-to-end encrypted; it is not a backup.
- If sync is enabled, confirm the recovery/encryption key is stored safely.
- Export bookmarks periodically before large browser changes.

## 9. Final acceptance checks

1. Open several tabs and confirm `Control+Tab` follows recent-use order.
2. Confirm `Shift+Command+A` can find tabs by title.
3. Open the bookmarks panel with `Option+Command+B`.
4. Confirm the panel is on the right.
5. Click the page and confirm only the panel slides away.
6. Confirm the address bar and top tab bar remain visible.
7. Open `vivaldi://settings/content/notifications` and confirm notifications are
   blocked by default.
8. Restart Vivaldi and confirm the previous session, pinned tabs, and workspaces
   are restored as expected.
