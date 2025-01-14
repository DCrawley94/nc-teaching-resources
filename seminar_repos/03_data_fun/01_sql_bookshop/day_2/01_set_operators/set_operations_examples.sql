DROP DATABASE IF EXISTS set_operators_example;
CREATE DATABASE set_operators_example;

\c set_operators_example;


CREATE TABLE my_fruit_bowl (
    name TEXT
);

CREATE TABLE tropical_fruits (
    name TEXT
);

INSERT INTO
my_fruit_bowl
VALUES
('Apple'),
('Banana'),
('Plum');

INSERT INTO
tropical_fruits
VALUES
('Banana'),
('Mango'),
('Papaya');

-- ############################ --
