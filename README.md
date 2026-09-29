# Student Performance Analyzer

A menu-driven, command-line Python program for recording student marks, calculating grades, and generating a class performance report. It also includes a small toolkit of classic beginner algorithms (factorial, Fibonacci, string reversal, decimal-to-binary, and value swapping).

Built as an introductory programming project. It uses only core Python: loops, conditionals, functions, lists, and dictionaries. No external libraries are required.

## Features

### Student management
- **Add student record**: enter a name, roll number, and marks for any number of subjects. The average and grade are calculated automatically.
- **View all records**: list every student with their marks, average, and grade.
- **Class performance report**: shows total students, class average, top performer, and pass/fail counts.
- **Search**: find students by partial name or exact roll number (case-insensitive).

### Algorithm toolkit
| Option | Description |
| ------ | ----------- |
| Factorial | Computes `n!` using a loop |
| Fibonacci sequence | Prints the first `n` Fibonacci numbers |
| Reverse text | Reverses a string character by character |
| Decimal to binary | Converts a non-negative integer to binary |
| Exchange two values | Swaps two values using a temporary variable |

## Requirements

- Python 3.6 or newer

## How to Run

1. Save the code as a `.py` file, for example `student_analyzer.py`.
2. Open a terminal in the same folder.
3. Run:

```bash
python student_analyzer.py
```

(On some systems, use `python3` instead of `python`.)

## Usage

When the program starts, you will see the main menu:

```
====================================================
               STUDENT PERFORMANCE ANALYZER
====================================================
1. Add student record
2. View all student records
3. Generate class performance report
4. Search for a student
5. Open algorithm toolkit
0. Exit
```

Type the number of the option you want and press Enter.

### Example session

```
Choose an option: 1

--- Add Student ---
Student name: Asha
Roll number: 101
Number of subjects: 3
Marks for subject 1 (0-100): 88
Marks for subject 2 (0-100): 92
Marks for subject 3 (0-100): 79
Record saved for Asha. Grade: A
```

## Grading Scale

The grade is based on the student's average marks.

| Average | Grade |
| ------- | ----- |
| 90 and above | A+ |
| 80 – 89.99 | A |
| 70 – 79.99 | B |
| 60 – 69.99 | C |
| 50 – 59.99 | D |
| Below 50 | F |

A student with an average of **50 or above** is counted as *passed* in the class report.

## Project Structure

The project is a single file organised into these functions:

| Function | Purpose |
| -------- | ------- |
| `add_new_student()` | Collects input, calculates average and grade, stores the record |
| `display_all()` | Prints all stored student records |
| `generate_report()` | Prints class-level statistics |
| `search_for_student()` | Searches by name or roll number |
| `algos()` | Sub-menu for the algorithm toolkit |
| `calc_factorial(n)` | Factorial of `n` |
| `get_fibonacci(n)` | List of the first `n` Fibonacci numbers |
| `reverse_string(text)` | Reversed copy of a string |
| `convert_to_binary(num)` | Binary representation of an integer |
| `swap_things(a, b)` | Returns the two values swapped |
| `get_total(my_list)` | Sum of a list of numbers |
| `menu()` | Main program loop |

Student records are stored in a global list called `students_list`, where each student is a dictionary:

```python
{
    "name": "Asha",
    "roll": "101",
    "marks": [88, 92, 79],
    "avg": 86.33,
    "grade": "A"
}
```

## Known Limitations

- **In-memory storage only**: all records are lost when the program exits.
- **Limited input validation**: entering text where a number is expected (for example, in the number of subjects or marks) will crash the program. Marks are also not checked to be within 0–100.
- **Zero subjects**: entering `0` for the number of subjects causes a division-by-zero error.
- **Negative numbers** in the factorial and binary options are not handled.
- Duplicate roll numbers are not prevented.

## Possible Improvements

- Add `try/except` blocks and range checks for all user input.
- Save and load records from a file (CSV or JSON) so data persists between runs.
- Add options to edit or delete a student.
- Sort students by average or name.
- Prevent duplicate roll numbers.

## License

This project was created for educational purposes. Feel free to use and modify it for learning.
