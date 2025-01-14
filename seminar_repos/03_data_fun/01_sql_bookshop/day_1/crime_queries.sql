-- This file contains queries on the Animal Crimes Database

\c animal_crimes

-- Fetch the data for all cats in the DB
\! echo "\nAll Cats:\n"

SELECT * FROM cats;


-- Fetch cats with a danger rating higher than 8
\! echo "\nDangerous Cats:\n"

SELECT * FROM cats
WHERE danger_rating > 8;


-- What is the name and description of the bear who has 
--      committed the crime of "Foul language"?
\! echo "\nRude Bear:\n"
SELECT bear_name, bear_description
FROM bears
JOIN bear_crimes
ON bears.crime_id = bear_crimes.crime_id
WHERE crime_description = 'Foul language';



-- Fetch data for bears who have been 
--      'Practicing magic without a license'
\! echo "\nMagic Bears:\n"
SELECT bear_name, crime_description
FROM bears
JOIN bear_crimes
ON bears.crime_id = bear_crimes.crime_id
WHERE crime_description = 'Practicing magic without a license';



-- What is the description of the least dangerous cat?
\! echo "\nLeast Dangerous Cat:\n"

SELECT cat_description
FROM cats
ORDER BY danger_rating ASC
LIMIT 1;



-- Update danger_rating of cats who have committed 
--      'Grand Theft Lasagne' to be 10
\! echo "\nUpdating Dangerous Cat:\n"

UPDATE cats
SET danger_rating = 10
FROM cat_crimes
WHERE cats.crime_id = cat_crimes.crime_id
AND crime_description = 'Grand Theft Lasagne';

SELECT * FROM cats;


-- Delete bears with a danger rating lower than 7 
\! echo "\nRemoving Non Dangerous Bears:\n"

DELETE FROM bears
WHERE danger_rating < 7;


SELECT * FROM bears WHERE bear_id = 4;