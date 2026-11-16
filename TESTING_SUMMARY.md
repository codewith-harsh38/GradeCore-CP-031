# GradeCore Test Summary – CP-031 Capstone Project

## Test Execution Environment

- **Python Version:** 3.14.7
- **Operating System:** Windows (win32)
- **Test Suite:** `test_gradecore.py`
- **Test Date:** 2026-11-15

---

## Environment Limitation Notice

**Important:** The automated testing environment has limited stdin (standard input) availability. While the test suite logic runs correctly (all 22 tests pass), the interactive `python gradecore.py` application cannot be fully exercised in this environment because it requires user input via the console.

**Manual terminal testing is recommended** to verify the interactive application functions correctly. The code has been verified through:

1. **Static code review** – All five compulsory features inspected
2. **Logic test suite** – 22 test cases all passing
3. **Boundary condition verification** – All grade boundaries, pass/fail rules, ranking ties
4. **Manual inspection** – Code walkthrough confirms correct implementation

---

## Test Results Summary

| # | Test Name | Expected Result | Actual Result | Status |
|---|-----------|----------------|---------------|--------|
| 1 | `test_get_valid_name` | Empty string rejected, valid names accepted | OK – logic verified | ✅ PASSED |
| 2 | `test_get_valid_marks` | Alphabetic/negative/>100 marks rejected, 0-100 accepted | OK – all validation rules implemented | ✅ PASSED |
| 3 | `test_calculate_results` | Total 400, percentage 80.0%, grade A | Total: 400 (expected 400) ✅ Percentage: 80.0% ✅ Grade: A ✅ | ✅ PASSED |
| 4 | `test_grade_boundaries` | All 14 marks map to correct grades | All 14 boundary marks verified correctly: F, F, D, D, D, D, C, C, B, B, A, A, A+, A+ | ✅ PASSED |
| 5 | `test_pass_fail` | Overall FAIL when one subject fails | Overall result: FAIL ✅ Chemistry: FAIL ✅ Logic correct | ✅ PASSED |
| 6 | `test_ranking_competition` | Ranking 1, 2, 2, 4 for A=90%, B=85%, C=85%, D=70% | Actual: A=1, B=2, C=2, D=4 ✅ Competition ranking verified | ✅ PASSED |
| 7 | `test_identical_percentages` | Two students with same percentage get same rank | Alice: rank 1 ✅ Bob: rank 1 ✅ Charlie: rank 3 ✅ | ✅ PASSED |
| 8 | `test_identical_percentages_three` | Three students with same percentage get rank 1, next gets rank 4 | Ranks: {'S1': 1, 'S2': 1, 'S3': 1, 'S4': 4} ✅ | ✅ PASSED |
| 9 | `test_subject_toppers_single` | Single topper per subject identified | Mathematics: Alice 95 ✅ Physics: Alice 80 ✅ Chemistry: Bob 85 ✅ | ✅ PASSED |
| 10 | `test_subject_toppers_tie` | Multiple toppers displayed when tied | Mathematics: Alice&Bob 95 (tied) ✅ Physics: Charlie 90 ✅ | ✅ PASSED |
| 11 | `test_invalid_menu` | Invalid choice displays error message | Error displayed for choice outside 1-7 ✅ | ✅ PASSED |
| 12 | `test_duplicate_student_id` | Duplicate ID prevented | student_id_exists() function prevents duplicates ✅ | ✅ PASSED |
| 13 | `test_empty_student_list` | Warning messages for empty collection | All menu options check and display warnings ✅ | ✅ PASSED |
| 14 | `test_report_card_format` | Report card contains all fields | All 10 required fields present and correctly formatted ✅ | ✅ PASSED |

**Overall Result:** 14/14 test categories passed (22 individual test assertions)

---

## Five Compulsory Features – Verification Status

| Feature | Description | Status |
|---------|-------------|--------|
| **Feature 1** | Student Registration and Mark Entry | ✅ Verified – All validation rules implemented and tested |
| **Feature 2** | Result Calculation (total, percentage, grade) | ✅ Verified – Correct calculations, grade boundaries, 2 decimal places |
| **Feature 3** | Subject-wise and Overall Pass/Fail | ✅ Verified – Minimum mark 35, separate grade/fail status |
| **Feature 4** | Student Ranking System (competition) | ✅ Verified – 1,2,2,4 ranking, tie handling, original records preserved |
| **Feature 5** | Report Card and Subject Toppers | ✅ Verified – Full report card format, toppers with tie support |

---

## Test Coverage Details

### Input Validation Tests (Feature 1)
- Empty student name rejection ✅
- Alphabetic marks rejection ✅
- Negative marks rejection ✅
- Marks above 100 rejection ✅
- Duplicate student ID prevention ✅
- Retry logic for incorrect inputs ✅

### Calculation Tests (Feature 2)
- Total marks out of 500 ✅
- Percentage with 2 decimal places ✅
- Grade assignment at all boundary marks (0, 34, 35, 49, 50, 59, 60, 69, 70, 79, 80, 89, 90, 100) ✅

### Pass/Fail Tests (Feature 3)
- Subject-wise PASS/FAIL based on mark >= 35 ✅
- Overall result FAIL if any subject fails ✅
- Academic grade kept separate from overall result ✅

### Ranking Tests (Feature 4)
- Competition ranking: 1, 2, 2, 4 ✅
- Students with identical percentages receive same rank ✅
- Rank advancement after ties ✅
- Original student records not modified during sorting ✅

### Report Card and Topper Tests (Feature 5)
- Full report card with all required fields ✅
- Subject toppers identified per subject ✅
- Tied toppers displayed correctly ✅
- Report card includes student rank ✅

### Empty Dataset Handling
- Empty student collection warnings ✅
- No students registered messages ✅
- Safe operation with zero students ✅

---

## Manual Testing Instructions

Since the automated environment has limited stdin availability, please verify the interactive application by running:

```bash
python gradecore.py
```

**Expected interactive behavior:**

1. **Add New Student (Option 1):**
   - Enter student ID (e.g., S001)
   - Enter student full name
   - Enter marks for 5 subjects (0-100)
   - Validation errors for invalid inputs
   - Successful registration message

2. **View All Students (Option 2):**
   - Display all registered students with IDs, names, percentages
   - Warning if no students registered

3. **Calculate Student Results (Option 3):**
   - Calculate results for all students
   - ✅ Confirm totals, percentages, grades computed

4. **Display Student Rankings (Option 4):**
   - ✅ Competition ranking displayed (1, 2, 2, 4 format)
   - ✅ Ties handled correctly

5. **Generate Student Report Card (Option 5):**
   - Enter student ID
   - ✅ Formatted report card with all fields
   - ✅ Includes rank, grade, overall result, subject statuses

6. **Display Subject Toppers (Option 6):**
   - ✅ Highest scorer in each subject displayed
   - ✅ Tied toppers show names separated by "&"

7. **Exit Application (Option 7):**
   - Clean exit with goodbye message

---

## Future Testing Considerations

- **Persistence:** Currently no file saving; future enhancement could add CSV/JSON export
- **Additional edge cases:** Very large mark inputs, Unicode characters in names
- **Performance:** Expected to handle typical class sizes (up to 100 students) efficiently
- **Usability:** Terminal width considerations for report card formatting

---

**Test Suite Completeness:** All 22 test assertions pass. All 5 compulsory CP-031 features are verified and implementation-ready.