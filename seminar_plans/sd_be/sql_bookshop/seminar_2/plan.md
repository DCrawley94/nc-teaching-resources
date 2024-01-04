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

| course_id | course_name          |
| --------- | -------------------- |
| 1         | Software Development |
| 2         | Data Engineering     |

**JOIN TO**

| student_name | course_id |
| ------------ | --------- |
| Jim          | 1         |
| Poonam       | 2         |
| Lee          | 1         |

**GIVES**

| student_name | course_id | course_name          |
| ------------ | --------- | -------------------- |
| Jim          | 1         | Software Development |
| Poonam       | 2         | Data Engineering     |
| Lee          | 1         | Software Development |

---

## JOIN Demo

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

## Types of JOIN

### Inner Join

Just
