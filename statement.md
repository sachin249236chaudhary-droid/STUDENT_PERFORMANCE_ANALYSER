# Student Performance Analyzer

## 1. Problem Statement

Teachers and students in small classes often track marks on paper or in loose
spreadsheets. Calculating averages, assigning grades, finding the top performer,
and counting who passed or failed by hand is slow and error-prone, and the
results are lost or inconsistent from one session to the next.

The **Student Performance Analyzer** solves this by providing a simple
command-line program where marks are entered once, and the averages, grades, and
class-level statistics are calculated automatically and saved for later use.

## 2. Scope of the Project

### In scope
- Entering student records: name, roll number, and marks for any number of subjects.
- Automatic calculation of each student's average and letter grade (A+ to F).
- Viewing all saved records and searching by name or roll number.
- Generating a class performance report (class average, top performer,
  pass/fail counts, grade distribution).
- Saving records to a local JSON file so data persists between runs.
- Configurable grade boundaries, pass mark, and maximum marks via `config.json`.
- Input validation (marks in range, numeric input, no duplicate roll numbers).
- A small algorithm toolkit (factorial, Fibonacci, string reversal,
  decimal-to-binary, value swap) that demonstrates core programming concepts.
- CSV export of records and unit tests for the core logic.

### Out of scope
- Graphical or web interface.
- Multi-user accounts, login, or network/database storage.
- Editing or deleting existing records (planned as a future enhancement).
- Subject-wise names, weightings, or attendance tracking.
- Charts and advanced statistical analysis.

## 3. Target Users

| User | How they benefit |
|------|------------------|
| **Teachers / tutors** | Quickly grade a class and see who needs extra help without manual calculation. |
| **Students** | Check their own average and grade and compare with class performance. |
| **Programming beginners** | A readable, modular example of loops, functions, dictionaries, file handling, and testing in Python. |
| **Small institutes / coaching classes** | A lightweight tool that needs no installation beyond Python. |

## 4. High-Level Features

1. **Add student record** – Enter name, roll number, and subject marks with validation.
2. **Automatic grading** – Average and grade computed from configurable boundaries.
3. **View all records** – Numbered list showing marks, average, and grade.
4. **Search** – Find students by partial name or exact roll number.
5. **Class performance report** – Total students, class average, highest performer,
   passed vs. needs improvement, and a grade distribution bar summary.
6. **Persistent storage** – Records saved to and loaded from `data/students.json`.
7. **Configuration file** – Change grading rules and pass mark without editing code.
8. **Algorithm toolkit** – Factorial, Fibonacci sequence, text reversal,
   decimal-to-binary conversion, and value exchange.
9. **CSV export script** – Produce a spreadsheet-friendly file of all records.
10. **Automated tests** – Unit tests covering grading, search, reports, and algorithms.
