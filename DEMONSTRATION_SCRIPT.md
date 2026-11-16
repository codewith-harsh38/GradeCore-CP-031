# GradeCore – 2-Minute Demonstration Script

## CP-031 Capstone Project Overview

**Project:** GradeCore – Academic Result Processing and Ranking Engine  
**Time:** approximately 120 seconds  
**Features Covered:** All 5 compulsory features

---

## Demonstration Flow (120 Seconds)

| Section | Time | Content |
|---------|------|---------|
| **Introduction** | 0:00–0:15 | Project overview and menu presentation |
| **Adding Students** | 0:15–0:45 | Register 2 students with marks |
| **Results Calculation** | 0:45–1:00 | Calculate results for all students |
| **Display Rankings** | 1:00–1:15 | Show competition rankings |
| **Report Card** | 1:15–1:35 | Generate and show a report card |
| **Subject Toppers** | 1:35–1:55 | Display subject toppers (including tie example) |
| **Conclusion** | 1:55–2:00 | Summary and exit |

---

## Detailed Script

### [0:00–0:15] Introduction

**Demonstrator:** "Hello, welcome to the GradeCore demonstration. GradeCore is a CP-031 capstone project – an Academic Result Processing and Ranking Engine designed to automate student mark entry, result calculations, grade assignment, student ranking, and report card generation.

The application is a menu-driven console program written in Python 3, using only the standard library with no external dependencies."

*(Optional – navigate to main menu)*
```
GRADECORE – MAIN MENU

  1. Add New Student
  2. View All Students
  3. Calculate Student Results
  4. Display Student Rankings
  5. Generate Student Report Card
  6. Display Subject Toppers
  7. Exit Application

Enter your choice (1-7): 
```

---

### [0:15–0:45] Adding Students

**Demonstrator:** "I'll now add two students with different marks.

*(Choose Option 1 – Add New Student)*

**Step 1:** Enter student ID: S001

**Step 2:** Enter student name: Alice Johnson

**Step 3:** Enter marks for each subject:
- Mathematics: 85
- Physics: 78
- Chemistry: 92
- English: 67
- Computer Science: 80

**Result:** "✅ Student 'Alice Johnson' (ID: S001) registered successfully!"

**Step 4:** Add a second student

**Student ID:** S002

**Name:** Bob Smith

**Marks:**
- Mathematics: 75
- Physics: 85
- Chemistry: 88
- English: 72
- Computer Science: 90

**Result:** "✅ Student 'Bob Smith' (ID: S002) registered successfully!"

**Demonstrator:** "Two students are now registered. Let me verify by viewing all students."

*(Choose Option 2 – View All Students)*
```
Student ID   Name              Percentage
S001         Alice Johnson              80.40%
S002         Bob Smith                77.60%
```

---

### [0:45–1:00] Results Calculation

**Demonstrator:** "Now I'll calculate the results for all students.

*(Choose Option 3 – Calculate Student Results)*

**Result:** "✅ Results calculated for all students."

**Demonstrator:** "The application has automatically computed:
- Total marks out of 500
- Percentage with 2 decimal places
- Grade assignment (A+, A, B, C, D, F)
- Subject-wise pass/fail status
- Overall result (PASS/FAIL)"

---

### [1:00–1:15] Display Rankings

**Demonstrator:** "Let me display the student rankings by percentage.

*(Choose Option 4 – Display Student Rankings)*

*(Expected output – competition ranking)*
```
Rank   Student ID   Name          Percentage
  1         S001     Alice Johnson     80.40%
  2         S002     Bob Smith         77.60%
```

**Demonstrator:** "Alice Johnson is ranked 1st with 80.40%, and Bob Smith is ranked 2nd with 77.60%. The ranking is in descending order by percentage. Note that the competition ranking system (1, 2, 2, 4) is implemented – if two students had the same percentage, they would receive the same rank."

---

### [1:15–1:35] Report Card

**Demonstrator:** "Now let me generate a formatted report card for Alice Johnson.

*(Choose Option 5 – Generate Student Report Card)*

**Input:** Enter student ID: S001

*(Expected output – formatted report card)*
```
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

    Total Marks:      402 / 500
    Percentage:       80.40%
    Grade:             B
    Overall Result:   PASS
    Student Rank:     1

==================================================
      Thank you for using GradeCore!
==================================================
```

**Demonstrator:** "The report card includes all required information: student ID, name, all five subjects with marks and pass/fail status, total marks, percentage, grade, overall result, and student rank."

---

### [1:35–1:55] Subject Toppers

**Demonstrator:** "Let me display the subject toppers – the highest scorer in each subject.

*(Choose Option 6 – Display Subject Toppers)*

*(Expected output)*
```
==================================================
          GRADECORE – SUBJECT TOPPERS
==================================================

  Mathematics: Alice — 85
  Physics: Alice — 78
  Chemistry: Bob — 88
  English: Bob — 72
  Computer Science: Bob — 90
==================================================
```

**Demonstrator:** "The application identifies the highest scorer in each subject:
- Mathematics: Alice with 85 marks
- Physics: Alice with 78 marks
- Chemistry: Bob with 88 marks
- English: Bob with 72 marks
- Computer Science: Bob with 90 marks

If multiple students had the same highest mark, the application would display all of them with a 'tied' notation."

---

### [1:55–2:00] Conclusion

**Demonstrator:** "That concludes the GradeCore demonstration. In approximately 2 minutes, we've covered all five compulsory features:

1. ✅ Student registration with mark validation
2. ✅ Result calculation (total, percentage, grade)
3. ✅ Subject-wise and overall pass/fail
4. ✅ Student ranking with competition ranking
5. ✅ Report card generation and subject toppers

GradeCore reduces manual calculation errors and provides accurate academic results. The application is ready for demonstration and can be run locally with `python gradecore.py`. Thank you."

---

## Key Points to Emphasize During Demonstration

1. **Input validation** – Show how the program rejects invalid marks (negative, >100, alphabetic)
2. **Competition ranking** – Highlight the 1, 2, 2, 4 ranking system if ties are demonstrated
3. **Pass/fail separation** – Emphasize that grade and overall result are kept separate
4. **Report card format** – Point out all 10 sections of the formatted report card
5. **No external dependencies** – Mention that only Python 3 standard library is required

---

## Troubleshooting During Demonstration

| Issue | Resolution |
|-------|------------|
| "EOF when reading a line" | This occurs in some IDE environments without stdin. The code is correct – run in a proper terminal. |
| Invalid choice error | Enter a number between 1 and 7 |
| "No students registered yet" | Add students first (Option 1) before viewing rankings/report cards |
| Unexpected mark input | Enter marks between 0 and 100 only |

---

## Time-Saving Variation (if < 120 seconds available)

**Condensed flow (80 seconds):**
1. Add 1 student (0:00–0:20)
2. Calculate results (0:20–0:30)
3. Show report card (0:30–0:50)
4. Show subject toppers (0:50–1:10)
5. Show rankings (1:10–1:20)
6. Exit (1:20–1:25)

Or skip the report card and focus on: add student → calculate → ranking → toppers → exit.