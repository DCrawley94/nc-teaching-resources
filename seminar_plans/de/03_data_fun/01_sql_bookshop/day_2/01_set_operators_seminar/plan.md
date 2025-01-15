# Plan

**THIS NEEDS MORE COMPLEXITY - THE SIMPLE EXAMPLE ARE TOO SIMPLE**

Figjam: https://www.figma.com/board/UrJfpsiUFCognkYk4sbncl/Set-Operators-1?node-id=0-1&t=gOZ1pgSTbJYgO78D-1

Documentation: https://www.postgresql.org/docs/current/queries-union.html

## Learning Objectives:

- Know that we can combine the results of two queries with set operators
- Know how to use set operators when querying a database

## Intro

Set Operators are something that can be used in SQL. We might also have seen them used with Python sets and elsewhere.

> Can anyone give me some examples of SET operations?

- UNION
- INTERSECT
- EXCEPT

## Types of Set Operations

### UNION

Imagine you have two lists: one of your friends and one of your colleagues. A `UNION` operation would create a single list of everyone you know, ensuring no duplicates.

**SHOW UNION EXAMPLE IN VSCODE**

```sql
SELECT * FROM my_fruit_bowl
UNION
SELECT * FROM tropical_fruits;
```

### INTERSECT

Think of the same two lists. `INTERSECT` would give you only the people who are both your friends and colleagues.

**SHOW INTERSECT EXAMPLE IN VSCODE**

```sql
SELECT * FROM my_fruit_bowl
INTERSECT
SELECT * FROM tropical_fruits;
```

### EXCEPT

If you want to know which of your friends are not colleagues, you use the `EXCEPT` operator.

**SHOW EXCEPT EXAMPLE IN VSCODE - SHOW EFFECT OF CHANGING ORDER**

```sql
SELECT * FROM my_fruit_bowl
EXCEPT
SELECT * FROM tropical_fruits;
```

## Example Queries

```sql
-- 1: Get a list of all unique names of
--  employees and contractors.
\! echo "\nUnique Employees and Contractors:\n"

SELECT name FROM employees
UNION
SELECT name FROM contractors;

-- 2: Get a combined list of all names of employees
--  and contractors including duplicates.
\! echo "\nAll Employees and Contractors:\n"

SELECT name FROM employees
UNION ALL
SELECT name FROM contractors;

-- 3: Find the names of people who are both
--  employees and contractors.
\! echo "\nPeople who are both Employees and Contractors:\n"

SELECT name FROM employees
INTERSECT
SELECT name FROM contractors;

-- 4: List all employees who are not contractors
\! echo "\nEmployees who are not Contractors:\n"

SELECT name FROM employees
EXCEPT
SELECT name FROM contractors;

-- 5: List all contractors who are not employees
\! echo "\nContractors who are not Employees:\n"

SELECT name FROM contractors
EXCEPT
SELECT name FROM employees;

-- 6: List unique departments represented in both
--  employees and contractors
\! echo "\nUnique departments across both Employees and Contractors:\n"

SELECT department FROM employees
UNION
SELECT department FROM contractors;

-- 7: Find departments common to both employees
--  and contractors
\! echo "\nCommon departments across Employees and Contractors:\n"

SELECT department FROM employees
INTERSECT
SELECT department FROM contractors;

-- 8: List departments that have employees but
--  no contractors
\! echo "\nDepartments that have Employees and *no* Contractors:\n"

SELECT department FROM employees
EXCEPT
SELECT department FROM contractors;

-- 9: Combine employee and contractor salaries into
--  a list of unique salaries
\! echo "\nUnique salaries across Employees and Contractors:\n"

SELECT salary FROM employees
UNION
SELECT salary FROM contractors;

-- 10: Find salaries that are the same for both employees
--  and contractors
\! echo "\Matching salaries across Employees and Contractors:\n"

SELECT salary FROM employees
INTERSECT
SELECT salary FROM contractors;
```

## More complex example

Step by step breakdown:

1. How do we get the average salary by department for employees?

```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
```

2. How do we get the average salary be department for contractors?

```sql
SELECT department, AVG(salary) AS avg_salary
FROM contractors
GROUP BY department;
```

3. How do we join them?

- `UNION`

Completed query:

```sql
SELECT department, AVG(salary) AS avg_salary, 'employees' as type
FROM employees
GROUP BY department
UNION
SELECT department, AVG(salary) AS avg_salary, 'contractors' as type
FROM contractors
GROUP BY department;
```

**'employees'/'contractors' as type can be included for clarity**

**can also ask students to round**

## Summary

We've explored how query results can be combined using the different SET operations, starting with example of simple datasets and then finally on a more complex example.

Remember this is not a replacements for anything you've learnt so far but instead a new tool to add to your toolbox.
