# Python Questions — Easy Difficulty

These questions cover the foundational Python skills assessed at GCSE. Each question targets a single concept and is worth 3–6 marks.

## Topics covered

| File  | Topic                                      |
|-------|--------------------------------------------|
| PQ1   | Input validation — numeric range check     |
| PQ2   | Input validation — multiple fields         |
| PQ3   | Functions — single return value            |
| PQ4   | Functions — grade boundary conditions      |
| PQ5   | While loop — running total with sentinel   |
| PQ6   | While loop — tracking minimum value        |
| PQ7   | 2D array — linear search                   |
| PQ8   | 2D array — accumulation across rows        |
| PQ9   | Boolean logic — compound condition         |
| PQ10  | File I/O — append mode                     |

## How to approach these questions

**Read the description carefully.** The description tells you exactly what inputs to expect, what to compute, and what to output. Match your output format precisely — even a missing space can lose a mark.

**Plan your structure before writing code.** Most questions follow a predictable pattern:

1. **Input** — collect what the user enters (or use the given data)
2. **Validation / Logic** — check conditions or calculate a result
3. **Output** — print the answer

**Input validation questions (PQ1, PQ2):** Check each condition with a simple `if` chain. Use `.isdigit()` before casting a string to `int` — never try `int(x)` on raw input without checking first.

**Function questions (PQ3, PQ4):** Define the function with `def`, use `return` to give back the result. You only need to write the function — you do not need to add user input code unless the question says so.

**Loop questions (PQ5, PQ6):** Use `while True` with a `break` when the sentinel value is entered, or use `while entry != "stop"`. Keep a running variable (total, minimum) and update it inside the loop.

**2D array questions (PQ7, PQ8):** Use a `for` loop to go through each row. Access columns by index number — for example, `row[0]` for the first column. Cast strings to `int` or `float` when you need to do arithmetic.

**Boolean logic (PQ9):** Write the condition exactly as described. Use `and` and `or` with brackets to group conditions where needed.

**File I/O (PQ10):** Open the file with `open("filename", "a")` for append mode. Use `\n` at the end of each line you write. The question will tell you which mode to use — use `"a"` when you must not overwrite existing content.

## Common mistakes to avoid

- Forgetting to cast input: `int(input(...))` will crash if the user types a letter — always use `.isdigit()` first.
- Comparing strings with the wrong case: `"Gold" == "gold"` is `False`.
- Off-by-one errors in range checks: `>= 1` and `<= 100` both use `=` to include the boundary values.
- Printing the wrong variable: double-check you are printing the result, not the input.
