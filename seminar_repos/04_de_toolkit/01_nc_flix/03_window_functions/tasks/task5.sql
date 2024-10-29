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

SELECT sales_period,
    album_title,
    artist_name,
    copies_sold,
    SUM(copies_sold) OVER(PARTITION BY album_title ORDER BY sales_period ASC) AS cumulative_sum_by_album
FROM album_catalogue
JOIN artists ON artists.artist_id = album_catalogue.artist_id
JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id;
