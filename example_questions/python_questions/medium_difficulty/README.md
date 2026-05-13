# Python Questions — Medium Difficulty

These questions combine two or more concepts from the easy set. Each question is worth 6–7 marks and requires you to think across multiple steps.

## Topics covered

| File  | Topic                                              |
|-------|----------------------------------------------------|
| PQ1   | Input validation — re-prompt loop until valid      |
| PQ2   | Functions — two functions, one calls the other     |
| PQ3   | While loop — tracking both minimum and maximum     |
| PQ4   | String functions — length check and character scan |
| PQ5   | List operations — iteration and counting           |
| PQ6   | File I/O — reading and finding a maximum value     |

## How to approach these questions

**Identify which concepts are being combined.** These questions do not introduce new Python syntax — they ask you to use what you already know in slightly more complex ways. Before writing anything, name the building blocks you need (e.g. "I need a loop inside a loop" or "I need a function that calls another function").

**Re-prompt loops (PQ1):** Use `while True` and only `break` out when the input is valid. Put the validation check inside the loop. This is a common exam pattern — the loop must keep running until the user gets it right.

**Two-function questions (PQ2):** Write the simpler function first. Then write the second function that calls it. Make sure you use the return value from the first function — store it in a variable inside the second function.

**Tracking two values at once (PQ3):** You need two variables — one for the highest value seen so far and one for the lowest. Set both to the first value entered before the loop begins, then update them each time a new value comes in.

**String functions (PQ4):** Use `len(username)` to check the length. To check for spaces, loop through each character with a `for` loop and check if the character equals `" "`. Alternatively, use `" " in username` — both approaches work at GCSE level.

**List iteration and counting (PQ5):** Use a `for` loop to go through the list. Keep a counter variable and increment it with `+= 1` each time a condition is met. The number of fails is simply the total length minus the number of passes.

**File reading (PQ6):** Open the file with `open("filename", "r")`. Use a `for` loop to read each line. Strip the newline character with `.strip()` or `.rstrip("\n")` before processing. Split each line on the comma with `.split(",")` to separate the name from the number.

## Common mistakes to avoid

- In a re-prompt loop, forgetting to read new input inside the loop body — if you only read once before the loop, the value never changes.
- In a two-function question, calling the helper function but ignoring its return value.
- Forgetting to initialise the min/max variables before the loop starts.
- When reading a file, forgetting that every value read from a file is a string — cast to `int` or `float` before comparing or calculating.
- Off-by-one: `>=` is not the same as `>`. Check whether the boundary value should be included.
