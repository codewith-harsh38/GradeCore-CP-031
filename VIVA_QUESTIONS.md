# GradeCore – Capstone Viva Preparation

## 20 Likely Viva Questions with Beginner-Friendly Answers

Based on the actual GradeCore CP-031 implementation

---

### Python Fundamentals

#### Q1: Why did you choose Python for this capstone project?

**A:** Python was chosen because it's beginner-friendly, has clear syntax, and is excellent for learning fundamental programming concepts like lists, dictionaries, functions, and conditional statements. It's also widely used in educational settings and doesn't require complex setup — just the Python 3 standard library, which makes it ideal for a foundation-level capstone project.

#### Q2: Explain the role of `import sys` in your application.

**A:** The `import sys` statement brings the `sys` module into the program, which provides system-specific functions. In GradeCore, it's used primarily for `sys.exit(0)` in the main menu option 7 (Exit Application) to terminate the application cleanly when the user chooses to exit.

---

### Functions

#### Q3: How many functions did you define in gradecore.py, and what are their purposes?

**A:** I defined 12 functions in gradecore.py:

1. `get_valid_name()` – Prompts for student name, rejects empty input
2. `get_valid_marks()` – Prompts for marks in 5 subjects with full validation
3. `student_id_exists()` – Checks if a student ID already exists in records
4. `register_student()` – Adds a new student with all validation
5. `calculate_results()` – Computes total, percentage, and grade for a student
6. `validate_all_results()` – Ensures all students have results calculated
7. `check_pass_fail()` – Determines subject-wise and overall pass/fail status
8. `rank_students()` – Ranks students by percentage using competition ranking
9. `get_student_rank()` – Gets rank of a specific student by ID
10. `generate_report_card()` – Generates formatted report card for a student
11. `find_subject_toppers()` – Finds highest scorer in each subject
12. `display_subject_toppers()` – Displays subject toppers in formatted output
13. `main_menu()` – Displays menu and handles user choices

#### Q4: How do you pass data between functions in your application?

**A:** Data is passed through function parameters and return values. The main data structure is the `students` list, which is passed by reference to most functions. For example:

- `register_student(students)` appends a new student dict to the list
- `calculate_results(student)` modifies a student dict in-place by adding total, percentage, and grade
- `rank_students(students)` takes the list, returns a sorted copy with ranks assigned
- `generate_report_card(students, student_id)` finds a specific student and generates their report

Global constants like `SUBJECTS`, `MIN_MARK`, `MAX_MARK`, and `GRADING_TABLE` are defined at module level and accessible to all functions.

#### Q5: What is the purpose of the `return` statement in your functions?

**A:** The `return` statement sends a value back to the caller. Different functions use return differently:

- `get_valid_name()` returns the validated name string
- `get_valid_marks()` returns a dictionary of subject-mark pairs
- `student_id_exists()` returns True/False (boolean)
- `rank_students()` returns a sorted list of student dicts with ranks
- `find_subject_toppers()` returns a dictionary of subject → (names list, mark)
- `check_pass_fail()` returns subject status dictionary and updates student overall_result

Functions that don't need to return a value (like `register_student()` displaying success messages) implicitly return `None`.

---

### Lists and Dictionaries

#### Q6: What Python data structures did you use to store student records, and why?

**A:** I used a **list of dictionaries** to store student records. Each student is a dictionary with keys like `"student_id"`, `"full_name"`, `"marks"` (another dictionary), `"total"`, `"percentage"`, `"grade"`, and `"overall_result"`. The list allows multiple students, and dictionaries provide key-value access for clear, readable data retrieval.

**Example student record:**
```python
{
    "student_id": "S001",
    "full_name": "Alice Johnson",
    "marks": {"Mathematics": 85, "Physics": 78, "Chemistry": 92, "English": 67, "Computer Science": 80},
    "total": 402,
    "percentage": 80.40,
    "grade": "A",
    "overall_result": "PASS"
}
```

#### Q7: How does the `marks` dictionary work within a student record?

