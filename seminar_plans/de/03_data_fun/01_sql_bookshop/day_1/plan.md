# Plan

Figjam: https://www.figma.com/board/uga79tuoPZQczFxrTm9Kqd/SQL-Bookshop-Day-1?node-id=0-1&t=0bnVimPC9qemZaUn-1

## Learning Objectives

- Understand how to create a table and insert data into it.
- Use conditional clauses to query, update and delete said table.

## Recap

**What is SQL?**

- Structured Query Language.
- Programming language for storing and processing information in a relational database.

**What is a Relational Database?**

- Stores information in a tabular format.
- rows and columns representing different data attributes and the relationships between the values.

## Part 1 - Table Creation

Show the ERD and ask students to guide me through the creation of the database tables:

```sql
DROP DATABASE IF EXISTS animal_crimes;
CREATE DATABASE animal_crimes;

\c animal_crimes

CREATE TABLE bear_crimes(
  crime_id SERIAL PRIMARY KEY,
  crime_description VARCHAR(100) NOT NULL
);

CREATE TABLE bears(
    bear_id SERIAL PRIMARY KEY,
    bear_name VARCHAR(40) NOT NULL,
    bear_description VARCHAR(100),
    danger_rating INT,
    crime_id INT REFERENCES bear_crimes ON DELETE CASCADE
);

CREATE TABLE cat_crimes(
  crime_id SERIAL PRIMARY KEY,
  crime_description VARCHAR(100) NOT NULL
);

CREATE TABLE cats (
  cat_id SERIAL PRIMARY KEY,
  cat_name VARCHAR(40) NOT NULL,
  cat_description VARCHAR(100),
  danger_rating INT,
  crime_id INT REFERENCES cat_crimes ON DELETE CASCADE
);
```

```sql
INSERT INTO bear_crimes
  (crime_description)
VALUES
  ('Gross mischief'),
  ('Foul language'),
  ('Thievery'),
  ('Practicing magic without a license'),
  ('Selling counterfeit marmalade');


INSERT INTO bears(bear_name, bear_description, danger_rating, crime_id)
VALUES
    ('Paddington', 'Looks cute but will destroy everything you own with his neglectful silliness',9,5),
    ('Sooty', 'Suspiciously quiet/ hiding something',5, 2),
    ('Yogi', 'Notorious Picnic thief',7, 3 ),
    ('Pooh','Would sell his own Granny for a pot of honey',6, 3),
    ('The Care Bears', 'One of the most dangerous gangs operating in the Kingdom of Caring',9, 4),
    ('Baloo', 'Enlists humans to do his bidding',8, 3),
    ('Fozzie Bear', 'Do not trust a word he says Waka waka',7, NULL);


INSERT INTO cat_crimes
  (crime_description)
VALUES
  ('White collar crime'),
  ('Grand Theft Lasagne'),
  ('Extreme Sass'),
  ('Practicing magic without a license'),
  ('Gross mischief');


INSERT INTO cats (cat_name, cat_description, danger_rating, crime_id)
VALUES
    ('Salem', 'Sassy magical house cat banished from the world of magic', 7, 4),
    ('Nyan Cat', 'Irritating but fabulous, heart of gold',5, 5),
    ('Scar', 'Scary intimidating all round bad guy, uncle of Simba', 9 , 3),
    ('Jess','Postman Pat''s longtime companion',6, NULL),
    ('Top Cat', 'A streetwise wily feline who always managed to outwit his nemesis, Officer Dibble', 9, 3),
    ('Garfield', 'Hates Mondays, loves Lasagne', 8, 2),
    ('Snagglepuss', 'A light pink anthropomorphic puma wearing a bow tie', 7, 1);
```

## Query Solutions:

```sql
-- This file contains queries on the Animal Crimes Database

\c animal_crimes

-- Fetch the data for all cats in the DB
\! echo "\nAll Cats:\n"
SELECT * FROM cats;
```

```sql
-- Fetch cats with a danger rating higher than 8
\! echo "\nDangerous Cats:\n"
SELECT * FROM cats
WHERE danger_rating >= 8;
```

```sql
-- What is the name and description of the bear who has committed the crime of "Foul language"?
\! echo "\nRude Bear:\n"
SELECT bear_name, bear_description FROM bears
JOIN bear_crimes ON bears.crime_id = bear_crimes.crime_id
WHERE crime_description = 'Foul language';
```

```sql
-- Fetch data for bears who have been 'Practicing magic without a license'
\! echo "\nMagic Bears:\n"
SELECT * FROM bears
JOIN bear_crimes
ON bears.crime_id = bear_crimes.crime_id
WHERE crime_description = 'Practicing magic without a license';
```

```sql
-- What is the description of the least dangerous cat?
\! echo "\nLeast Dangerous Cat:\n"
SELECT * FROM cats
ORDER BY danger_rating ASC
LIMIT 1;
```

**This is a weird one, worth showing the [documentation](https://www.postgresql.org/docs/17/sql-update.html) for UPDATE**

```sql
-- Update danger_rating of cats who have committed 'Grand Theft Lasagne' to be 10
\! echo "\nUpdating Dangerous Cat:\n"
UPDATE cats
SET danger_rating = 10
FROM cat_crimes
WHERE cats.crime_id = cat_crimes.crime_id
  AND cat_crimes.crime_description = 'Grand Theft Lasagne';
```

```sql
--Delete bears with a danger rating lower than 7

-- Can talk about how it would be a good idea to check the rows that are going to be deleted with a SELECT first
\! echo "\nRemoving Dangerous Cats:\n"
DELETE FROM cats
WHERE danger_rating > 7;
```
