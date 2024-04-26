# Subqueries:

## Scalar:

1. Get paintings that are above average price

```sql
SELECT artwork_name, listed_price
FROM paintings
WHERE listed_price > (
    SELECT AVG(listed_price)
    FROM paintings
);
```
