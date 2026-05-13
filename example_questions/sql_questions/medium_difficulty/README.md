# SQL Questions — Medium Difficulty

These questions extend the easy SELECT pattern with new keywords: OR, LIKE, aggregate functions, and combined ordering. Each question is worth 4–5 marks.

## Topics covered

| File  | Topic                                                    |
|-------|----------------------------------------------------------|
| SQ1   | SELECT with WHERE and OR                                 |
| SQ2   | SELECT with WHERE and LIKE                               |
| SQ3   | SELECT with COUNT aggregate                              |
| SQ4   | SELECT with AND, ORDER BY DESC — two conditions combined |

## How to approach these questions

**OR vs AND (SQ1):** `OR` returns a row if *either* condition is true. `AND` requires *both* to be true. If the question says "where X or Y", use `OR`. If it says "where X and Y", use `AND`. Mixing them up is the most common error at this level.

```sql
WHERE House = "Red" OR Year = 9
```

**LIKE with wildcards (SQ2):** `LIKE` lets you match part of a string. The `%` wildcard means "any characters here". To find rows where a title *contains* a word, put `%` on both sides:

```sql
WHERE Title LIKE "%Python%"
```

To find titles that *start* with a word, use `%` only at the end: `LIKE "Python%"`.

**COUNT aggregate (SQ3):** `COUNT(*)` counts the number of rows that match your `WHERE` clause. Give the result a name using `AS`:

```sql
SELECT COUNT(*) AS TotalScreenings
FROM TblScreenings
WHERE Hall = "A"
```

No `GROUP BY` is needed here — you are counting all matching rows, not grouping by category.

**ORDER BY DESC (SQ4):** Works exactly like `ASC` but in reverse order. Put it after `WHERE`:

```sql
SELECT FullName, Score
FROM TblApplicants
WHERE Role = "Software Dev" AND Score >= 80
ORDER BY Score DESC;
```

## Common mistakes to avoid

- Using `AND` when the question says `OR` — re-read the condition carefully.
- Forgetting the `%` signs in a `LIKE` pattern, or putting them in the wrong place.
- Forgetting the `AS` keyword when the question specifies an alias for your count.
- Putting `ORDER BY` before `WHERE` in the query.
- Omitting `DESC` when descending order is required — without it, results default to ascending.
