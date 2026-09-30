"""Persistence: JSON load/save and CSV export."""
import csv
import json
from datetime import datetime
from pathlib import Path
from typing import List

from .models import Student


def load_students(path) -> List[Student]:
    path = Path(path)
    if not path.exists():
        return []
    try:
        with open(path, encoding="utf-8") as f:
            return [Student.from_dict(d) for d in json.load(f)]
    except (json.JSONDecodeError, KeyError, TypeError):
        print(f"Warning: could not read {path}; starting with an empty list.")
        return []


def save_students(students: List[Student], path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump([s.to_dict() for s in students], f, indent=2)


def export_csv(students: List[Student], export_dir, thresholds) -> Path:
    export_dir = Path(export_dir)
    export_dir.mkdir(parents=True, exist_ok=True)
    out = export_dir / f"students_{datetime.now():%Y%m%d_%H%M%S}.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Name", "Roll", "Marks", "Average", "Grade"])
        for s in students:
            w.writerow([s.name, s.roll, " ".join(map(str, s.marks)),
                        round(s.average, 2), s.grade(thresholds)])
    return out
