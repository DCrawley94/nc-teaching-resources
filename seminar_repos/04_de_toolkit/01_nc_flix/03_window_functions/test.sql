\! echo "\nSales in the fourth quarter of 2022:\n"

SELECT 
    sales_period,
    album_title,
    artist,
    copies_sold,
    SUM (copies_sold) OVER() AS sold_in_4Q_2022
FROM album_catalogue
WHERE sales_period = '2022_4Q';


\! echo "\nSales over time of the album 'In the Right Place':\n"
SELECT sales_period,
     album_title,
     artist,
     copies_sold,
     SUM (copies_sold) OVER(ORDER BY sales_period ASC) AS cumulative_sum
FROM album_catalogue
WHERE album_title = 'In the Right Place';

\! echo "\nSales in the fourth quarter by genre':\n"
SELECT album_title,
    artist,
    copies_sold,
    album_genre,
    SUM (copies_sold) OVER(PARTITION BY album_genre) AS sales_by_genre
FROM album_catalogue
WHERE sales_period = '2022_4Q';

\! echo "\nSales in the fourth quarter by genre':\n"
SELECT sales_period,
    album_title,
    artist,
    copies_sold,
    SUM (copies_sold) OVER(PARTITION BY album_title ORDER BY sales_period ASC) AS cumulative_sum_by_album
FROM album_catalogue;