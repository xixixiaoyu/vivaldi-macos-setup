---
name: vivaldi-macos-setup
description: Configure or audit Vivaldi on macOS for a stable, low-distraction daily browsing workflow. Use when preparing a new Mac or reproducing and verifying the user's preferred tab bar, sliding bookmarks panel, tab switching, startup, privacy, and performance settings.
metadata:
  short-description: "Configure a stable Vivaldi workflow on macOS"
---

# Vivaldi macOS Setup

Set up Vivaldi as a stable daily browser while preserving the user's data and
avoiding unnecessary layout churn.

## Target outcome

- Top horizontal tab bar, not a left or right vertical rail.
- Bookmark panel on the right, with only the panel auto-hidden and sliding out
  from the right edge.
- Address bar, tab bar, and bookmarks bar remain visible or hidden independently
  as specified in the checklist.
- Four fixed themes: `暖纸黄` for system light mode, `暖纸夜` for system dark
  mode, plus the alternative dark themes `青灰绿` and `雾紫石墨`.
- Recent-use tab cycling, fast tab search, balanced memory use, session restore,
  light content blocking, and blocked-by-default notifications.
- Existing bookmarks, passwords, history, profiles, and workspaces are preserved.

## Procedure

1. Read [references/ui-checklist.md](references/ui-checklist.md) before changing
   settings. Apply the validated baseline there, adapting only for labels that
   have changed in a newer Vivaldi release.
2. Confirm the installed release is Vivaldi Stable. Do not use a Snapshot build
   as the daily browser without an explicit request.
3. Make changes through `vivaldi://settings/` while Vivaldi is running. Do not
   edit `Preferences` or `Secure Preferences` directly.
4. Keep changes scoped to the user's request. Do not change macOS Dock placement,
   profiles, bookmarks, extensions, or accounts unless explicitly asked.
5. If the user asks for bookmark organization, propose project folders such as
   `工作`, `学习`, and `日常`. Do not create dummy bookmarks or move existing
   content unless requested.
6. Never restore, empty, or delete the bookmark Trash without explicit approval.
   Treat a request to restore UI layout as layout-only.
7. Verify the result in the live window after each category:
   - Tabs are where the user asked them to be.
   - The bookmark panel appears from the intended edge and collapses after focus
     moves back to the page.
   - Settings that should stay fixed, such as the address bar, do not disappear.
   - The navigation toolbar includes Reload, Back, and Forward.
   - No existing tabs, bookmarks, or workspaces were removed.
8. Run:

   ```bash
   python3 scripts/check_vivaldi_settings.py
   ```

   Investigate every `FAIL`. Treat `WARN` and `MANUAL` entries as prompts for a
   live UI check, not as permission to modify data.

## Multi-tab baseline

- `⌃Tab` / `⌃⇧Tab`: cycle in recent-use order.
- `⇧⌘A`: search all tabs.
- `F2` or `⌘E`: Quick Commands; use `tab:` or `workspace:` prefixes.
- `⌘1` through `⌘8`: jump to a tab by position; `⌘9`: last tab.
- Prefer 3-8 pinned tabs. Move project-specific tabs into workspaces and save a
  named session before closing a large working set.

## Data safety

Vivaldi Sync is not a backup. If the user uses sync, explain the recovery-key
risk. Recommend periodic bookmark export or a separately protected profile
backup before major configuration changes.
