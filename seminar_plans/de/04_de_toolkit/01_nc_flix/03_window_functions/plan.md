# Window Functions Seminar

## Intro

**What is a Window Function?**

A window function is a type of SQL function that performs calculations across a set of rows related to the current row, known as a "window." Unlike regular aggregate functions (like SUM or COUNT), which reduce multiple rows into a single result, window functions keep each row in the output while performing a calculation across a specific range of rows.

## Task 1

### Solution

```sql
SELECT
    sales_period,
    album_title,
    artist_name,
    copies_sold,
    SUM(copies_sold) OVER() AS sold_in_4Q_2022
FROM album_catalogue
JOIN artists ON artists.artist_id = album_catalogue.artist_id
JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id
WHERE sales_period = '2022_4Q';
```

In this query, we’re using a window function to calculate the total number of copies sold for the 2022_4Q period, and we’re displaying that total in a new column, sold_in_4Q_2022, for each row of our result.

**How This Window Function Works in the Query**
Let’s look specifically at the `SUM(copies_sold) OVER()` part:

- `SUM(copies_sold)`: This part calculates the sum of the copies_sold column.
- `OVER()`: This part is what makes it a window function. When we use OVER() without any additional specification, it means that the window includes all the rows in the result after filtering for 2022_4Q.

**Step-by-Step Breakdown**
Here’s how the window function works step-by-step in this query:

- Filtering Rows: The `WHERE sales_period = '2022_4Q'` clause filters the data to include only rows from the fourth quarter of 2022.

- Calculating the Sum: `SUM(copies_sold) OVER()` calculates the total of copies_sold for all rows that passed the filter (all rows in 2022_4Q). Importantly, it calculates this total once for the filtered data set.

- Displaying the Total: The total copies sold is shown in the `sold_in_4Q_2022` column for each row. Even though each row represents an individual album, the total number of copies sold across all albums in 2022_4Q is repeated in this column for every row.

### Horrible Alternative Subquery/CTE

Students may take us down this route. Or I can do it to show as an alternative but it is not ideal.

```sql
SELECT
    sales_period,
    album_title,
    artist_name,
    copies_sold,
    (
        SELECT SUM(copies_sold)
        FROM album_catalogue
        JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id
        WHERE sales_period = '2022_4Q') AS total_copies_sold
FROM album_catalogue
JOIN artists ON artists.artist_id = album_catalogue.artist_id
JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id
WHERE sales_period = '2022_4Q';
```

```sql
WITH total_sold AS (
    SELECT SUM(copies_sold) AS sold_in_4Q_2022
    FROM album_catalogue
    JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id
    WHERE sales_period = '2022_4Q'
)
SELECT
    sales_period,
    album_title,
    artist_name,
    copies_sold,
    (SELECT sold_in_4Q_2022 FROM total_sold) AS sold_in_4Q_2022
FROM album_catalogue
JOIN artists ON artists.artist_id = album_catalogue.artist_id
JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id
WHERE sales_period = '2022_4Q';
```

## Task 2

### Solution

```sql
SELECT
    sales_period,
    album_title,
    artist_name,
    copies_sold,
    SUM(copies_sold) OVER(ORDER BY sales_period ASC) AS cumulative_sales
FROM album_catalogue
JOIN artists ON artists.artist_id = album_catalogue.artist_id
JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id
WHERE album_title = 'Licensed to Ill';
```

**Understanding `SUM(copies_sold) OVER(ORDER BY sales_period ASC)`**

Let’s break down the window function `SUM(copies_sold) OVER(ORDER BY sales_period ASC)`.

- `SUM(copies_sold)`: This part calculates the sum of the `copies_sold` column, but since it’s inside a window function, it can calculate this sum cumulatively (incrementally) across rows.

- `OVER(ORDER BY sales_period ASC)`:

- The `OVER()` clause tells SQL to treat this as a window function.
- `ORDER BY` sales_period ASC specifies the order in which rows should be considered within this window.
- `ASC` means that we start from the earliest sales period and move forward in time.

By adding `ORDER BY sales_period ASC`, the cumulative total will build up as we move through each sales period in order. For each row, the cumulative total will include all copies sold from the earliest period up to that row's period.

**Purpose of `ORDER BY` in This Window Function**
In window functions, `ORDER BY` controls how the calculation progresses across rows:

- Without `ORDER BY`: The `SUM()` would simply return the same grand total in each row (just like a regular aggregate function).
- With `ORDER BY`: The `SUM()` acts as a cumulative total (running total), recalculating at each row by adding the sales from previous rows in sequence.

---

**GET STUDENTS TO THINK ABOUT WHAT HAPPENS HERE**

Might be beneficial to show that `ORDER BY` can be used as normal outside the window function. But this doesn't effect the running total:

```sql
SELECT
    sales_period,
    album_title,
    artist_name,
    copies_sold,
    SUM(copies_sold) OVER(ORDER BY sales_period ASC) AS cumulative_sales
FROM album_catalogue
JOIN artists ON artists.artist_id = album_catalogue.artist_id
JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id
WHERE album_title = 'Licensed to Ill'
ORDER BY copies_sold;
```

## Task 3

### Solution

