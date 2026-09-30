"""Business logic: managing students, searching and reporting."""
from typing import List, Optional

from .models import Student


class StudentService:
    def __init__(self, students: Optional[List[Student]] = None, pass_mark=50):
        self.students = students if students is not None else []
        self.pass_mark = pass_mark

    def add(self, name, roll, marks) -> Student:
        student = Student(name, roll, marks)
        self.students.append(student)
        return student

    def roll_exists(self, roll) -> bool:
        return any(s.roll.lower() == roll.lower() for s in self.students)

    def remove(self, roll) -> bool:
        for s in self.students:
            if s.roll.lower() == roll.lower():
                self.students.remove(s)
                return True
        return False

    def search(self, query) -> List[Student]:
        q = query.lower()
        return [s for s in self.students if q in s.name.lower() or q == s.roll.lower()]

    def ranked(self) -> List[Student]:
        return sorted(self.students, key=lambda s: s.average, reverse=True)

    def report(self) -> Optional[dict]:
        if not self.students:
            return None
        avgs = [s.average for s in self.students]
        passed = sum(1 for a in avgs if a >= self.pass_mark)
        return {
            "total": len(self.students),
            "class_average": sum(avgs) / len(avgs),
            "top": max(self.students, key=lambda s: s.average),
            "passed": passed,
            "failed": len(avgs) - passed,
        }
