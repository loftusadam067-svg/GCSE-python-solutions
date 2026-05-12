# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This repository contains model solutions for OCR GCSE Computer Science Section B programming questions (Python), covering past papers from 2022–2024. Each file is a standalone, self-contained script targeting GCSE-level students.

## Running Solutions

Each file is a standalone Python script with no dependencies:

```bash
python 2022_Q5bi.py
```

There is no test suite, build step, or package manager. Solutions are verified by running them manually and supplying the expected inputs.

## File Naming Convention

Files follow the pattern `YYYY_QXyz.py`, where the question reference maps directly to the exam paper notation:

- `2023_Q6fii.py` → 2023 paper, Question 6(f)(ii)
- `2022_Q5bi.py` → 2022 paper, Question 5(b)(i)

## Required File Header

Every solution file must begin with this comment block:

```python
# Year:        YYYY
# Question:    QX(y)(z)
# Marks:       N
# Description: One or two sentences describing what the program does,
#              including any notable constraints from the question.
```

## Code Style Conventions

**Beginner-appropriate Python only.** Solutions must match the skill level assessed at GCSE:

- No imports unless the question explicitly requires them
- No list comprehensions, f-strings, or advanced constructs
- String concatenation with `+` and `str()`, not f-strings
- Use `int()` / `float()` casts explicitly rather than implicit conversion
- Validate with `.isdigit()` before casting user input to int

**Section dividers** separate logical parts of each script using the pattern `# --- Label ---`. Common labels: `Input`, `Validation`, `Calculation`, `Output`, `Main Loop`, `Variables`, `Logic`.

**Inline comments** explain the *why* — exam constraints, non-obvious choices, and anything that would surprise a student reading the code (e.g. why `"a"` mode is used instead of `"w"` in file I/O).

## Architecture

All solutions are flat scripts (no modules, no shared utilities). Where a question asks for a function, the function is defined and called within the same file — even if it duplicates a function from a related question file (e.g. `2022_Q5ci.py` and `2022_Q5cii.py` both define `newPrice()`). This is intentional: each file must be fully runnable in isolation.

2D lists (arrays) use index-based access with explicit comments documenting the column structure, since GCSE students are not expected to use dictionaries or named fields.
