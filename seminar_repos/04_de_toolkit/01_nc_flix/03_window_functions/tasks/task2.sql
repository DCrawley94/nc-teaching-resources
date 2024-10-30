/*
The CFO has requested more information. 
This time about a particular album by the Beastie Boys.

I need to present them with the following information:
    - sales_period
    - album_title 
    - artist_name, 
    - copies sold
    - cumulative copies sold over time *chronologically*
for the album 'Licensed to Ill'.
*/

\c nc_albums

\! echo "\nSales over time of the album 'Licensed to Ill':\n"


SELECT
    sales_period,
    album_title,
    artist_name,
    copies_sold,
    SUM(copies_sold) OVER(ORDER BY sales_period) AS cumulative_sales_total
FROM album_catalogue AS c
LEFT OUTER JOIN artists AS a ON c.artist_id = a.artist_id
LEFT OUTER JOIN sales_periods AS s ON c.sales_period_id = s.period_id
WHERE album_title = 'Licensed to Ill';
