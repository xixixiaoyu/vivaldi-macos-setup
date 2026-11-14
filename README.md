# Vivaldi macOS Setup

Codex skill for reproducing a stable, low-distraction Vivaldi workflow on macOS.
It covers the top tab bar, right-side sliding bookmark panel, recent-tab
switching, startup recovery, the `雾紫石墨` and `青灰绿` dark themes, bookmarks,
privacy, and performance settings.

Validated with Vivaldi `8.3.4191.44` on 2026-11-14.

## Install on a new Mac

```bash
git clone git@github.com:xixixiaoyu/vivaldi-macos-setup.git \
  "$HOME/.codex/skills/vivaldi-macos-setup"
```

Invoke the skill as `$vivaldi-macos-setup`.

## Verify the current browser

```bash
python3 "$HOME/.codex/skills/vivaldi-macos-setup/scripts/check_vivaldi_settings.py"
```

The checker is read-only and never modifies browser data.
