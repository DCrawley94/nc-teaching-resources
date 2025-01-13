DROP DATABASE IF EXISTS northcoders_test;
CREATE DATABASE northcoders_test;

\c northcoders_test;

CREATE TABLE june_staff(
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    surname VARCHAR(50),
    seminar_grp INT,
    title VARCHAR(20) NOT NULL
);

CREATE TABLE mar_staff(
    staff_id SERIAL PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    surname VARCHAR(50),
    job_role VARCHAR(20) NOT NULL
);


INSERT INTO june_staff
  (first_name, surname, seminar_grp, title)
VALUES
  ('Alex', 'Swain', 1, 'M'),
  ('Carrie', 'Platten', 1, 'M'),
  ('Eli', 'Wiggins', 2, 'SL'),
  ('Kyle', 'McPhail',2 , 'M'),
  ('Mick', 'Fay', 2, 'M');


INSERT INTO mar_staff
  (firstname, surname, job_role)
VALUES
  ('Alex', 'Swain', 'M'),
  ('Liam', 'Greenfield', 'CL'),
  ('Mick', 'Fay', 'M'),
  ('Kyle', 'McPhail','M'),
  ('Chon', 'Lee', 'M');


-- SELECT firstname, surname, job_role FROM mar_staff UNION SELECT first_name, surname, title FROM june_staff;

