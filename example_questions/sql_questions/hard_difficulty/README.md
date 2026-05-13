# SQL Questions — Hard Difficulty

These questions use the same keywords as the easy and medium questions — SELECT, FROM, WHERE, AND, ORDER BY ASC — but require you to handle four or more conditions at once, construct range checks, and select the right subset of columns from a wider table. Each question is worth 5 marks.

## Topics covered

| File  | Topic                                                                       |
|-------|-----------------------------------------------------------------------------|
| SQ1   | SELECT with WHERE and four AND conditions                                   |
| SQ2   | SELECT specific fields with WHERE range condition and ORDER BY ASC          |
| SQ3   | SELECT specific fields with WHERE, four conditions, and ORDER BY ASC        |

## How to approach these questions

**Read all the conditions before writing anything.** Hard questions combine four or more AND conditions, and it is easy to miss one. Underline or list each condition in the question description before translating it into SQL.

**Four AND conditions (SQ1):** Structure is the same as before — one condition per clause, all joined by AND. Take each condition in turn:

```sql
WHERE Ward = "A" AND Year = 2024 AND Urgent = "No" AND Checked = "Yes"
```

**Range conditions (SQ2):** A range ("between X and Y") requires two separate comparisons on the same column, both joined by AND. Do not use BETWEEN — just write the two inequalities:

```sql
WHERE Category = "Dairy" AND Price > 1.00 AND Price < 2.00
```

Both comparisons reference the same column (`Price`). This is not a mistake — it is the correct way to express a range.

**Combining four conditions with ORDER BY (SQ3):** Build the WHERE clause condition by condition. Once all conditions are in place, add ORDER BY at the end. Double-check that you are ordering by the column the question specifies, which may be different from the columns in your WHERE:

```sql
SELECT FullName, Score
FROM TblApplicants
WHERE Role = "Software Dev" AND Stage = "Final" AND Score >= 85 AND Available = "Yes"
ORDER BY Score ASC;
```

**Checking your expected output:** Count the rows in the sample table that satisfy all your conditions. If your expected output does not match the question's expected output, re-read each condition — one is likely wrong.

## Common mistakes to avoid

- Missing one condition from a long AND chain — re-read the description and count the conditions.
- Writing a range as a single expression (`1.00 < Price < 2.00`) — SQL does not support this; write two separate conditions joined by AND.
- Putting the equals sign before the comparison operator: `=>` is wrong, `>=` is correct.
- Sorting by the wrong column — ORDER BY applies to the output, not the filter.
- Forgetting to select the right columns — re-read which fields the question asks for.
