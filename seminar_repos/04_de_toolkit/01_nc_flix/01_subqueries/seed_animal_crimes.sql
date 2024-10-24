DROP DATABASE IF EXISTS bear_crimes;
CREATE DATABASE bear_crimes;

\c bear_crimes

CREATE TABLE crimes(
  crime_id SERIAL PRIMARY KEY,
  crime_description VARCHAR(100) NOT NULL
);

INSERT INTO crimes
  (crime_description)
VALUES
  ('Gross mischief'),
  ('Foul language'),
  ('Thievery'),
  ('Practicing magic without a license'),
  ('Selling counterfeit marmalade');

CREATE TABLE bears(
    bear_id SERIAL PRIMARY KEY,
    bear_name VARCHAR(40) NOT NULL,
    bear_description VARCHAR(100),
    danger_rating INT,
    crime_id INT REFERENCES crimes ON DELETE CASCADE
);

INSERT INTO bears(bear_name, bear_description, danger_rating, crime_id)
VALUES
    ('Paddington', 'Looks cute but will destroy everything you own with his neglectful silliness',9,5),
    ('Sooty', 'Suspiciously quiet/ hiding something',5, 4),
    ('Yogi', 'Notorious Picnic thief',7, 3 ),
    ('Pooh','Would sell his own Granny for a pot of honey',6, 3),
    ('The Care Bears', 'One of the most dangerous gangs operating in the Kingdom of Caring',9, 4),
    ('Baloo', 'Enlists humans to do his bidding',8, 3),
    ('Fozzie Bear', 'Do not trust a word he says Waka waka',7, NULL);

