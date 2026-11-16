# GradeCore – Academic Result Processing and Ranking Engine

## Project ID: CP-031
## Level: Foundation
## Programming Language: Python 3
## Application Type: Menu-driven console application

---

## Project Introduction

GradeCore is an academic result management application designed to automate student mark entry, result calculations, grade assignment, student ranking, and report card generation. The application reduces manual calculation errors and provides accurate academic results for educational institutions.

This capstone project implements a complete result processing system using Python 3's standard library, featuring a clean console-based interface suitable for foundation-level students and educators.

---

## Problem Statement

Manual academic result processing in educational institutions involves:
- Time-consuming mark entry and calculation
- Human errors in totaling marks and determining grades
- Inconsistent ranking methodologies
- Difficulties in generating standardized report cards
- Lack of automated subject-wise pass/fail analysis

GradeCore addresses these problems by providing an automated, error-free result processing engine that handles all academic result requirements through a simple console interface.

---

## Project Objectives

1. **Automate student registration** – Capture student IDs and names with proper validation
2. **Enable accurate mark entry** – Accept marks for five subjects with strict input validation
3. **Calculate results automatically** – Compute totals, percentages, and grades without manual intervention
4. **Determine pass/fail status** – Subject-wise and overall result analysis based on minimum passing criteria
5. **Rank students fairly** – Competition ranking system that handles ties correctly
6. **Generate formatted report cards** – Professional output containing all result details
7. **Identify subject toppers** – Recognize highest scorers in each subject

---

## Technologies Used

- **Python 3** – Core programming language
- **Standard Library Only** – No external dependencies required
  - `sys` – Application exit handling
  - Built-in data structures: `lists`, `dicts`
  - String formatting for terminal output
  - Comparison and sorting algorithms

- **Development Environment** – Any Python 3 environment (IDLE, VS Code, PyCharm, etc.)
- **Operating System** – Windows, macOS, or Linux (console-compatible)

---

## Project Features

### Five Compulsory Features (CP-031)

#### Feature 1: Student Registration and Mark Entry

- Accept student ID with duplicate prevention
- Accept student full name (reject empty names)
- Accept marks for exactly five subjects:
  - Mathematics
  - Physics
  - Chemistry
  - English
  - Computer Science
- Validate marks between 0 and 100 inclusive
- Reject negative marks
- Reject marks above 100
- Reject alphabetic input
- Reject empty student names
- Allow users to retry incorrect inputs without restarting the program

#### Feature 2: Result Calculation

- Automatically calculate total marks out of 500
- Calculate percentage (with two decimal places)
- Assign grades based on standard boundaries:
  - 90–100: A+
  - 80–89.99: A
  - 70–79.99: B
  - 60–69.99: C
  - 50–59.99: D
  - Below 50: F
- Display percentages up to two decimal places

#### Feature 3: Subject-wise Pass/Fail

- Minimum passing mark: 35
- Marks >= 35 = PASS
- Marks < 35 = FAIL
- Display status for every subject
- Overall result FAIL if any single subject is failed
- Otherwise, overall result is PASS
- Academic grade and overall pass/fail status kept separate

#### Feature 4: Student Ranking System

- Rank students according to percentage (descending order)
- Highest percentage receives rank 1
- Implement competition ranking: 1, 2, 2, 4 (tied students receive same rank; next rank advances by tie count)
- Do not modify original student records while sorting
- Handle students with identical percentages correctly

#### Feature 5: Report Card and Subject Toppers

- Search students using their student ID
- Generate a formatted report card containing:
  - Institution/project heading
  - Student ID
  - Student name
  - All five subjects with marks obtained
  - Individual subject pass/fail status
  - Total marks
  - Percentage
  - Grade
  - Overall result
  - Student rank
- Identify the highest scorer in each subject
- Display the topper's name and marks
- If multiple students have equal highest marks, display all of them

---

## Project Folder Structure

```
GradeCore/
├── gradecore.py      # Main application source code
├── test_gradecore.py # Comprehensive test suite
├── README.md         # Project documentation
├── requirements.txt  # Python dependencies (standard library only)
└── .gitignore        # Git ignore configuration
```

---

## Installation Instructions

### Prerequisites

- Python 3.x installed (Python 3.6 or later recommended)
- No external packages required – application uses standard library only

### Setup

1. Ensure Python 3 is installed:
   ```bash
   python --version
   ```

