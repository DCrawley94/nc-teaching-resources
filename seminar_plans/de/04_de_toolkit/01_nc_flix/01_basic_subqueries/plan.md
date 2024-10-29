# Bear Crimes

# ❗ **THIS SEMINAR WAS DONE IN 40 MINUTES - ADD MORE COMPLEX TASKS AS A BACKUP** ❗

https://www.figma.com/board/H0W89WCAEKGlUZheGGtm4f/Subqueries?node-id=0-1&t=j5NbBz1jAfD57tj7-1

## Learning Objectives

- Know how to use some advanced SQL tools such as CASE/WHEN and subqueries.
- Know some of the different types of subqueries available to us.
- Know how to write SQL queries that make use of subqueries.

## Intro what is a subquery?

- simply defined as a query within another query

## Tasks

The Animal Crimes division of the FBI (Furry Bureau of Investigation) have asked
us to help investigate some dangerous criminal masterminds. In order to find
these fluffy menaces we will need to find the following -

### 1

- Get the average danger_rating of all bears.
- Round this to 2 decimal places

```sql
SELECT ROUND(AVG(danger_rating), 2) from bears;
```

### 2

- Using a subquery to get a list of all bears that are more dangerous than Pooh

```sql
SELECT bear_name, danger_rating FROM bears
WHERE danger_rating > (
    SELECT danger_rating from bears WHERE bear_name = 'Pooh'
);
```

### 3

- Using a subquery select information about only the bears with a danger_rating greater than the average.

```sql
SELECT bear_name, danger_rating FROM bears
WHERE danger_rating > (
    SELECT AVG(danger_rating) from bears
);
```

### 4

- Write a query that will retrieve the bears and assign them a danger level based on their danger rating.
  - > 'not dangerous': danger_rating of 6 or less
  - > 'dangerous': danger_rating of 7 or 8
  - > 'very dangerous': danger_rating of 9 or above

```sql
SELECT
    bear_name,
    danger_rating,
    CASE
        WHEN danger_rating <= 6 THEN 'not dangerous'
        WHEN danger_rating < 9 THEN 'dangerous'
        ELSE 'very dangerous'
    END as danger_level
FROM bears;
```

### 5

- Refactor the above to use a subquery.
  - This time bears with an above average danger_rating should be classed as 'very dangerous' and those with a below average rating should be classed as 'not dangerous'.

```sql
SELECT
    bear_name,
    danger_rating,
    CASE
        WHEN danger_rating > (SELECT AVG(danger_rating) FROM bears) THEN 'very dangerous'
        ELSE 'not dangerous'
    END
FROM bears;
```

---

## BREAK

Switch back to Figjam and discuss different types of subquery:

We saw a couple of different types of subquery this morning. What were they?

- single value: Scalar subquery
- multi-row: One column with multiple rows OR multiple columns and multiple rows

---

## Extra Multi-Row Subquery

- Query the database to find the crimes committed by all the bears that have an above average danger rating **without** using a JOIN.

```sql
SELECT crime_description FROM crimes
WHERE crime_id IN (
    SELECT crime_id FROM bears
    WHERE danger_rating > (SELECT AVG(danger_rating) FROM bears)
);
```

## Questions

- What kind of subquery have we seen here?
  - scalar (single row)
  - multi row
