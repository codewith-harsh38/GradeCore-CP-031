# GradeCore – GitHub Preparation Guide

## Prerequisites

- Git installed on your machine
- GitHub account (optional, for remote repository)
- Project folder: `E:\Projects\GradeCore\`

---

## Initializing Git

Open your terminal or command prompt, navigate to the project folder, and run:

```cmd
cd E:\Projects\GradeCore
git init
```

This initializes a new Git repository in the GradeCore folder.

---

## Adding Files

Add all project files to Git's tracking:

```cmd
git add gradecore.py
git add test_gradecore.py
git add README.md
git add requirements.txt
git add .gitignore
```

**Alternative – add all files at once:**

```cmd
git add .
```

---

## Creating the Initial Commit

Create the first commit with a descriptive message:

```cmd
git commit -m "Initial commit: GradeCore CP-031 capstone project"

    Included:
    - gradecore.py (main application source code)
    - test_gradecore.py (comprehensive test suite)
    - README.md (project documentation)
    - requirements.txt (Python dependencies)
    - .gitignore (Python cache and environment files)
```

---

## Setting the GitHub Remote

If you have a GitHub repository already created, set the remote:

```cmd
git remote add origin <your-github-repository-url>
```

**Example:**

```cmd
git remote add origin https://github.com/username/GradeCore.git
```

> **Note:** If you haven't created a GitHub repository yet, visit https://github.com/new, create a new repository, and follow GitHub's instructions for pushing an existing project.

---

## Pushing to the Main Branch

Push your committed changes to GitHub:

```cmd
git branch -M main
git push -u origin main
```

This:
1. Renames the current branch to `main`
2. Pushes `main` to the `origin` remote
3. Sets up tracking so future `git push` works without specifying the branch

---

## Verification

After pushing, verify your repository on GitHub contains:

- `gradecore.py`
- `test_gradecore.py`
- `README.md`
- `requirements.txt`
- `.gitignore`

**Expected repository contents:**

```
GradeCore/
│
├── gradecore.py          # Main application (CP-031 capstone)
├── test_gradecore.py     # Test suite (22 tests verified)
├── README.md             # Professional project documentation
├── requirements.txt      # Standard library only – no external deps
├── .gitignore           # Python cache and env files
└── .git/                # Git internal metadata (not listed)
```

---

## File Checksum Verification (Optional)

You may want to verify your files match the expected content:

```cmd
# Check Python file sizes and dates
dir gradecore.py
dir test_gradecore.py
dir README.md
dir requirements.txt
dir .gitignore
```

---

## .gitignore Contents

The `.gitignore` file should contain:

```
# Python
__pycache__/
*.py[cod]
*$py.class

# Environment variables
.env

# PyInstaller
*.manifest
*.spec

# Distribution / packaging
*.egg-info/
dist/
build/

# Virtual environments
venv/
env/
.venv/

# Jupyter Notebook
.ipynb_checkpoints/

# GradeCore specific
test_output/
*.log
```

This ensures Python cache files (`*.pyc`), virtual environments, and build artifacts are not tracked in Git.

---

## GitHub Repository Checklist

[ ] Repository created on GitHub
[ ] `git init` executed in local folder
[ ] All 5 files added: `gradecore.py`, `test_gradecore.py`, `README.md`, `requirements.txt`, `.gitignore`
[ ] Initial commit created with descriptive message
[ ] Remote set to GitHub repository URL
[ ] Code pushed to `main` branch
[ ] Repository accessible at expected URL
[ ] File structure verified on GitHub website