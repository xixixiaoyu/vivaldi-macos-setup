# Arc-like Vivaldi Setup

Codex skill for reproducing a stable, low-distraction Vivaldi setup on macOS.
It covers the top tab bar, right-side sliding bookmark panel, recent-tab
switching, startup recovery, bookmarks, privacy, and performance settings.

Validated with Vivaldi `8.3.4191.44` on 2026-11-14.

## Install on a new Mac

```bash
git clone git@github.com:xixixiaoyu/arc-like-vivaldi-setup.git \
  "$HOME/.codex/skills/arc-like-vivaldi-setup"
```

Invoke the skill as `$arc-like-vivaldi-setup`.

## Verify the current browser

```bash
python3 "$HOME/.codex/skills/arc-like-vivaldi-setup/scripts/check_vivaldi_settings.py"
```

The checker is read-only and never modifies browser data.
