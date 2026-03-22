# SQL Problem: CTE WITH DENSE_RANK() WINDOW FUNCTIONS
![alt text](e-commerce-schema-1.png)
## Problem
Find the top 3 products by revenue for each category.

---

## Approach
...

---

## Query

```sql
----------SQL---------------
WITH ranked AS (
  SELECT 
    c.name AS category,
    p.name AS product,
    SUM(oi.quantity * oi.unit_price) AS revenue,
    DENSE_RANK() OVER (
      PARTITION BY c.category_id
      ORDER BY SUM(oi.quantity* oi.unit_price) DESC
    ) AS rank
  FROM order_item oi
  JOIN product p ON oi.product_id = p.product_id
  JOIN category c ON c.category_id = p.category_id
  GROUP BY c.category_id,p.product_id
)
SELECT * FROM ranked where rank<=3;
--------END SQL-------------
```
## Follow up questions
Find users who ordered in January but not in February.
```sql
----------SQL---------------
SELECT DISTINCT user_id FROM orders
WHERE DATE_TRUNC('month', created_at) = '2024-01-01'

EXCEPT

SELECT DISTINCT user_id FROM orders
WHERE DATE_TRUNC('month', created_at) = '2024-02-01';

--------END SQL-------------
```

## Alternate Solution

## Advance Level Solution