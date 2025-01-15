\c set_operators_example;

DROP TABLE IF EXISTS my_fruit_bowl;
DROP TABLE IF EXISTS tropical_fruits;

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