**A:** The `marks` dictionary within each student record maps subject names to the marks obtained. The keys are the five subject names from the `SUBJECTS` constant list, and the values are integer marks between 0 and 100. This structure allows easy iteration, lookup, and calculation:

```python
for subject in SUBJECTS:
    mark = student["marks"][subject]
    # Calculate total: sum(student["marks"].values())
    # Check pass/fail: mark >= MIN_PASS_MARK
```

#### Q8: Explain the sorting you used in the ranking system.

**A:** I used Python's built-in `sorted()` function with a `key` parameter:

```python
sorted_students = sorted(students, key=lambda s: s["percentage"], reverse=True)
```

This sorts the students by their `percentage` field in descending order (`reverse=True`). The original student records are not modified because `sorted()` returns a new list, leaving the original `students` list unchanged.

#### Q9: How do you handle students with identical percentages in ranking?

**A:** The `rank_students()` function implements competition ranking (1, 2, 2, 4):

1. After sorting by percentage, it iterates through the sorted list
2. It counts how many students share the same percentage (tie count)
3. All tied students receive the same rank
4. The next rank advances by the tie count (e.g., if two students tie at rank 1, the next student gets rank 3)

This is implemented with a `while` loop that counts ties and adjusts the rank counter accordingly.

#### Q10: Why did you use a dictionary for marks instead of separate variables?

**A:** Using a dictionary for marks provides several advantages:

- **Scalability:** Easy to handle exactly 5 subjects without declaring 5 separate variables
- **Iteration:** Can loop through subjects with `for subject in SUBJECTS`
- **Dynamic access:** Marks can be looked up by subject name
- **Validation:** Can validate each mark in a loop within `get_valid_marks()`
- **Ranking:** Can sort/compare percentages across all subjects easily
- **Report generation:** Can generate subject tables dynamically

---

### Input Validation

#### Q11: How does mark validation work in your application?

**A:** The `get_valid_marks()` function validates marks through multiple checks in sequence:

1. **Alphabetic rejection:** `if raw.isalpha()` – rejects inputs like "abc"
2. **Empty input rejection:** `if not raw` – rejects empty strings
3. **Numeric conversion:** `try: mark = int(raw)` – attempts integer conversion
4. **ValueError handling:** `except ValueError` – catches non-numeric input
5. **Range check (lower):** `if mark < MIN_MARK` – rejects negative marks
6. **Range check (upper):** `if mark > MAX_MARK` – rejects marks above 100

If any check fails, an error message is displayed and the user is prompted to re-enter the mark for that subject. This loop continues until valid input is provided for all 5 subjects.

#### Q12: How do you validate student names?

**A:** The `get_valid_name()` function validates names:

```python
name = input("Enter student full name: ").strip()
if not name:
    print("❌ Error: Student name cannot be empty. Please try again.")
    continue
return name
```

The `.strip()` removes leading/trailing whitespace, and `if not name` checks for empty string. If the name is empty, an error message is displayed and the user is prompted again. The function uses a `while True` loop that continues until a valid non-empty name is entered.

#### Q13: How do you prevent duplicate student IDs?

**A:** The `student_id_exists()` function checks for duplicates:

```python
def student_id_exists(student_id, students):
    for s in students:
        if s["student_id"] == student_id:
            return True
    return False
```

In `register_student()`, before adding a new student:

```python
if student_id_exists(sid, students):
    print(f"❌ Error: Student ID '{sid}' already exists. Please use a unique ID.")
    continue
```

If the ID already exists, an error is displayed and the user must enter a different ID. This loop continues until a unique ID is provided.

#### Q14: How does the application handle invalid menu selections?

**A:** In the `main_menu()` function, the choice is validated:

```python
choice = input("\nEnter your choice (1-7): ").strip()

if choice == "1":
    # Add New Student
elif choice == "2":
    # View All Students
elif choice == "3":
    # Calculate Student Results
elif choice == "4":
    # Display Student Rankings
elif choice == "5":
    # Generate Student Report Card
elif choice == "6":
    # Display Subject Toppers
elif choice == "7":
    # Exit Application
else:
    print("❌ Invalid choice. Please enter a number between 1 and 7.")
```

