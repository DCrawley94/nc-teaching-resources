/*
Lets do something a little different.

I want to rank the the albums by duration in 
descending order.

I need to get the following data:
    - album_title
    - album_length
    - album length ranking
*/

\c nc_albums

\! echo "\nRanking albums by album length:\n"
WITH album_details AS (
    SELECT DISTINCT 
        album_title,
        album_length
    FROM album_catalogue
)
SELECT *,
     RANK() OVER (ORDER BY album_length DESC) AS album_length_rank
FROM album_details
ORDER BY album_length_rank;
