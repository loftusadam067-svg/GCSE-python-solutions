# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This repository contains model solutions for OCR GCSE Computer Science Section B programming questions (Python and SQL), covering past papers from 2022–2024. Each file is a standalone, self-contained script targeting GCSE-level students.

The repository also includes a bank of practice questions organised by topic and difficulty.

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

## Example Questions Folder

Practice question stubs live under `example_questions/`. Each question is an empty file with a header comment describing the task — students write their solution at the bottom.

```
example_questions/
├── python_questions/
│   ├── easy_difficulty/       PQ1–PQ10  (input validation, functions, loops, 2D arrays, file I/O)
│   ├── medium_difficulty/     PQ1–PQ6   (re-prompt loops, multi-function, min/max, strings, lists, file read)
│   └── hard_difficulty/       PQ1–PQ5   (multi-field validation, statistics, Caesar cipher, 2D update, file transform)
└── sql_questions/
    ├── easy_difficulty/       SQ1–SQ3   (SELECT WHERE single/AND conditions, ORDER BY)
    ├── medium_difficulty/     SQ1–SQ4   (OR, LIKE, COUNT aggregate, ORDER BY DESC)
    └── hard_difficulty/       SQ1–SQ3   (GROUP BY + COUNT, INNER JOIN, GROUP BY + HAVING)
```

### Difficulty levels

| Level  | Description                                                                                  |
|--------|----------------------------------------------------------------------------------------------|
| Easy   | Single concept per question. Directly mirrors past-paper question parts (3–6 marks).         |
| Medium | Two concepts combined. Requires using familiar syntax in a slightly more complex way (6–7 marks). |
| Hard   | Multi-step programs. May involve character-level processing, file transforms, or 2D updates (7–9 marks). |

### Example question file naming

Python question files use the pattern `PQN.py` (e.g. `PQ1.py`, `PQ10.py`).
SQL question files use the pattern `SQN.sql` (e.g. `SQ1.sql`, `SQ3.sql`).
Numbers restart at 1 within each difficulty folder — `easy_difficulty/PQ1.py` and `medium_difficulty/PQ1.py` are different questions.

Each difficulty folder contains a `README.md` with guidance on how to approach the questions in that folder.
