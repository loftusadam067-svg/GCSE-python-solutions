# Topic:       2D array (search, update value, recalculate derived field)
# Marks:       8
# Description: A school stores student exam results in a 2D array.
#              Each row contains: [StudentName, Score, Grade]
#              The 2D array arrayStudents is given below.
#
#              Write a program that:
#                - asks the user to enter a student name
#                - searches arrayStudents for that student
#                - if not found, outputs "Student not found"
#                - if found, asks the user to enter a new score (0-100)
#                - updates the Score (index 1) with the new value
#                - recalculates and updates the Grade (index 2) using:
#                    70 and above  →  "A"
#                    55 to 69      →  "B"
#                    40 to 54      →  "C"
#                    below 40      →  "U"
#                - outputs "Updated: " followed by the name, new score,
#                  and new grade
#
# Column index reference:
#   Index 0 = StudentName   e.g. "Alice"
#   Index 1 = Score         e.g. "72"  -- stored as string, cast before use
#   Index 2 = Grade         e.g. "A"
#
# Example run:
#   Enter student name: Bob
#   Enter new score for Bob: 68
#   Updated: Bob  68  B

arrayStudents = [
    ["Alice", "72", "A"],
    ["Bob",   "55", "B"],
    ["Carol", "38", "U"],
    ["Dan",   "61", "B"],
    ["Eve",   "90", "A"],
]

# Write your solution below:
