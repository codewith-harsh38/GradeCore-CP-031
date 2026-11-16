#!/usr/bin/env python3
"""
GradeCore – Academic Result Processing and Ranking Engine
CP-031 Capstone Project
Foundation Level · Python 3 · Console Application
"""

import sys

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SUBJECTS = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "English",
    "Computer Science",
]

MIN_MARK = 0
MAX_MARK = 100
MIN_PASS_MARK = 35

GRADING_TABLE = [
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (0, "F"),
]

MENU_OPTIONS = [
    "Add New Student",
    "View All Students",
    "Calculate Student Results",
    "Display Student Rankings",
    "Generate Student Report Card",
    "Display Subject Toppers",
    "Exit Application",
]


# ---------------------------------------------------------------------------
# Student Registration & Mark Entry
# ---------------------------------------------------------------------------
def get_valid_name():
    """Prompt for student name, reject empty input."""
    while True:
        name = input("Enter student full name: ").strip()
        if not name:
            print("❌ Error: Student name cannot be empty. Please try again.")
            continue
        return name


def get_valid_marks():
    """Prompt for marks in 5 subjects with full validation."""
    marks = {}
    for subject in SUBJECTS:
        while True:
            raw = input(f"  Enter marks for {subject} ({MIN_MARK}-{MAX_MARK}): ").strip()
            # Reject alphabetic input
            if raw.isalpha():
                print(f"   ❌ Error: '{raw}' is alphabetic. Marks must be numeric.")
                continue
            # Reject empty
            if not raw:
                print("   ❌ Error: Input cannot be empty. Please enter a number.")
                continue
            try:
                mark = int(raw)
            except ValueError:
                print(f"   ❌ Error: '{raw}' is not a valid number. Please enter 0-100.")
                continue
            # Range check
            if mark < MIN_MARK:
                print(f"   ❌ Error: Marks cannot be negative. Minimum is {MIN_MARK}.")
                continue
            if mark > MAX_MARK:
                print(f"   ❌ Error: Marks cannot exceed {MAX_MARK}. Please re-enter.")
                continue
            marks[subject] = mark
            break
    return marks


def student_id_exists(student_id, students):
    """Check if a student ID already exists in the records."""
    for s in students:
        if s["student_id"] == student_id:
            return True
    return False


def register_student(students):
    """Add a new student with validation."""
    print("\n--- Add New Student ---")

    # Student ID with duplicate check
    while True:
        sid = input("Enter student ID (e.g., S001): ").strip()
        if not sid:
            print("❌ Error: Student ID cannot be empty. Please try again.")
            continue
        if student_id_exists(sid, students):
            print(f"❌ Error: Student ID '{sid}' already exists. Please use a unique ID.")
            continue
        break

    name = get_valid_name()
    marks = get_valid_marks()

    student = {
        "student_id": sid,
        "full_name": name,
        "marks": marks,
        "total": 0,      # will be calculated
        "percentage": 0.0,  # will be calculated
        "grade": "",     # will be calculated
        "overall_result": "",  # will be calculated
    }
    # Calculate results immediately after registration (Issue 1 fix)
    calculate_results(student)
    students.append(student)
    print(f"✅ Student '{name}' (ID: {sid}) registered successfully!\n")
    return student


# ---------------------------------------------------------------------------
# Feature 2: Result Calculation
# ---------------------------------------------------------------------------
def calculate_results(student):
    """Calculate total, percentage, and grade for a student."""
    marks = student["marks"]
    total = sum(marks.values())
    percentage = total / 5  # out of 500, so 5 subjects

    # Grade assignment based on boundaries
    grade = "F"
    for threshold, gr in GRADING_TABLE:
        if percentage >= threshold:
            grade = gr
            break

    student["total"] = total
    student["percentage"] = round(percentage, 2)
    student["grade"] = grade

    # Overall pass/fail will be set by Feature 3 logic
    student["overall_result"] = "PASS"  # temporary; corrected in Feature 3


