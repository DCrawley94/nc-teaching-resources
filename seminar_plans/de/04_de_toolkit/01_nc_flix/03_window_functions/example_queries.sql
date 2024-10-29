\c nc_albums

\! echo "\nSales in the fourth quarter of 2022:\n"

SELECT 
    sales_period,
    album_title,
    artist_name,
    copies_sold,
    SUM(copies_sold) OVER() AS sold_in_4Q_2022
FROM album_catalogue
JOIN artists ON artists.artist_id = album_catalogue.artist_id
JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id
WHERE sales_period = '2022_4Q';


\! echo "\nSales over time of the album 'Licensed to Ill':\n"
SELECT sales_period,
     album_title,
     artist_name,
     copies_sold,
     SUM(copies_sold) OVER(ORDER BY sales_period ASC) AS cumulative_sum
FROM album_catalogue
JOIN artists ON artists.artist_id = album_catalogue.artist_id
JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id
WHERE album_title = 'Licensed to Ill';

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

-- Could also rewrite it as a subquery if there's time. Just for bants really

SELECT *,
     RANK() OVER (ORDER BY album_length DESC) AS album_length_rank
FROM (
    SELECT DISTINCT 
        album_title,
        album_length
    FROM album_catalogue
    ) AS distinct_album
ORDER BY album_length_rank;

\! echo "\nCumulative sales by album':\n"
SELECT sales_period,
    album_title,
    artist_name,
    copies_sold,
    SUM(copies_sold) OVER(PARTITION BY album_title ORDER BY sales_period ASC) AS cumulative_sum_by_album
FROM album_catalogue
JOIN artists ON artists.artist_id = album_catalogue.artist_id
JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id;


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