2. Clone or copy the project folder:
   ```bash
   # If using Git
   git clone <repository-url>

   # Or manually copy files to your desired location
   mkdir GradeCore
   copy gradecore.py test_gradecore.py README.md requirements.txt .gitignore GradeCore\
   ```

3. Navigate to the project directory:
   ```bash
   cd GradeCore
   ```

4. Verify the application runs:
   ```bash
   python gradecore.py
   ```

---

## How to Run the Application

### Launch

```bash
python gradecore.py
```

### Main Menu

The application displays a clean, interactive menu:

```
GRADECORE – MAIN MENU

  1. Add New Student
  2. View All Students
  3. Calculate Student Results
  4. Display Student Rankings
  5. Generate Student Report Card
  6. Display Subject Toppers
  7. Exit Application
```

### Menu Options

| Option | Function |
|--------|----------|
| **1** | Add New Student – Register a new student with ID, name, and subject marks |
| **2** | View All Students – Display summary of all registered students |
| **3** | Calculate Student Results – Compute totals, percentages, and grades for all students |
| **4** | Display Student Rankings – Show student rankings by percentage (competition ranking) |
| **5** | Generate Student Report Card – Create formatted report card for a specific student ID |
| **6** | Display Subject Toppers – Show highest scorers in each subject |
| **7** | Exit Application – Terminate the application |

---

## Subject Information

The application handles exactly five subjects:

1. **Mathematics**
2. **Physics**
3. **Chemistry**
4. **English**
5. **Computer Science**

All mark validation, calculation, and ranking operations apply to these five subjects exclusively.

---

## Grade Calculation Table

| Percentage Range | Grade |
|------------------|-------|
| 90 – 100         | A+    |
| 80 – 89.99       | A     |
| 70 – 79.99       | B     |
| 60 – 69.99       | C     |
| 50 – 59.99       | D     |
| Below 50         | F     |

**Note:** Percentages are calculated as `total / 5` (out of 500, five subjects). Grade assignment uses threshold comparison: `if percentage >= threshold`.

---

## Pass/Fail Calculation Rules

### Subject-wise Status

- **Pass:** Mark >= 35
- **Fail:** Mark < 35

### Overall Result

- **PASS:** All five subjects have marks >= 35
- **FAIL:** Even one subject has mark < 35 (overall result is FAIL regardless of total percentage)

**Important:** The academic grade and overall pass/fail status are kept separate. A student can have grade A but overall result FAIL if they fail even one subject.

---

## Student Ranking Algorithm

### Competition Ranking (1, 2, 2, 4)

1. **Sort** students by percentage in descending order (highest first)
2. **Initialize** rank counter at 1
3. **Iterate** through sorted students:
   - Count how many students share the current percentage (tie count)
   - **Assign** the same rank to all students in the tie group
   - **Advance** the rank counter by the tie count (this creates the "competition" effect)
   - **Continue** with the next group

### Example

With percentages: [90, 85, 85, 70]
- Student at 90% → Rank 1
- Two students at 85% → Both receive Rank 2
- Student at 70% → Rank 4 (skips rank 3 due to two-way tie at rank 2)

**Original student records are NOT modified** during the ranking process; a sorted copy is used.

---

## Report Card Format

The generated report card contains:

```
==================================================
              GRADECORE – REPORT CARD
==================================================

Student ID:   S001
Student Name: John Doe

    Subject       Marks   Status
    ---------------------------------
    Mathematics   85      PASS
    Physics       78      PASS
    Chemistry     92      PASS
    English       67      PASS
    Computer Science 80  PASS
    ---------------------------------

    Total Marks:      392 / 500
    Percentage:       78.40%
    Grade:             B
    Overall Result:   PASS
    Student Rank:     3

==================================================
      Thank you for using GradeCore!
==================================================
```

---

## Subject Topper Functionality

### Topper Identification

For each of the five subjects, the application:
1. Examines all students' marks in that subject
2. Identifies the highest mark
3. Finds all students achieving that highest mark
4. Displays the topper name(s) and mark

### Tie Handling

If multiple students have the same highest mark in a subject:
- **Single topper:** Display `Subject: Name — Mark`
- **Multiple toppers:** Display `Subject: Name1 & Name2 — Mark (tied)`

### Example Output

```
GRADECORE – SUBJECT TOPPERS

  Mathematics: Alice — 95
  Physics: Alice & Bob — 90 (tied)
  Chemistry: Charlie — 88
  English: Bob — 75
  Computer Science: Alice — 92
```