def validate_all_results(students):
    """Ensure all students have results calculated; recalculate if needed."""
    for s in students:
        # Only recalculate if total is 0 and marks exist (i.e., not yet calculated)
        # or if percentage is 0. Skip if already calculated with real values.
        total = s.get("total", 0)
        percentage = s.get("percentage", 0)
        if total == 0 and percentage == 0 and s.get("marks"):
            calculate_results(s)


# ---------------------------------------------------------------------------
# Feature 3: Subject-wise Pass/Fail
# ---------------------------------------------------------------------------
def check_pass_fail(student):
    """Determine subject-wise and overall pass/fail status."""
    marks = student["marks"]
    subject_status = {}

    all_pass = True
    for subject, mark in marks.items():
        if mark >= MIN_PASS_MARK:
            subject_status[subject] = "PASS"
        else:
            subject_status[subject] = "FAIL"
            all_pass = False

    student["overall_result"] = "PASS" if all_pass else "FAIL"
    return subject_status


# ---------------------------------------------------------------------------
# Feature 4: Student Ranking System (competition ranking)
# ---------------------------------------------------------------------------
def rank_students(students):
    """Rank students by percentage using competition ranking (1, 2, 2, 4)."""
    if not students:
        return []

    # Validate results for all students first
    validate_all_results(students)

    # Create a sorted copy; do NOT modify original records
    sorted_students = sorted(students, key=lambda s: s["percentage"], reverse=True)

    rank = 1
    i = 0
    while i < len(sorted_students):
        current_percentage = sorted_students[i]["percentage"]
        # Count how many students share this percentage
        tie_count = 1
        j = i + 1
        while j < len(sorted_students) and sorted_students[j]["percentage"] == current_percentage:
            tie_count += 1
            j += 1

        # Assign the same rank to all tied students
        for k in range(i, i + tie_count):
            sorted_students[k]["rank"] = rank

        # Next rank advances by tie_count (competition ranking)
        rank += tie_count
        i = j

    return sorted_students


def get_student_rank(students, student_id):
    """Get the rank of a specific student by ID."""
    ranked = rank_students(students)
    for s in ranked:
        if s["student_id"] == student_id:
            return s["rank"]
    return None


# ---------------------------------------------------------------------------
# Feature 5: Report Card & Subject Toppers
# ---------------------------------------------------------------------------
def generate_report_card(students, student_id):
    """Generate a formatted report card for a given student ID."""
    # Find the student
    target = None
    for s in students:
        if s["student_id"] == student_id:
            target = s
            break

    if target is None:
        print(f"❌ Error: No student found with ID '{student_id}'.\n")
        return

    # Ensure results are calculated
    calculate_results(target)
    check_pass_fail(target)

    # Get rank from ranking function (doesn't modify original data)
    ranked = rank_students(students)
    rank_val = None
    for s in ranked:
        if s["student_id"] == student_id:
            rank_val = s.get("rank", "—")
            break

    # Subject status
    subject_status = check_pass_fail(target)

    # Heading
    lines = []
    lines.append("=" * 50)
    lines.append("              GRADECORE – REPORT CARD")
    lines.append("=" * 50)
    lines.append("")
    lines.append(f"Student ID:   {target['student_id']}")
    lines.append(f"Student Name: {target['full_name']}")
    lines.append("")

    # Subject table
    lines.append("    Subject       Marks   Status")
    lines.append("    " + "-" * 35)
    for subject in SUBJECTS:
        mark = target["marks"][subject]
        status = subject_status.get(subject, "—")
        lines.append(f"    {subject:<15} {mark:>3}     {status}")
    lines.append("    " + "-" * 35)

    # Totals and performance
    lines.append("")
    lines.append(f"    Total Marks:      {target['total']} / 500")
    lines.append(f"    Percentage:       {target['percentage']:.2f}%")
    lines.append(f"    Grade:             {target['grade']}")
    lines.append(f"    Overall Result:   {target['overall_result']}")
    lines.append(f"    Student Rank:     {rank_val}")
    lines.append("")

    # Footer
    lines.append("=" * 50)
    lines.append("      Thank you for using GradeCore!")
    lines.append("=" * 50)

    # Display
    for line in lines:
        print(line)

    print()


