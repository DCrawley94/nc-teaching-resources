DROP DATABASE IF EXISTS animal_crimes;
CREATE DATABASE animal_crimes;

\c animal_crimes

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

CREATE TABLE cat_crimes(
  crime_id SERIAL PRIMARY KEY,
  crime_description VARCHAR(100) NOT NULL
);

INSERT INTO cat_crimes
  (crime_description)
VALUES
  ('White collar crime'),
  ('Grand Theft Lasagne'),
  ('Extreme Sass'),
  ('Practicing magic without a license'),
  ('Gross mischief');


CREATE TABLE cats (
  cat_id SERIAL PRIMARY KEY,
  cat_name VARCHAR(40) NOT NULL,
  cat_description VARCHAR(100),
  danger_rating INT,
  crime_id INT REFERENCES cat_crimes ON DELETE CASCADE
);

INSERT INTO cats (cat_name, cat_description, danger_rating, crime_id)
VALUES
    ('Salem', 'Sassy magical house cat banished from the world of magic', 7, 4),
    ('Nyan Cat', 'Irritating but fabulous, heart of gold',5, 5),
    ('Scar', 'Scary intimidating all round bad guy, uncle of Simba', 9 , 3),
    ('Jess','Postman Pat''s longtime companion',6, NULL),
    ('Top Cat', 'A streetwise wily feline who always managed to outwit his nemesis, Officer Dibble', 9, 3),
    ('Garfield', 'Hates Mondays, loves Lasagne', 8, 2),
    ('Snagglepuss', 'A light pink anthropomorphic puma wearing a bow tie', 7, 1);

-- Union/Intersect/Except

SELECT crime_description 
FROM crimes
INTERSECT
SELECT crime_description
FROM cat_crimes;

-- Case
SELECT bear_name,
  CASE 
    WHEN danger_rating <= 6 THEN 'not dangerous'
    WHEN danger_rating <= 8 THEN 'dangerous'
    ELSE 'very dangerous'
  END danger_level FROM bears ORDER BY danger_rating DESC;

--Aggregate Queries if time

SELECT bear_name, crime_description AS crime FROM bears JOIN crimes ON bears.crime_id = crimes.crime_id;
SELECT cats.cat_name, cat_crimes.crime_description FROM cats JOIN cat_crimes ON cats.crime_id = cat_crimes.crime_id;