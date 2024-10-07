-- DO NOT CHANGE THIS CODE

DROP DATABASE IF EXISTS normalisationsql;
CREATE DATABASE normalisationsql;

\c normalisationsql;

CREATE TABLE nc_students_2NF
(
    student_id INT PRIMARY KEY,
    mentor VARCHAR,
    classroom VARCHAR
);

CREATE TABLE student_subjects_2NF
(
    student_id INT,
    subject VARCHAR,
    PRIMARY KEY (student_id, subject),
    FOREIGN KEY (student_id) REFERENCES nc_students_2NF(student_id)
);

INSERT INTO nc_students_2NF (student_id, mentor, classroom)
VALUES
('10456', 'Rose', 'Zoom_12'),
('10839', 'Haz', 'Zoom_08'),
('10931', 'Rose', 'Zoom_12'),
('11525', 'Liam', 'Zoom_15'),
('12633', 'Haz', 'Zoom_08');

INSERT INTO student_subjects_2NF (student_id, subject)
VALUES
('10456','Maths'),
('10456','Science'),
('10456','English'),
('10839','English'),
('10839', 'Art'),
('10839', 'P.E.'),
('10931', 'Music'),
('10931', 'French'),
('10931', 'Business'),
('11525', 'I.T.'),
('11525', 'Art'),
('12633', 'Science'),
('12633', 'P.E.'),
('12633', 'I.T.');

SELECT * FROM nc_students_2NF;
SELECT * FROM student_subjects_2NF;

-- CREATE NEW TABLES HERE:

