# SQL Problem: Islands and Gaps

## Problem
Find the longest streak of consecutive login days for a user?
...

---

## Approach
The trick is subtracting a row number from each date ; consecutive dates will produce the same "group_id".
...

---

## Query

```sql
WITH login_groups AS (
  SELECT 
    user_id,
    login_date,
    login_date - ROW_NUMBER() OVER (
      PARTITION BY user_id 
      ORDER BY login_date
    ) * INTERVAL '1 day' AS group_id
  FROM user_logins
)
SELECT 
  user_id,
  MIN(login_date) AS streak_start,
  MAX(login_date) AS streak_end,
  COUNT(*) AS streak_length
FROM login_groups
GROUP BY user_id, group_id
ORDER BY streak_length DESC
LIMIT 1;

```
## Follow up questions
How do you handle NULL values in calculations and comparisons?
Ans: NULL represents missing or unknown data and requires special handling:

Comparisons: Use IS NULL or IS NOT NULL instead of = NULL
COALESCE(): Returns the first non-NULL value: COALESCE(column, 'default')
NULLIF(): Returns NULL if two values are equal: NULLIF(a, b)
ISNULL() / NVL(): Database-specific functions to replace NULL values
Example :
SELECT 
  name,
  COALESCE(phone, email, 'No contact') AS contact_info,
  CASE WHEN status IS NULL THEN 'Unknown' ELSE status END AS status
FROM customers;

## Alternate Solution

## Advance Level Solution