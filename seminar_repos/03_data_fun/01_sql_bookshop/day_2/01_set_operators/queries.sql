\c set_operators_example;

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