```sql
SELECT
    album_title,
    artist_name,
    copies_sold,
    album_genre,
    SUM(copies_sold) OVER(PARTITION BY album_genre)
FROM album_catalogue
JOIN artists ON artists.artist_id = album_catalogue.artist_id
JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id
WHERE sales_period = '2022_4Q';
```

---

**Understanding SUM(copies_sold) OVER(PARTITION BY album_genre)**
The key part of the query here is the window function:

- `SUM(copies_sold)`: This part calculates the sum of `copies_sold` within each genre.
- `OVER(PARTITION BY album_genre)`: This part tells SQL to calculate the sum within groups, where each group consists of rows with the same `album_genre`.

When we use `PARTITION BY`, the window function calculates a separate total for each unique `album_genre`. So each genre has its own "partition," or subset, in the result. Each row within a genre partition will display the total sales for that genre, while still keeping its individual album’s sales data.

**Purpose of `PARTITION BY` in This Window Function**
The `PARTITION BY` clause in the window function essentially divides the data into groups based on the value in the `album_genre` column. The `SUM` is then calculated within each of these groups instead of across the entire result set.

Without `PARTITION BY`, `SUM(copies_sold) OVER()` would calculate a single grand total for `copies_sold` across all rows in `2022_4Q`. However, `PARTITION BY album_genre` limits the sum to each genre, so that each album in the same genre shows the total sales for that genre only.

**Key Takeaways for Students**

- Window functions with PARTITION BY create grouped calculations (totals, averages, etc.) while preserving each row individually.
- PARTITION BY divides the rows into groups (partitions) based on a column (in this case, album_genre). Each partition has its own calculation.
- This approach is useful for categorical aggregations: you can get total, average, or other metrics for each category without collapsing rows.

Using PARTITION BY in a window function is perfect when you want grouped totals or other aggregations without combining rows into a single row per group. It provides both individual row detail and group-level context in one result set.

## Task 4

### Solution

```sql
WITH album_details AS (
    SELECT DISTINCT
        album_title,
        album_length
    FROM album_catalogue
)
SELECT *,
     RANK() OVER (ORDER BY album_length DESC) AS album_length_rank
FROM album_details
ORDER BY album_length_rank;
```

Students might suggest this:

```sql
SELECT DISTINCT
    album_title,
    album_length,
    RANK() OVER (ORDER BY album_length DESC) AS album_length_rank
FROM album_catalogue;
```

Which gives us wild numbers for the rank due to having multiple albums appearing in the catalogue - first we need to narrow it down to distinct albums.

---

**Talk about `dense_rank` vs `rank`**

## Task 5

### Solution

```sql
SELECT
    sales_period,
    album_title,
    artist_name,
    copies_sold,
    SUM(copies_sold) OVER(PARTITION BY album_title ORDER BY sales_period ASC) AS cumulative_sales_by_genre
FROM album_catalogue
JOIN artists ON artists.artist_id = album_catalogue.artist_id
JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id;
```

**Understanding SUM(copies_sold) OVER(PARTITION BY album_title ORDER BY sales_period ASC)**

This window function includes both PARTITION BY and ORDER BY, each serving a specific purpose:

1. SUM(copies_sold): This part calculates the sum of copies_sold, but since it’s inside a window function, it applies the sum in a cumulative way based on PARTITION BY and ORDER BY.

2. PARTITION BY album_title:

- Divides the rows into partitions, where each partition consists of rows with the same album_title.
- The cumulative sum will be calculated independently within each album’s partition.

3. ORDER BY sales_period ASC:

- Controls the order in which rows are evaluated within each album_title partition.
- By specifying ORDER BY sales_period ASC, the cumulative total starts with the earliest sales period and adds up sales as we progress through time.

This combination of PARTITION BY and ORDER BY produces a cumulative total for each album that builds up over each sales period.

**Purpose of PARTITION BY and ORDER BY Together**

Using both PARTITION BY and ORDER BY is essential for creating cumulative totals that are specific to each album and time-ordered within each album:

- PARTITION BY album_title: Ensures that the cumulative total resets for each album, so we get separate cumulative totals for each album.
- ORDER BY sales_period ASC: Controls the cumulative calculation within each album, so that each row includes all previous sales for that album up to the given sales_period.

Without PARTITION BY, we’d get a single cumulative total across all albums combined. Without ORDER BY, we’d get the same total sales for each album in every row, instead of a running total.

**Key Takeaways for Students**

- PARTITION BY creates a separate cumulative total for each unique album.
- ORDER BY within the window controls the order of calculation, making it a running total over time within each album.
- Together, these clauses allow you to track how sales accumulate over time for each album, providing both row-level detail and an ordered cumulative total.

This approach is great for time-series analysis where you want a running total within specific categories, in this case, each album.

## Task 6

### Solution

```sql
SELECT album_title,
     artist_name,
     copies_sold,
     album_genre,
     SUM(copies_sold) OVER (PARTITION BY album_genre) AS sales_by_genre,
     ROUND((copies_sold::decimal/ SUM(copies_sold) OVER (PARTITION BY album_genre))*100.0, 2) AS percent_of_genre_sales
FROM album_catalogue
JOIN artists ON artists.artist_id = album_catalogue.artist_id
JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id
WHERE sales_period = '2022_2Q'
ORDER BY album_genre, copies_sold DESC;
```
