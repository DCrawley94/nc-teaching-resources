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

SELECT album_title,
    artist_name,
    copies_sold,
    album_genre,
    SUM(copies_sold) OVER(PARTITION BY album_genre) AS sales_by_genre
FROM album_catalogue
JOIN artists ON artists.artist_id = album_catalogue.artist_id
JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id
WHERE sales_period = '2022_4Q';