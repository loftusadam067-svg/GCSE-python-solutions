# SQL Questions — Hard Difficulty

These questions introduce GROUP BY, HAVING, and INNER JOIN — the most complex SQL features at GCSE level. Each question is worth 5–6 marks and requires combining multiple clauses in the right order.

## Topics covered

| File  | Topic                                         |
|-------|-----------------------------------------------|
| SQ1   | GROUP BY with COUNT and ORDER BY              |
| SQ2   | INNER JOIN across two tables                  |
| SQ3   | GROUP BY with SUM and HAVING                  |

## How to approach these questions

**GROUP BY (SQ1, SQ3):** Use `GROUP BY` when you need a result *per category* — for example, the number of lessons per subject, or the total units per product. The column you group by must appear in your `SELECT` list. Your aggregate function (`COUNT`, `SUM`, etc.) goes in the `SELECT` too.

```sql
SELECT Subject, COUNT(*) AS LessonCount
FROM TblLessons
GROUP BY Subject
ORDER BY LessonCount DESC;
```

The clause order is: SELECT → FROM → WHERE (optional) → GROUP BY → HAVING (optional) → ORDER BY.

**HAVING vs WHERE (SQ3):** `WHERE` filters individual rows *before* grouping. `HAVING` filters groups *after* grouping, so it can use the result of an aggregate function. If the question says "only include [groups] where the total is greater than X", use `HAVING`:

```sql
GROUP BY ProductName
HAVING SUM(Units) > 60
```

You cannot use `WHERE SUM(Units) > 60` — `WHERE` does not know the group total yet.

**INNER JOIN (SQ2):** Use a JOIN when the data you need is spread across two tables. Identify the shared column (the foreign key) and match the tables on it:

```sql
SELECT TblCustomers.FullName, TblOrders.OrderID, TblOrders.Total
FROM TblOrders
INNER JOIN TblCustomers ON TblOrders.CustomerID = TblCustomers.CustomerID
WHERE TblOrders.Status = "Dispatched";
```

Name each column with its table prefix (`TableName.ColumnName`) to avoid ambiguity when both tables have columns with the same name.

## Common mistakes to avoid

- Using `WHERE` instead of `HAVING` to filter on an aggregate result — `WHERE` cannot see group totals.
- Including a non-aggregated column in `SELECT` without also putting it in `GROUP BY`.
- In a JOIN, writing `ON` with the wrong column — both sides of `ON` must refer to the same piece of data (usually an ID).
- Forgetting table prefixes in a JOIN query when both tables share a column name (e.g. `CustomerID`).
- Putting `HAVING` before `GROUP BY` — it must come after.
