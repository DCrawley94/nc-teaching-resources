/*
Yet more requests from the CFO.
They need a list the albums and their cumulative sales 
data by genre.

I need to get the following data:
    - sales_period
    - album_title 
    - artist_name
    - copies_sold, 
    - CUMULATIVE sales by album
for all artists.
*/

\c nc_albums

\! echo "\nCumulative sales by album':\n"

SELECT 
    sales_period,
    album_title,
    artist_name,
    copies_sold,
    SUM(copies_sold) OVER (PARTITION BY artist_name ORDER BY sales_period)
FROM album_catalogue AS c
LEFT OUTER JOIN artists AS a ON c.artist_id = a.artist_id
LEFT OUTER JOIN sales_periods AS s ON c.sales_period_id = s.period_id;
