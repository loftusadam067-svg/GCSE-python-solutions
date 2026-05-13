# SQL Questions — Easy Difficulty

These questions cover the core SELECT syntax assessed at GCSE. Each question is worth 3–4 marks and focuses on retrieving data with simple conditions.

## Topics covered

| File  | Topic                                               |
|-------|-----------------------------------------------------|
| SQ1   | SELECT with WHERE — single condition                |
| SQ2   | SELECT with WHERE and AND — two conditions          |
| SQ3   | SELECT with WHERE, AND, and ORDER BY                |

## How to approach these questions

**Learn the template.** Every SELECT query at this level follows the same skeleton:

```sql
SELECT column1, column2
FROM TableName
WHERE condition
ORDER BY column ASC;
```

Work through it top-to-bottom. Ask yourself:
1. Which columns do I need? (`SELECT *` for all, or list specific names)
2. Which table? (`FROM`)
3. What filter? (`WHERE`)
4. Any sorting? (`ORDER BY ... ASC` or `DESC`)

**Choosing columns (SQ1 vs SQ2):** If the question says "all fields", use `SELECT *`. If it says specific fields, list them by name separated by commas.

**WHERE with AND (SQ2, SQ3):** Both conditions must be true for a row to appear. Write each condition separately, joined by `AND`:

```sql
WHERE Total > 100 AND Status = "Dispatched"
```

**ORDER BY (SQ3):** Put `ORDER BY` at the very end of your query, after `WHERE`. Use `ASC` for smallest-to-largest (or A–Z), `DESC` for largest-to-smallest. If the question says "ascending order", `ASC` is the default and can be omitted, but writing it makes your intent clear.

**String values need quotes.** Numbers do not. `WHERE Age = 34` is correct. `WHERE MembershipType = "Gold"` needs the quotes.

## Common mistakes to avoid

- Writing `SELECT *` when the question asks for specific columns — re-read what fields are required.
- Putting `ORDER BY` before `WHERE` — the order must be SELECT → FROM → WHERE → ORDER BY.
- Missing the equals sign in a condition: `WHERE Status "Gold"` is a syntax error.
- Using the wrong comparison operator: `>` means strictly greater than; `>=` includes the boundary value.
