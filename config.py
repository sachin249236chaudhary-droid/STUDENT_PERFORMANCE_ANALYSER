"""Loads application settings from config/settings.json."""
import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SETTINGS_PATH = ROOT_DIR / "config" / "settings.json"
BANNER_PATH = ROOT_DIR / "assets" / "banner.txt"

DEFAULTS = {
    "data_file": "data/students.json",
    "export_dir": "data/exports",
    "max_marks": 100,
    "pass_mark": 50,
    "grade_thresholds": [
        {"min": 90, "grade": "A+"}, {"min": 80, "grade": "A"},
        {"min": 70, "grade": "B"}, {"min": 60, "grade": "C"},
        {"min": 50, "grade": "D"}, {"min": 0, "grade": "F"},
    ],
}


def load_settings(path=SETTINGS_PATH):
    """Return settings merged over defaults; falls back to defaults if missing/corrupt."""
    settings = dict(DEFAULTS)
    try:
        with open(path, encoding="utf-8") as f:
            settings.update(json.load(f))
    except (OSError, json.JSONDecodeError):
        pass
    settings["grade_thresholds"] = sorted(
        settings["grade_thresholds"], key=lambda t: t["min"], reverse=True
    )
    return settings


def resolve(relative_path):
    """Resolve a settings path relative to the project root."""
    p = Path(relative_path)
    return p if p.is_absolute() else ROOT_DIR / p
