\c bear_crimes


-- Get the average danger_rating of all bears.
-- Round this to 2 decimal places
\! echo "\nAverage danger rating:\n"

SELECT ROUND(AVG(danger_rating), 2) from bears;



-- Using a subquery to get a list of all bears that are more dangerous than Pooh
\! echo "\nBears more dangerous than Pooh:\n"

SELECT bear_name, danger_rating FROM bears
WHERE danger_rating > (
    SELECT danger_rating from bears WHERE bear_name = 'Pooh'
);



-- Using a subquery select information about only the bears with a danger_rating greater than the average.
\! echo "\nBears with a greater than average danger rating:\n"

SELECT bear_name, danger_rating FROM bears
WHERE danger_rating > (
    SELECT AVG(danger_rating) from bears
);



-- Write a query that will retrieve the bears and assign them a danger level based on their danger rating.  
-- >> 'not dangerous': danger_rating of 6 or less
-- >> 'dangerous': danger_rating of 7 or 8
-- >> 'very dangerous': danger_rating of 9 or above
\! echo "\nAssigning bears a danger level:\n"

SELECT 
    bear_name,
    danger_rating,
    CASE 
        WHEN danger_rating <= 6 THEN 'not dangerous'
        WHEN danger_rating < 9 THEN 'dangerous'
        ELSE 'very dangerous'
    END as danger_level
FROM bears;



-- Refactor the above to use a subquery. 
-- >> This time bears with an above average danger_rating should be classed as 'very dangerous' and those with a below average rating  should be classed as 'not dangerous'.
\! echo "\nDanger level refactor:\n"

SELECT
    bear_name,
    danger_rating,
    CASE
        WHEN danger_rating > (SELECT AVG(danger_rating) FROM bears) THEN 'very dangerous'
        ELSE 'not dangerous'
    END
FROM bears;



-- Query the database to find the crimes committed by all the bears that have an above average danger rating WITHOUT using a JOIN.
\! echo "\nDangerous Bear Crimes:\n"

SELECT crime_description FROM crimes
WHERE crime_id IN (
    SELECT crime_id FROM bears
    WHERE danger_rating > (SELECT AVG(danger_rating) FROM bears)
);


--Scalar subqueries - exactly 1 row and column
SELECT 
    bear_name AS bear, 
    danger_rating, 
    (
        SELECT ROUND(AVG(danger_rating)::NUMERIC, 2) 
        FROM bears
    ) AS avg_danger_rating 
FROM bears;
