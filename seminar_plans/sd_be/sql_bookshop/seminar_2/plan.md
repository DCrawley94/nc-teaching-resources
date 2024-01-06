# Joins and Junction Tables

## Learning Objectives

- Have an understanding of the main types of JOINs
- Know how to query tables with a many to many relationship
- Know how to use some aggregate functions

## Intro to JOINs

Joins:

- Used to combine columns from different tables based on values of common columns between tables
- Typically this means the primary key column of one table and the foreign key column of another

---

EXAMPLE:

Show example data on FIGJAM

Talk about hwo I have data in two tables

A column from films has a foreign key (director_id) that relates to the primary key of the directors table.

Therefore I can use this to _JOIN_ the tables and get the data I'd like - **film name, release_date and director**.

## JOIN Demo

**Show DB Diagram of Database I am using**

Demo how to create a join in the repo:

Describe the task:

We want information about films, their release dates and the film directors.

Talk through the creation of the following query:

```sql
SELECT * FROM films
JOIN directors
ON films.director_id = directors.director_id;
```

Talk about why we need to specify the table for `director_id`.

Show that this has worked, a new table has been created that includes `director_id` and `director_name` from directors table.

Great that it works but a bit too much information, let's narrows it down to the information we actually want:

- films title
- release date
- director name

```sql
SELECT title, release_date, director_name FROM films
JOIN directors
ON films.director_id = directors.director_id;
```

## Discuss Types of JOIN

This is going to be more theoretical - the **SQL Relationships** notes has a link to an online article that will give some nice examples of the later joins in action.

### Inner Join

**This is what the default JOIN is - what we just did**

Selects all rows from both tables as long as join condition is satisfied.

### Left Outer Join

All rows from both tables that match the joining condition are returned.

Also returns all rows from table 1 that don’t satisfy condition.

### Right Outer Join

All rows from both tables that match the joining condition are returned.

Also returns all rows from table 2 that don’t satisfy condition.

### Full Outer Join

All rows from both tables that match the joining condition are returned.

Also returns all the rows from both tables that don’t satisfy the joining condition.

## Many - to - Many relationships

Look at the films table and directors table in txt file.

Talk about the relationship between then and how it is a one-to-many relationship as one director can direct many films.

**Ask students if they could describe how films and actors could be related.**

Talk about how this relationship is many-to-many because films have multiple actors and actors can be in many different films.

**Tell students to have a think about how this relationship could be defined in our database**

**Ask students if they have any ideas how this could be done** - they may have no idea depending on what they saw in the lecture.

Show a representation of the DB on DB Diagram. Talk about how the best way to demonstrate this relationship is with a **Junction Table** to link the two separate tables.

**Junction Table things to mention:**

- Other than the primary key column in only needs two columns
- these columns hold the references the the different tables

## Create Junction Table in VSCode:

Ask student to help write SQL to create the Junction table - refer back to DB Diagram if they get stuck.

Aim to end up with something like this:

```sql
DROP TABLE IF EXISTS film_actors;

CREATE TABLE film_actors (
    film_actor_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES films(film_id),
    actor_id INT REFERENCES actors(actor_id)
)
```

Provide data to insert:

```sql
INSERT INTO film_actors (film_id, actor_id) VALUES
    (1, 1), (1, 2), (1, 3),
    (2, 4), (2, 5), (2, 6),
    (3, 7), (3, 8), (3, 9),
    (4, 10), (4, 11), (4, 12),
    (5, 20), (5, 21), (6, 8),
    (6, 13), (6, 14), (7, 15),
    (7, 16), (7, 17), (8, 4),
    (8, 18), (8, 19), (9, 22);
```

Add in an echo statement so we can see what it looks like:

```sql
\! echo "\nJunction table:"
SELECT * FROM film_actors;
```

## Further queries to show more JOINS an intro Aggregates

1. Select all the films and all the actors using the junction table

```sql
SELECT title, actor_name
FROM film_actors
JOIN films ON films.film_id = film_actors.film_id
JOIN actors ON actors.actor_id = film_actors.actor_id;
```

2. Select all the actors that are not in any movies

```sql
SELECT actor_name
FROM film_actors
JOIN films ON films.film_id = film_actors.film_id
RIGHT OUTER JOIN actors ON actors.actor_id = film_actors.actor_id
WHERE title IS NULL;
```

3. Count the number of actors that have been in a film that has a rating less than 5

```sql
SELECT Count(actor_name) as actor_count
FROM film_actors
JOIN films ON films.film_id = film_actors.film_id
JOIN actors ON actors.actor_id = film_actors.actor_id
WHERE rating < 5;
```

**TRY AND FINISH HERE**

## If asked: GROUP BY

The GROUP BY statement groups rows that have the same values into summary rows, like "find the number of customers in each country"
