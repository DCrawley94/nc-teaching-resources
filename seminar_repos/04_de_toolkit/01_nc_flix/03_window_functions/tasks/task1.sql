/*
The CFO want details about album sales in the fourth quarter 
of 2022.

I need to present them with the following information:
    - sales_period
    - album_title 
    - artist_name, 
    - copies sold
    - TOTAL copies sold
for all albums in the sales_period of '2022_4Q'.
*/

\c nc_albums

\! echo "\nSales in the fourth quarter of 2022:\n"

SELECT 
    sales_period,
    album_title,
    artist_name,
    copies_sold,
    SUM(copies_sold) OVER ()
FROM album_catalogue AS c
LEFT OUTER JOIN artists AS a ON c.artist_id = a.artist_id
LEFT OUTER JOIN sales_periods AS s ON c.sales_period_id = s.period_id
WHERE s.sales_period = '2022_4Q';


