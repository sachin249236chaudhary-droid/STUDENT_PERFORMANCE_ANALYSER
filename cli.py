"""Command-line interface."""
from . import algorithms as algo
from .config import BANNER_PATH, load_settings, resolve
from .service import StudentService
from .storage import export_csv, load_students, save_students


# ---------- input helpers ----------
def read_int(prompt, lo=None, hi=None):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if (lo is not None and value < lo) or (hi is not None and value > hi):
            print(f"Value must be between {lo} and {hi}.")
            continue
        return value


def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def banner():
    try:
        print("\n" + BANNER_PATH.read_text(encoding="utf-8").rstrip())
    except OSError:
        print("\n=== STUDENT PERFORMANCE ANALYZER ===")


# ---------- app ----------
class App:
    def __init__(self):
        self.settings = load_settings()
        self.data_path = resolve(self.settings["data_file"])
        self.thresholds = self.settings["grade_thresholds"]
        self.max_marks = self.settings["max_marks"]
        self.service = StudentService(load_students(self.data_path),
                                      self.settings["pass_mark"])

    def save(self):
        save_students(self.service.students, self.data_path)

    # --- student actions ---
    def add_student(self):
        print("\n--- Add Student ---")
        name = read_text("Student name: ")
        roll = read_text("Roll number: ")
        if self.service.roll_exists(roll):
            print("A student with that roll number already exists.")
            return
        n = read_int("Number of subjects: ", 1, 50)
        marks = [read_int(f"Marks for subject {i + 1} (0-{self.max_marks}): ",
                          0, self.max_marks) for i in range(n)]
        s = self.service.add(name, roll, marks)
        self.save()
        print(f"Record saved for {name}. Grade: {s.grade(self.thresholds)}")

    def view_all(self):
        print("\n--- Student Records ---")
        if not self.service.students:
            print("No student records available.")
            return
        for i, s in enumerate(self.service.students, 1):
            print(f"{i}. {s.name} | Roll: {s.roll} | Marks: {' '.join(map(str, s.marks))} "
                  f"| Average: {s.average:.2f} | Grade: {s.grade(self.thresholds)}")

    def report(self):
        print("\n--- Class Performance Report ---")
        r = self.service.report()
        if r is None:
            print("Add at least one student first.")
            return
        print(f"Total students: {r['total']}")
        print(f"Class average: {r['class_average']:.2f}")
        print(f"Highest performer: {r['top'].name} ({r['top'].average:.2f})")
        print(f"Passed: {r['passed']}")
        print(f"Needs improvement: {r['failed']}")

    def search(self):
        print("\n--- Search Student ---")
        found = self.service.search(read_text("Enter name or roll number: "))
        if not found:
            print("No matching student found.")
        for s in found:
            print(f"{s.name} - Roll: {s.roll} - Avg: {s.average:.2f}")

    def remove(self):
        print("\n--- Remove Student ---")
        if self.service.remove(read_text("Roll number to remove: ")):
            self.save()
            print("Record removed.")
        else:
            print("No student with that roll number.")

    def export(self):
        if not self.service.students:
            print("Nothing to export.")
            return
        out = export_csv(self.service.students,
                         resolve(self.settings["export_dir"]), self.thresholds)
        print(f"Exported to {out}")

    # --- toolkit ---
    def toolkit(self):
        print("\n--- Algorithm Toolkit ---")
        print("1. Factorial\n2. Fibonacci sequence\n3. Reverse text\n"
              "4. Decimal to binary\n5. Exchange two values\n0. Return to main menu")
        opt = input("Choose an algorithm: ").strip()
        try:
            if opt == "1":
                print("Factorial is:", algo.factorial(read_int("Enter a number: ", 0)))
            elif opt == "2":
                print(algo.fibonacci(read_int("How many Fibonacci terms? ", 0)))
            elif opt == "3":
                print("Reversed:", algo.reverse_string(input("Enter text: ")))
            elif opt == "4":
                print("Binary:", algo.to_binary(read_int("Enter a decimal number: ", 0)))
            elif opt == "5":
                a, b = algo.swap(input("First value: "), input("Second value: "))
                print(f"After exchange: first is {a}, second is {b}")
            elif opt != "0":
                print("Invalid choice.")
        except ValueError as e:
            print("Error:", e)

    # --- main loop ---
    def run(self):
        actions = {
            "1": self.add_student, "2": self.view_all, "3": self.report,
            "4": self.search, "5": self.toolkit, "6": self.remove, "7": self.export,
        }
        while True:
            banner()
            print("1. Add student record\n2. View all student records\n"
                  "3. Generate class performance report\n4. Search for a student\n"
                  "5. Open algorithm toolkit\n6. Remove a student\n"
                  "7. Export records to CSV\n0. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "0":
                print("Bye!")
                break
            actions.get(choice, lambda: print("Wrong choice."))()


def main():
    try:
        App().run()
    except (KeyboardInterrupt, EOFError):
        print("\nBye!")
