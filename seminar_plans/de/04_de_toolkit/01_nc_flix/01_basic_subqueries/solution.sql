-- Subquery

SELECT * FROM bears
WHERE danger_rating > (SELECT danger_rating FROM bears WHERE bear_name = 'Sooty');

--Aggregate

SELECT AVG(danger_rating) FROM bears;
SELECT ROUND(AVG(danger_rating), 2) FROM bears;

--Subquery with Aggregate - combines first 2

SELECT * FROM bears
WHERE danger_rating > (SELECT ROUND(AVG(danger_rating), 2) FROM bears;)

--CASE/WHEN

SELECT bear_id, danger_rating, 
CASE 
WHEN danger_rating <= 6 THEN 'not dangerous'
WHEN danger_rating <= 8 THEN 'dangerous'
ELSE 'very dangerous'
END danger_level FROM bears ORDER BY danger_level DESC;

--CASE/WHEN with subqueries & aggregate

SELECT bear_id, danger_rating, 
CASE 
WHEN danger_rating <= (SELECT AVG(danger_rating) AS average from bears) 
THEN 'not dangerous'
ELSE 'very dangerous'
END danger_level FROM bears ORDER BY danger_level DESC;

--Scalar subqueries - exactly 1 row and column
SELECT bear_name AS bear, danger_rating, (SELECT ROUND(AVG(danger_rating)::NUMERIC, 2) FROM bears) AS avg_danger_rating FROM bears;
