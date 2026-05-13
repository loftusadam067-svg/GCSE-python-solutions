# SQL Questions — Medium Difficulty

These questions build on the easy SELECT pattern by introducing more conditions in the WHERE clause, numerical comparisons, and ORDER BY ASC. Each question is worth 4–5 marks.

## Topics covered

| File  | Topic                                                               |
|-------|---------------------------------------------------------------------|
| SQ1   | SELECT with WHERE and three AND conditions (all equality)           |
| SQ2   | SELECT specific fields with WHERE AND and a numerical comparison    |
| SQ3   | SELECT specific fields with WHERE AND, comparison, and ORDER BY ASC |
| SQ4   | SELECT specific fields with WHERE, three conditions, and ORDER BY ASC |

## How to approach these questions

**More conditions does not mean more complexity — just more care.** You already know AND from the easy questions. Medium questions ask you to use it with three or more conditions, and to mix equality (`=`) with comparison operators (`>`, `<`, `>=`, `<=`).

**Three AND conditions (SQ1):** Write each condition separately, joined by AND. The order you write the conditions does not affect the result, but be precise — every condition must be met:

```sql
WHERE Year = 10 AND House = "Red" AND Active = "Yes"
```

**Numerical comparisons (SQ2):** Use `>`, `<`, `>=`, `<=` when comparing numbers. No quotes around the number:

```sql
WHERE RoomType = "Deluxe" AND Nights > 3
```

Note: `"Deluxe"` needs quotes (it is a string), but `3` does not (it is a number).

**Adding ORDER BY ASC (SQ3, SQ4):** Put ORDER BY at the very end of your query, after WHERE. The column you sort on does not have to be in your WHERE clause:

```sql
SELECT RunnerName, Time
FROM TblResults
WHERE Event = "100m" AND Time < 14
ORDER BY Time ASC;
```

**Selecting specific columns (SQ2, SQ3, SQ4):** List column names separated by commas instead of using `*`. Match the column names exactly as they appear in the table — capitalisation matters.

## Common mistakes to avoid

- Adding quotes around numbers in a comparison (`Nights > "3"` is wrong — use `Nights > 3`).
- Forgetting to put quotes around string values (`House = Red` is wrong — use `House = "Red"`).
- Putting ORDER BY before WHERE — the order must always be: SELECT → FROM → WHERE → ORDER BY.
- Writing `=<` or `=>` — the correct forms are `<=` and `>=` (the equals sign always comes second).
