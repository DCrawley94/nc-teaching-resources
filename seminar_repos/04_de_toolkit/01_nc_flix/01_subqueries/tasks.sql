\c bear_crimes


-- Get the average danger_rating of all bears.
-- Round this to 2 decimal places
\! echo "\nAverage danger rating:\n"





-- Using a subquery to get a list of all bears that are more dangerous than Pooh
\! echo "\nBears more dangerous than Pooh:\n"





-- Using a subquery select information about only the bears with a danger_rating greater than the average.
\! echo "\nBears with a greater than average danger rating:\n"





-- Write a query that will retrieve the bears and assign them a danger level based on their danger rating.  
-- >> 'not dangerous': danger_rating of 6 or less
-- >> 'dangerous': danger_rating of 7 or 8
-- >> 'very dangerous': danger_rating of 9 or above
\! echo "\nAssigning bears a danger level:\n"




-- Refactor the above to use a subquery. 
-- >> This time bears with an above average danger_rating should be classed as 'very dangerous' and those with a below average rating  should be classed as 'not dangerous'.
\! echo "\nDanger level refactor:\n"




-- Query the database to find the crimes committed by all the bears that have an above average danger rating WITHOUT using a JOIN.
\! echo "\nDangerous Bear Crimes:\n"


