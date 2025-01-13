-- This file contains queries on the Animal Crimes Database

\c animal_crimes

-- Fetch the data for all cats in the DB
SELECT * FROM cats;

-- Fetch data for bears who have been 'Practicing magic without a license'
SELECT * FROM bears
JOIN bear_crimes 
ON bears.crime_id = bear_crimes.crime_id
WHERE crime_description = 'Practicing magic without a license';

-- Fetch cats with a danger rating higher than 8

SELECT * FROM cats
WHERE danger_rating >= 8;

-- What are the names and danger ratings of all bears in the DB?

SELECT bear_name, danger_rating FROM bears;

-- What is the description of the least dangerous cat?

SELECT * FROM cats
ORDER BY danger_rating ASC
LIMIT 1;

--Update danger_rating of cats who have committed 'Grand Theft Lasagne' to be 10

UPDATE cats
SET danger_rating = 10
FROM cat_crimes
WHERE cats.crime_id = cat_crimes.crime_id
  AND cat_crimes.crime_description = 'Grand Theft Lasagne';

SELECT * FROM cats;



--Delete bears with a danger rating lower than 7 

-- What is the name and description of the bear who has committed the crime of Foul Language?