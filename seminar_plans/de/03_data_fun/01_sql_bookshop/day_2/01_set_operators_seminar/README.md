# More SQL

This seminar requires pre-made:

- a database (drop then create)
- two tables
- data populated in two tables
- a venv to run the sql within (psql -f <file name>)

The two tables need to be similar enough that the data has overlaps. E.g. two tables of staff data where one has new staff info. Or employees/contractor, vendor/customer
Importantly they must contain some columns that contain the same data type.

Don't necessarily need the same column names but the queries need to be "union compatible"

- same num of columns
- compatible data types in corresponding columns

Recommendation: start with two identical table structures to make the queries easier to digest.
Such as:

```sql
CREATE TABLE june_staff(
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    surname VARCHAR(50),
    title VARCHAR(20) NOT NULL
);

CREATE TABLE mar_staff(
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    surname VARCHAR(50),
    title VARCHAR(20) NOT NULL
);

```

Then when students are comfy with the basics of the operators introduce changes to demo the 'union compatibility' requirements. So June staff turns into:

```sql
CREATE TABLE june_staff(
    staff_id SERIAL PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    surname VARCHAR(50),
    seminar_grp INT,
    job_role VARCHAR(20) NOT NULL
);
```

This should show that the columns need to be equivalent but not the same name and also should break `SELECT *` statements to show same num of columns are needed.

## INTRO

Walk through existing code - dropping and creating db, creating table + columns, inserting values.

## SET OPERATORS

Introduce the idea of set operators which join the result of two or more queries together into one table.

Different to a JOIN because we are doing two separate queries and 'gluing' them together whereas a JOIN joins columns of two or more related tables.

There does not have to be a relation here, just a common structure in the resultant columns from the query.
Queries must return:

- Same num of columns
- compatible data types in respective columns

## UNION

Glues two query results together and eliminates duplicates.
e.g.

```sql
SELECT * FROM june_staff UNION SELECT * FROM mar_staff;
```

This union has technically brought back all the unique rows.

Q: how are they unique?
The staff_id is making it unique.

We can exclude it from our select and select specific columns

```sql

SELECT first_name, surname, title FROM june_staff UNION SELECT first_name, surname, title FROM mar_staff;
```

NOTE: order of returned rows is not guaranteed it's just coincidence

We can bring duplicates back in using `ALL`

```sql

SELECT first_name, surname, title FROM june_staff UNION ALL SELECT first_name, surname, title FROM mar_staff;
```

## INTERSECT

Returns all rows present in query1 and in query2, eliminates duplicates.

## EXCEPT

Returns all rows present in query1 (left) but not in query2 (right) (the difference), eliminates duplicates.

Switch the queries around and get students to guess output.

## <operator> ALL

Can use ALL to include duplicates. Often we'll see UNION ALL but it can be used with EXCEPT and INTERSECT too.

## Change a table to be different

Extra column first. Show how the extra column breaks the 'union compatibility' when we do select\* now.

```sql

CREATE TABLE june_staff(
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    surname VARCHAR(50),
    seminar_grp INT,
    title VARCHAR(20) NOT NULL
);
```

Different named column second. Show how column names don't have an impact here

```sql
CREATE TABLE june_staff(
    staff_id SERIAL PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    surname VARCHAR(50),
    title VARCHAR(20) NOT NULL
);
```

Different data type e.g. title is boolean for some unknown reason in one of the tables.
e.g.

```sql


CREATE TABLE june_staff(
    staff_id SERIAL PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    surname VARCHAR(50),
    title BOOLEAN NOT NULL
);

INSERT INTO june_staff
  (firstname, surname, title)
VALUES
  ('Alex', 'Swain', true),
  ('Carrie', 'Platten',true),
  ('Eli', 'Wiggins', true),
  ('Kyle', 'McPhail',true),
  ('Mick', 'Fay',true);


INSERT INTO mar_staff
  (first_name, surname, title)
VALUES
  ('Alex', 'Swain', 'M'),
  ('Liam', 'Greenfield', 'CL'),
  ('Mick', 'Fay', 'M'),
  ('Kyle', 'McPhail','M'),
  ('Chon', 'Lee', 'M');


```

## Optional: order of evaluation.

Might be an opportunity for students to guess the order of execution. For example which queries does the except statement work on and which one does the Union work on in the first example. Get them used to the idea of the queries being evaluated in a order (brackets) by showing them and do another guess with them.

We can chain operators e.g.

```sql

query1 UNION query2 EXCEPT query3

```

Which will evaluate too...

```sql

(query1 UNION query2) EXCEPT query3

```

(BTW use of brackets is valid psql syntax, but it is just for demo here)

e.g. selecting all the staff from both tables who weren't a mentor in the june cohort.

```sql

SELECT firstname, surname, job_role FROM mar_staff UNION SELECT first_name, surname, title FROM june_staff EXCEPT SELECT first_name, surname, title FROM june_staff WHERE title='M';

```

Or
INTERSECT binding more tightly

```sql

query1 UNION query2 INTERSECT query3

```

Being equivalent to

```sql

query1 UNION (query2 INTERSECT query3)

```

E.g. Selecting the staff who worked only on June cohort and are a SL

```sql

SELECT first_name, surname, title FROM june_staff WHERE title='SL' EXCEPT SELECT firstname, surname, job_role FROM mar_staff INTERSECT SELECT first_name, surname, title FROM june_staff;
```
