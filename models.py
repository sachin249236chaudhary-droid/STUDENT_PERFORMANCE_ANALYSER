"""Data model for a student."""
from dataclasses import dataclass, field
from typing import List

from .grading import calculate_grade


@dataclass
class Student:
    name: str
    roll: str
    marks: List[float] = field(default_factory=list)

    @property
    def average(self) -> float:
        return sum(self.marks) / len(self.marks) if self.marks else 0.0

    def grade(self, thresholds) -> str:
        return calculate_grade(self.average, thresholds)

    def to_dict(self) -> dict:
        return {"name": self.name, "roll": self.roll, "marks": self.marks}

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        return cls(str(data["name"]), str(data["roll"]), list(data.get("marks", [])))
