# Subqueries:

## Learning Objectives:

- Practice writing queries that make use of subqueries and common table expressions.
- Identify some of the benefits of using common table expressions.

## Intro what is a subquery?

- simply defined as a query within another query

We saw a couple of different types of subquery this morning. What were they?

- single value: Scalar subquery
- multi-row

## Scalar:

1. Get paintings that are above average price

Showing the DB Diagram and ask for someone the help me with a solution.

```sql
SELECT artwork_name, listed_price
FROM paintings
WHERE listed_price > (
  SELECT AVG(listed_price)
  FROM paintings
);
```

2. Find the painting the sold for the least amount of money

Similar to the first, ask for help with a solution.

**CAREFUL NOT TO JOIN ON SALES.ARTIST_ID AS THIS WILL LEAD TO DUPLICATE ROWS (MULTIPLE ARTWORKS PER ARTIST)**

```sql
SELECT first_name, last_name, artwork_name, sales_price
FROM sales
JOIN paintings ON paintings.painting_id = sales.painting_id
JOIN artists ON sales.artist_id = artists.artist_id
WHERE sales_price = (
  SELECT MIN(sales_price)
  FROM sales
);
```

After solving these ask students to tell me how many rows are being returned from the subqueries?

- **Just the 1** -> These are known as _Scalar_ subqueries, this means they only either return a single value OR one row and one column.

**Go back to Figjam and add this subquery type to the list**

## Multi row:

1. List all collectors who haven't purchased paintings from the gallery

Again ask for help with this, students may suggest JOINs as a solution which is valid but explain I want to use a subquery for now.

```sql
SELECT first_name, last_name
FROM collectors
WHERE collector_id IN (
    SELECT collector_id
    FROM sales
);
```

After solving ask students to tell me how many rows are being returned from the subquery?

- multiple -> this is a multi-row subquery

**point out that this a a multi-row/single column subquery. There can be subqueries that returns multiple columns and multiple rows but we won't look at them here**

## Brief mention of other types of subqueries

- multi row/multi column subqueries
- correlated subqueries

**EXTRA STUFF NOT REALLY RELEVANT**

Solution with inner join for comparison:

```sql
SELECT DISTINCT collectors.first_name, collectors.last_name
FROM collectors
JOIN sales
ON collectors.collector_id = sales.collector_id;
```

Possible question: When to use joins vs subqueries? 🤔 🤔 🤔 - I believe JOINs are more optimal but defer until tomorrows lecture.

## Subquery > CTE refactor

Start:

```sql
SELECT
  sales_price,
  (SELECT MIN(sales_price) FROM sales) AS min,
  (SELECT MAX(sales_price) FROM sales) AS max,
  ROUND((SELECT AVG(sales_price) FROM sales), 2) AS average,
  ROUND(sales_price - (SELECT AVG(sales_price) FROM sales), 2) AS price_diff_from_average
FROM sales
ORDER BY price_diff_from_average DESC;
```

Explain what this is doing, showing the result of running a query.

❓ Ask students if they can spot any repetition ❓

**If no answers point out that I'm currently calculating the average twice, I'd like to rewrite my current solution to use a Common Table Expression:**

**I'd like to include the sales_price, the min, the max and the average on this CTE, and then query my CTE for the result I want.**

Work towards this solution:

```sql
WITH sales_details AS (
  SELECT
  sales_price,
  (SELECT MIN(sales_price) FROM sales) AS min,
  (SELECT MAX(sales_price) FROM sales) AS max,
  ROUND((SELECT AVG(sales_price) FROM sales), 2) AS average
  FROM sales
)
SELECT
  sales_price,
  min,
  max,
  average,
  sales_price - average AS price_diff_from_average
FROM sales_details
ORDER BY price_diff_from_average DESC;
```

### Discuss benefits of this

Encourage students to look at both solutions, can they see any major benefits to the CTE approach?

- Can give the CTE a meaningful name (admittedly aliases could help with this as well) - enhance readability
- CTEs are reusable within a query
- Allow you to break down complex queries into smaller more manageable parts - multiple CTEs stacked up
- Recursion, should you wish 👀

Possible drawbacks:

- can't be used in a separate query, only available for the current query.
