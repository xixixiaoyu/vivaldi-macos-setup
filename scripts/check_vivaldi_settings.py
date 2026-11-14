#!/usr/bin/env python3
"""Read-only audit of the validated Vivaldi macOS baseline."""

from __future__ import annotations

import json
import plistlib
import sys
from pathlib import Path
from typing import Any


APP = Path("/Applications/Vivaldi.app")
PROFILE = Path.home() / "Library/Application Support/Vivaldi/Default/Preferences"
LOCAL_STATE = Path.home() / "Library/Application Support/Vivaldi/Local State"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def nested(data: dict[str, Any], path: str) -> Any:
    value: Any = data
    for part in path.split("."):
        if not isinstance(value, dict) or part not in value:
            return None
        value = value[part]
    return value


def report(label: str, actual: Any, expected: Any) -> bool:
    ok = actual == expected
    state = "PASS" if ok else "FAIL"
    print(f"[{state}] {label}: actual={actual!r}, expected={expected!r}")
    return ok


def main() -> int:
    if not PROFILE.exists():
        print(f"[FAIL] Vivaldi preferences not found: {PROFILE}", file=sys.stderr)
        return 2

    prefs = load_json(PROFILE)
    failures = 0

    if APP.exists():
        version_file = APP / "Contents/Info.plist"
        with version_file.open("rb") as handle:
            info = plistlib.load(handle)
        print(f"Vivaldi version: {info.get('CFBundleShortVersionString', 'unknown')}")
    else:
        print(f"[WARN] Vivaldi app not found at {APP}")

    checks = [
        ("tab bar is at the top", "vivaldi.tabs.bar.position", 0),
        ("hover-expanded tab rail is off", "vivaldi.tabs.bar.expand_on_hover", False),
        ("panel is on the right", "vivaldi.panels.position", 1),
        ("panel toggle is visible", "vivaldi.panels.show_toggle", True),
        ("interface auto-hide is enabled", "vivaldi.auto_hide.enabled", True),
        ("only the panel slides out", "vivaldi.auto_hide.panel", True),
        ("address bar stays visible", "vivaldi.auto_hide.address_bar", False),
        ("tab bar stays visible", "vivaldi.auto_hide.tab_bar", False),
        ("bookmark single-click is enabled", "vivaldi.bookmarks.single_click_opens", True),
        ("title bar is hidden", "vivaldi.appearance.disable_title_bar", True),
        ("notifications are blocked", "profile.default_content_setting_values.notifications", 2),
        ("Do Not Track request is enabled", "enable_do_not_track", True),
    ]

    for label, path, expected in checks:
        if not report(label, nested(prefs, path), expected):
            failures += 1

    tabbar_before = nested(prefs, "vivaldi.toolbars.tabbar_before") or []
    for control in ("Reload", "Back", "Forward"):
        if not report(f"top toolbar contains {control}", control in tabbar_before, True):
            failures += 1

    themes = nested(prefs, "vivaldi.themes.user") or []
    expected_themes = {
        "雾紫石墨": {
            "colorBg": "#1c1b20",
            "colorFg": "#ecebf2",
            "colorHighlightBg": "#7a6ccb",
            "colorAccentBg": "#9c92e2",
        },
        "青灰绿": {
            "colorBg": "#191d1b",
            "colorFg": "#e7f0eb",
            "colorHighlightBg": "#66a68c",
            "colorAccentBg": "#86bca6",
        },
        "暖纸黄": {
            "colorBg": "#f4efe4",
            "colorFg": "#2d2a25",
            "colorHighlightBg": "#c86e4d",
            "colorAccentBg": "#e5b66e",
        },
    }
    theme_ids = {}
    for name, expected_values in expected_themes.items():
        theme = next((item for item in themes if item.get("name") == name), None)
        if theme is None:
            print(f"[FAIL] custom theme {name} was not found")
            failures += 1
            continue
        theme_ids[name] = theme.get("id")
        for key, expected in expected_values.items():
            if not report(f"{name} {key}", theme.get(key), expected):
                failures += 1
        if not report(f"{name} does not take accent from page", theme.get("accentFromPage"), False):
            failures += 1

    schedule = nested(prefs, "vivaldi.theme.schedule") or {}
    active_dark = schedule.get("o_s", {}).get("dark")
    if not report("system dark mode uses 青灰绿", active_dark, theme_ids.get("青灰绿")):
        failures += 1
    active_light = schedule.get("o_s", {}).get("light")
    if not report("system light mode uses 暖纸黄", active_light, theme_ids.get("暖纸黄")):
        failures += 1

    if LOCAL_STATE.exists():
        local_state = load_json(LOCAL_STATE)
        if not report(
            "hardware acceleration was enabled",
            nested(local_state, "hardware_acceleration_mode_previous"),
            True,
        ):
            failures += 1
    else:
        print(f"[WARN] Vivaldi Local State not found: {LOCAL_STATE}")

    print("[MANUAL] Check startup: 上次会话 + 延迟加载恢复的标签页")
    print("[MANUAL] Check performance: 均衡优化 + hardware acceleration enabled")
    print("[MANUAL] Check privacy: 轻度 blocker + abusive-ad blocking enabled")
    print("[MANUAL] Check permissions: location/camera/microphone = ask")
    print("[MANUAL] Confirm the right panel slides out while the address bar remains fixed")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