def find_subject_toppers(students):
    """Find the highest scorer(s) in each subject. Returns dict of subject -> list of (name, mark)."""
    if not students:
        return {}

    # Validate results
    validate_all_results(students)

    toppers = {}
    for subject in SUBJECTS:
        # Get all marks for this subject
        subject_marks = [(s["full_name"], s["marks"][subject]) for s in students]
        # Find the maximum mark
        max_mark = max(mark for _, mark in subject_marks)
        # Find all students with that max mark
        top_names = [name for name, mark in subject_marks if mark == max_mark]
        toppers[subject] = (top_names, max_mark)
    return toppers


def display_subject_toppers(students):
    """Display subject toppers in a formatted way."""
    toppers = find_subject_toppers(students)

    if not toppers:
        print("⚠️  No students registered yet.\n")
        return

    lines = []
    lines.append("=" * 50)
    lines.append("          GRADECORE – SUBJECT TOPPERS")
    lines.append("=" * 50)
    lines.append("")

    for subject, (names, mark) in toppers.items():
        if len(names) == 1:
            lines.append(f"  {subject}: {names[0]} — {mark}")
        else:
            names_str = " & ".join(names)
            lines.append(f"  {subject}: {names_str} — {mark} (tied)")
        lines.append("")

    lines.append("=" * 50)
    for line in lines:
        print(line)

    print()


# ---------------------------------------------------------------------------
# Main Menu System
# ---------------------------------------------------------------------------
def main_menu():
    """Display main menu and handle user choices."""
    students = []  # in-memory student records

    while True:
        print("\n" + "=" * 40)
        print("         GRADECORE – MAIN MENU")
        print("=" * 40)
        for i, option in enumerate(MENU_OPTIONS, 1):
            print(f"  {i}. {option}")
        print("=" * 40)

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            # Add New Student
            register_student(students)

        elif choice == "2":
            # View All Students
            if not students:
                print("⚠️  No students registered yet.\n")
                continue
            print(f"\n{'Student ID':<12} {'Name':<20} {'Percentage':>10}")
            print("-" * 48)
            for s in students:
                print(f"{s['student_id']:<12} {s['full_name']:<20} {s['percentage']:>9.2f}%")
            print()

        elif choice == "3":
            # Calculate Student Results
            if not students:
                print("⚠️  No students registered yet.\n")
                continue
            # Ensure all have results calculated
            for s in students:
                if s["total"] == 0:
                    calculate_results(s)
                    check_pass_fail(s)
            print("✅ Results calculated for all students.\n")

        elif choice == "4":
            # Display Student Rankings
            if not students:
                print("⚠️  No students registered yet.\n")
                continue
            ranked = rank_students(students)
            if not ranked:
                print("⚠️  No data to rank.\n")
                continue
            print(f"\n{'Rank':>6} {'Student ID':<12} {'Name':<20} {'Percentage':>10}")
            print("-" * 52)
            for s in ranked:
                print(f"{s['rank']:>6} {s['student_id']:<12} {s['full_name']:<20} {s['percentage']:>9.2f}%")
            print()

        elif choice == "5":
            # Generate Student Report Card
            if not students:
                print("⚠️  No students registered yet.\n")
                continue
            sid = input("Enter student ID to generate report card: ").strip()
            generate_report_card(students, sid)

        elif choice == "6":
            # Display Subject Toppers
            display_subject_toppers(students)

        elif choice == "7":
            # Exit Application
            print("\n👋 Exiting GradeCore. Goodbye!\n")
            sys.exit(0)

        else:
            print("❌ Invalid choice. Please enter a number between 1 and 7.")


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("\nWelcome to GradeCore – Academic Result Processing Engine")
    print("=" * 40 + "\n")
    main_menu()