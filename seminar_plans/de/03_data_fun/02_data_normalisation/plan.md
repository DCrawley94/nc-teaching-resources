# 1nf and Q+A

## 1 NF

Work through an example of 1nf with unnest/string_to_array or similar

Key problem:

**Nested Data**

Solution:

```sql
CREATE TABLE students_1NF AS (
    SELECT student_id, student_name, UNNEST(STRING_TO_ARRAY(courses, ', ')) AS course, age
    FROM students
);


ALTER TABLE students_1NF
ADD PRIMARY KEY(student_id, course);


SELECT * FROM students_1NF;

```

## 2 NF

What is the issue with our data that means it's not in second normal form?

subject column does not depend on the primary key!

Therefore we should extract subject in some way.

---

Solution:

First lets pull out the keys that are fine as is:

```sql
CREATE TABLE nc_student_2NF AS (
    SELECT DISTINCT student_no, mentor, classroom
    FROM nc_classroom_1NF
);
```

And add the primary key constraint back in:

```sql
ALTER TABLE nc_student_2NF
ADD PRIMARY KEY (student_no);
```

Next let's extract the column causing the issues into it's own table:

```sql
CREATE TABLE nc_student_subject_2NF AS (
    SELECT student_no, subject
    FROM nc_classroom_1NF
);
```

Currently this does not have a primary key or a foreign key.

What can we use for the primary key? - lead them to the idea of composite keys if their struggling

What shall we use for the foreign key? - student no

```sql
ALTER TABLE nc_student_subject_2NF
ADD PRIMARY KEY (student_no, subject),
ADD FOREIGN KEY (student_no) REFERENCES nc_student_2NF(student_no);
```

And check:

```sql
SELECT * FROM nc_student_2NF;
SELECT * FROM nc_student_subject_2NF;
```

Example query:

```sql
SELECT nc_student_2NF.student_no, mentor, classroom
FROM nc_student_2NF
JOIN nc_student_subject_2NF
    ON nc_student_2NF.student_no = nc_student_subject_2NF.student_no
WHERE subject = 'English';
```

## 3 NF

We can see that the `classroom` is not directly related to the `student_id` - in fact the `classroom` number is set by the `mentor` and the mentor is set by the `student_id` . What this means is that the classroom is **transitively dependant** on the `student_id`!

Solution:

Extract the source of the transitive dependency - can use mentor as a foreign key in this case (assume no mentors with the same name)

```sql
CREATE TABLE nc_mentors_3NF AS (
    SELECT DISTINCT mentor, classroom
    FROM nc_students_2NF
);

ALTER TABLE nc_mentors_3NF
ADD PRIMARY KEY (mentor);
```

Extract student data from 2NF table - keeping mentor to serve as foreign key

```sql
CREATE TABLE nc_students_3NF AS (
    SELECT student_id, mentor
    FROM nc_students_2NF
);

ALTER TABLE nc_students_3NF
ADD PRIMARY KEY (student_id),
ADD FOREIGN KEY (mentor) REFERENCES nc_mentors_3NF(mentor);
```

The `student_subjects` table is identical to 2NF table, could just update the constraints on the old one to point to new tables but lets just create a completely new table for clarity:

```sql
CREATE TABLE student_subjects_3NF AS (
    SELECT * FROM student_subjects_2NF
);

ALTER TABLE student_subjects_3NF
ADD PRIMARY KEY (student_id, subject),
ADD FOREIGN KEY (student_id) REFERENCES nc_students_3NF(student_id);
```

Checks:

```sql
SELECT * FROM nc_mentors_3NF;
SELECT * FROM nc_students_3NF;
SELECT * FROM student_subjects_3NF;
```

Example query:

```sql
SELECT nc_students_3NF.student_id, nc_mentors_3NF.mentor, classroom
FROM nc_students_3NF
JOIN student_subjects_3NF
    ON nc_students_3NF.student_id = student_subjects_3NF.student_id
JOIN nc_mentors_3NF
    ON nc_mentors_3NF.mentor = nc_students_3NF.mentor
WHERE subject = 'English';
```
