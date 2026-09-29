# Student Performance Analyzer
# Made for intro to programming project

# global list to store all students
students_list = []

def swap_things(a, b):
    # standard way to swap using a temp variable
    temp = a
    a = b
    b = temp
    return a, b

def get_total(my_list):
    # calculate total using a loop
    total = 0
    for num in my_list:
        total = total + num
    return total

def calc_factorial(n):
    # loop to find factorial
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i
    return ans

def get_fibonacci(n):
    fib_list = []
    a = 0
    b = 1
    for i in range(n):
        fib_list.append(a)
        # add the last two numbers
        next_num = a + b
        a = b
        b = next_num
    return fib_list

def reverse_string(text):
    # looping to reverse text
    rev = ""
    for char in text:
        rev = char + rev
    return rev

def convert_to_binary(num):
    if num == 0:
        return "0"
    
    bin_str = ""
    while num > 0:
        rem = num % 2
        bin_str = str(rem) + bin_str
        num = num // 2
    return bin_str

def add_new_student():
    print("\n--- Add Student ---")
    name = input("Student name: ")
    roll = input("Roll number: ")
    
    # no try/except here, just assuming user types a number
    num_subs = int(input("Number of subjects: "))
    
    marks_array = []
    for i in range(num_subs):
        m = int(input("Marks for subject " + str(i+1) + " (0-100): "))
        marks_array.append(m)
        
    # calculate average manually
    total_marks = 0
    for mark in marks_array:
        total_marks = total_marks + mark
        
    avg = total_marks / num_subs
    
    # get grade
    grade = ""
    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 50:
        grade = "D"
    else:
        grade = "F"
    
    # store in dictionary and append to global list
    student_dict = {
        "name": name,
        "roll": roll,
        "marks": marks_array,
        "avg": avg,
        "grade": grade
    }
    students_list.append(student_dict)
    print("Record saved for " + name + ". Grade: " + grade)

def display_all():
    print("\n--- Student Records ---")
    if len(students_list) == 0:
        print("No student records available.")
    else:
        counter = 1
        for s in students_list:
            # manually make a string of marks separated by commas
            marks_str = ""
            for m in s["marks"]:
                marks_str = marks_str + str(m) + " "
                
            print(str(counter) + ". " + s['name'] + " | Roll: " + s['roll'] + " | Marks: " + marks_str + "| Average: " + str(round(s['avg'], 2)) + " | Grade: " + s['grade'])
            counter = counter + 1

def generate_report():
    print("\n--- Class Performance Report ---")
    if len(students_list) == 0:
        print("Add at least one student first.")
        return
        
    # Calculate class average using explicit loop
    sum_avgs = 0
    for s in students_list:
        sum_avgs = sum_avgs + s["avg"]
    class_avg = sum_avgs / len(students_list)
    
    # Find top student without using lambda or max()
    top_student = students_list[0]
    for s in students_list:
        if s["avg"] > top_student["avg"]:
            top_student = s
            
    # Count passed and failed manually
    passed_count = 0
    failed_count = 0
    for s in students_list:
        if s["avg"] >= 50:
            passed_count = passed_count + 1
        else:
            failed_count = failed_count + 1

    print("Total students: " + str(len(students_list)))
    print("Class average: " + str(round(class_avg, 2)))
    print("Highest performer: " + top_student['name'] + " (" + str(round(top_student['avg'], 2)) + ")")
    print("Passed: " + str(passed_count))
    print("Needs improvement: " + str(failed_count))

def search_for_student():
    print("\n--- Search Student ---")
    q = input("Enter name or roll number: ").lower()
    
    found_students = []
    # Loop to search instead of list comprehension
    for s in students_list:
        if q in s["name"].lower() or q == s["roll"].lower():
            found_students.append(s)
            
    if len(found_students) == 0:
        print("No matching student found.")
    else:
        for s in found_students:
            print(s["name"] + " - Roll: " + s["roll"] + " - Avg: " + str(s["avg"]))

def algos():
    print("\n--- Algorithm Toolkit ---")
    print("1. Factorial")
    print("2. Fibonacci sequence")
    print("3. Reverse text")
    print("4. Decimal to binary")
    print("5. Exchange two values")
    print("0. Return to main menu")

    opt = input("Choose an algorithm: ")
    if opt == "1":
        n = int(input("Enter a number: "))
        print("Factorial is:", calc_factorial(n))
    elif opt == "2":
        c = int(input("How many Fibonacci terms? "))
        print(get_fibonacci(c))
    elif opt == "3":
        t = input("Enter text: ")
        print("Reversed:", reverse_string(t))
    elif opt == "4":
        n = int(input("Enter a decimal number: "))
        print("Binary:", convert_to_binary(n))
    elif opt == "5":
        v1 = input("First value: ")
        v2 = input("Second value: ")
        res1, res2 = swap_things(v1, v2)
        print("After exchange: first is " + res1 + ", second is " + res2)
    elif opt == "0":
        pass
    else:
        print("Invalid choice.")

def menu():
    while True:
        print("\n====================================================")
        print("               STUDENT PERFORMANCE ANALYZER")
        print("====================================================")
        print("1. Add student record")
        print("2. View all student records")
        print("3. Generate class performance report")
        print("4. Search for a student")
        print("5. Open algorithm toolkit")
        print("0. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_new_student()
        elif choice == "2":
            display_all()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            search_for_student()
        elif choice == "5":
            algos()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Wrong choice.")

# run the program
menu()