Any choice outside "1" through "7" triggers the error message, and the menu loop continues.

---

### Percentage Calculations

#### Q15: How is the percentage calculated in GradeCore?

**A:** The percentage is calculated in the `calculate_results()` function:

```python
def calculate_results(student):
    marks = student["marks"]
    total = sum(marks.values())  # Sum of all 5 subject marks
    percentage = total / 5  # Out of 500 (5 subjects × 100)
    ...
```

**Example:** If a student scores 85, 78, 92, 67, 80:
- Total = 85 + 78 + 92 + 67 + 80 = 402
- Percentage = 402 / 5 = 80.40%

The result is stored with 2 decimal places: `student["percentage"] = round(percentage, 2)`.

#### Q16: What are the grading boundaries used?

**A:** The grading boundaries are defined in the `GRADING_TABLE` constant:

```python
GRADING_TABLE = [
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (0, "F"),
]
```

The grade assignment loop:

```python
grade = "F"
for threshold, gr in GRADING_TABLE:
    if percentage >= threshold:
        grade = gr
        break
```

This means:
- 90–100 → A+ (first threshold met is 90)
- 80–89.99 → A (meets 80 but not 90)
- 70–79.99 → B
- 60–69.99 → C
- 50–59.99 → D
- Below 50 → F

#### Q17: Why do you round the percentage to 2 decimal places?

**A:** The percentage is rounded to 2 decimal places for consistent display and to match the specification: "Display percentages up to two decimal places." This ensures that percentages like 80.4 are shown as 80.40, and provides precision without excessive decimal places. The `round(percentage, 2)` function handles this.

#### Q18: How does the application handle the total out of 500?

**A:** The total is calculated as the sum of all 5 subject marks (each out of 100), so the maximum possible total is 500. This is implicit – the application doesn't store a "maximum total" variable; it's understood that 5 subjects × 100 marks each = 500 total. The report card explicitly shows "Total Marks: X / 500".

---

### Grade Assignment

#### Q19: Explain how grade assignment works with the boundary conditions.

**A:** Grade assignment uses threshold comparison from highest to lowest:

```python
grade = "F"  # Default grade
for threshold, gr in GRADING_TABLE:
    if percentage >= threshold:
        grade = gr
        break
```

The `break` statement ensures only the first (highest) matching threshold is used. The GRADING_TABLE is ordered from highest to lowest:

- If percentage >= 90 → A+ (highest threshold)
- If percentage >= 80 but < 90 → A
- If percentage >= 70 but < 80 → B
- If percentage >= 60 but < 70 → C
- If percentage >= 50 but < 60 → D
- If percentage < 50 → F (default, since no threshold matches)

**Edge case examples:**
- 89.99% → Grade A (meets 80, but not 90)
- 90.00% → Grade A+ (meets 90)
- 75.50% → Grade B (meets 70, but not 80)
- 50.00% → Grade D (meets 50, but not 60)
- 49.99% → Grade F (doesn't meet 50)

#### Q20: How are the pass/fail status and academic grade kept separate?

**A:** The application maintains two separate concepts:

1. **Academic Grade** – Assigned based on percentage using GRADING_TABLE (A+, A, B, C, D, F)
2. **Overall Result** – PASS/FAIL based on subject-wise minimum passing mark (35)

In `calculate_results()`:
```python
student["overall_result"] = "PASS"  # temporary; corrected in Feature 3
```

In `check_pass_fail()`:
```python
student["overall_result"] = "PASS" if all_pass else "FAIL"
```

**Example:** A student with 85% overall but Chemistry mark = 25:
- Grade = B (based on 85% overall)
- Overall Result = FAIL (because one subject fails the minimum 35 mark requirement)

This separation is explicitly documented in the code and tested in the test suite.