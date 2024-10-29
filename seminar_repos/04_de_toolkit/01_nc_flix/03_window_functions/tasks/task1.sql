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
    SUM(copies_sold) OVER() AS sold_in_4Q_2022
FROM album_catalogue
JOIN artists ON artists.artist_id = album_catalogue.artist_id
JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id
WHERE sales_period = '2022_4Q';