# Plan

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

### INTERSECT

Think of the same two lists. `INTERSECT` would give you only the people who are both your friends and colleagues.

**SHOW INTERSECT EXAMPLE IN VSCODE**

### EXCEPT

If you want to know which of your friends are not colleagues, you use the `EXCEPT` operator.

**SHOW EXCEPT EXAMPLE IN VSCODE - SHOW EFFECT OF CHANGING ORDER**

## Example Queries

## Outro

The project members table could maybe be improved.

What is the relationships between employees and projects
