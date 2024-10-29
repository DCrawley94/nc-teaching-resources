/*
Next we need information about album sales
in Q2 2022 including total sales by genre and 
the how much each album contributes to genre sales
as a percentage.

I need to get the following data:
    - album_title
    - artist_name
    - copies_sold
    - album_genre
    - TOTAL sales by genre, 
    - Percentage contribution to total genre sales
for '2022_2Q'.
*/
\c nc_albums

\! echo "\nPercentage of total genre sales in Q1 2023':\n"

SELECT album_title,
     artist_name,
     copies_sold,
     album_genre,
     SUM(copies_sold) OVER (PARTITION BY album_genre) AS sales_by_genre,
     ROUND((copies_sold::decimal/ SUM(copies_sold) OVER (PARTITION BY album_genre))*100.0, 2) AS percent_of_genre_sales
FROM album_catalogue
JOIN artists ON artists.artist_id = album_catalogue.artist_id
JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id
WHERE sales_period = '2023_1Q'
ORDER BY album_genre, copies_sold DESC;