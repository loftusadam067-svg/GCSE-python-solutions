# Python Questions — Hard Difficulty

These questions require you to bring together several skills in a single program. Each question is worth 7–9 marks and involves multi-step logic, complex data structures, or processing that spans more than one file.

## Topics covered

| File  | Topic                                                          |
|-------|----------------------------------------------------------------|
| PQ1   | Input validation — re-prompt loops for multiple fields         |
| PQ2   | Functions — list parameter, computing multiple statistics      |
| PQ3   | String processing — character iteration and classification     |
| PQ4   | 2D array — search, update a value, recalculate derived field   |
| PQ5   | File I/O — read, process data, write to a new file             |

## How to approach these questions

**Break the problem into stages before touching the keyboard.** Hard questions almost always have three or four distinct phases. Write down what each phase needs to do (e.g. "Phase 1: get valid nights. Phase 2: get valid room type. Phase 3: print summary.") before writing any code.

**Re-prompt loops for multiple fields (PQ1):** Write a separate `while True` loop for each field that needs validation. Finish the first loop (confirm the value is valid and break), then move to the second loop. Do not try to validate both fields inside one loop — it gets tangled.

**List statistics function (PQ2):** Iterate through the list once with a `for` loop, accumulating the total and updating the running minimum and maximum at the same time. Calculate the average after the loop ends. Use `round(average, 1)` to get one decimal place.

**Character classification (PQ3):** Process the string one character at a time with a `for` loop. Use `.isupper()` to test whether a character is an uppercase letter and `.isdigit()` to test whether it is a digit. Keep a separate counter for each category. After the loop, check all the conditions together to decide what to return.

**2D array update (PQ4):** Search the array with a `for` loop, checking `row[0]` against the user's input. When you find a match, overwrite `row[1]` with the new score and work out the new grade using a chain of `if / elif / else`. Store the updated grade in `row[2]`. Print the result after the update.

**Read-process-write (PQ5):** Open the input file for reading and build a list of results in memory. Close the input file (or use `with`). Then open the output file for writing and write each processed result. Do not try to read and write the same file at the same time.

## Common mistakes to avoid

- In a multi-field re-prompt, putting both fields inside one loop — validate them one at a time with separate loops.
- In the character classification function, forgetting to check the length of the password separately from the character counts.
- Forgetting that strings in a 2D array must be cast to `int` or `float` before arithmetic.
- When writing to a file, forgetting the `\n` at the end of each line — lines will all appear on one line without it.
- Mixing up `"r"` (read) and `"w"` (write) modes when opening files.
