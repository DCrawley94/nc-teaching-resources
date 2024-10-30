/*
Yet more requests from the CFO.
They need a list the albums, their sales data for the 
fourth quarter of 2022, and the sales by genre for that quarter.

I need to get the following data:
    - album_title
    - artist_name 
    - copies_sold
    - album_genre, 
    - TOTAL sales by genre (not cumulative)
for all albums in the sales_period of '2022_4Q'.
*/

\c nc_albums

\! echo "\nSales in the fourth quarter by genre':\n"

SELECT 
    album_title,
    artist_name,
    copies_sold,
    album_genre,
    SUM(copies_sold) OVER (PARTITION BY album_genre )
FROM album_catalogue AS c
LEFT OUTER JOIN artists AS a ON c.artist_id = a.artist_id
LEFT OUTER JOIN sales_periods AS s ON c.sales_period_id = s.period_id
WHERE sales_period = '2022_4Q';