---

## Testing Instructions

### Running the Test Suite

```bash
python test_gradecore.py
```

### Test Coverage

The test suite (`test_gradecore.py`) includes 22 test cases verifying:

| Test Category | Specific Tests |
|--------------|----------------|
| **Input Validation** | Empty name rejection, alphabetic marks rejection, negative mark rejection, mark >100 rejection, duplicate student ID prevention |
| **Calculation** | Total calculation, percentage with 2 decimals, grade assignment at all boundary marks |
| **Grade Boundaries** | All 14 specified marks: 0, 34, 35, 49, 50, 59, 60, 69, 70, 79, 80, 89, 90, 100 |
| **Pass/Fail** | Subject-wise PASS/FAIL, overall FAIL when any subject fails |
| **Ranking** | Competition ranking 1,2,2,4; identical percentages handled; three students with identical percentages |
| **Subject Toppers** | Single topper per subject; tied toppers displayed |
| **Menu Handling** | Invalid menu selection, empty student collection warnings |
| **Report Card** | All required fields present and correctly formatted |

### Sample Test Marks

0, 34, 35, 49, 50, 59, 60, 69, 70, 79, 80, 89, 90 and 100

---

## Sample Application Output

### Adding a New Student

```
GRADECORE – MAIN MENU

  1. Add New Student
  2. View All Students
  3. Calculate Student Results
  4. Display Student Rankings
  5. Generate Student Report Card
  6. Display Subject Toppers
  7. Exit Application

Enter your choice (1-7): 1

--- Add New Student ---

Enter student ID (e.g., S001): S001
Enter student full name: Alice Johnson
  Enter marks for Mathematics (0-100): 85
  Enter marks for Physics (0-100): 78
  Enter marks for Chemistry (0-100): 92
  Enter marks for English (0-100): 67
  Enter marks for Computer Science (0-100): 80

✅ Student 'Alice Johnson' (ID: S001) registered successfully!
```

### Generating a Report Card

```
GRADECORE – REPORT CARD

==================================================
              GRADECORE – REPORT CARD
==================================================

Student ID:   S001
Student Name: Alice Johnson

    Subject       Marks   Status
    ---------------------------------
    Mathematics   85      PASS
    Physics       78      PASS
    Chemistry     92      PASS
    English       67      PASS
    Computer Science 80  PASS
    ---------------------------------

    Total Marks:      392 / 500
    Percentage:       78.40%
    Grade:             B
    Overall Result:   PASS
    Student Rank:     3

==================================================
      Thank you for using GradeCore!
==================================================
```

### Displaying Subject Toppers

```
GRADECORE – SUBJECT TOPPERS

==================================================
          GRADECORE – SUBJECT TOPPERS
==================================================

  Mathematics: Alice — 95
  Physics: Alice & Bob — 90 (tied)
  Chemistry: Charlie — 88
  English: Bob — 75
  Computer Science: Alice — 92
==================================================
```

---

## Limitations

1. **In-memory data storage** – Student records are stored in RAM and lost when the application exits
2. **No database integration** – This is a console application without database connectivity
3. **Fixed subject set** – Only the five specified subjects (Mathematics, Physics, Chemistry, English, Computer Science) are supported
4. **Fixed number of subjects** – Exactly five subjects per student; cannot be configured or extended
5. **No persistance** – Student data is not saved between application runs
6. **Single-user console** – Designed for individual use; no multi-user or network features
7. **No GUI** – Terminal-based interface only; no graphical windows or buttons

---

## Future Enhancements

1. **CSV/JSON persistence** – Save and load student records from data files
2. **Student search by name** – Additional search functionality beyond student ID
3. **Export results** – Generate PDF or printable report card formats
4. **Grade averaging** – Calculate cohort statistics and class averages
5. **Advanced ranking** - Percentile ranking and class performance distribution
6. **User authentication** – Login system for different user roles
7. **Web interface** – Flask-based web application version
8. **Grade weighting** – Different weightage for subjects in percentage calculation

---

## Author/Contributor Section

<student-name>
<student-id>
<course>
<institution>
<date>

*Note: This is a capstone project developed as part of academic requirements. The implementation demonstrates Python programming skills, application design, and systematic testing methodology.*
</student-name>
<student-id>
<course>
<institution>
<date>