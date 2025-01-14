DROP DATABASE IF EXISTS set_operators_example;
CREATE DATABASE set_operators_example;

\c set_operators_example;

CREATE TABLE employees (
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

CREATE TABLE contractors (
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

INSERT INTO employees (name, department, salary)
VALUES
('Alice', 'Engineering', 75000),
('Bob', 'Marketing', 60000),
('Charlie', 'Engineering', 72000),
('Diana', 'HR', 50000),
('Eve', 'Marketing', 58000);

INSERT INTO contractors (name, department, salary)
VALUES
('Frank', 'Engineering', 70000),
('Grace', 'Marketing', 60000),
('Charlie', 'Engineering', 72000),
('Diana', 'Finance', 55000),
('Hank', 'Engineering', 75000);
