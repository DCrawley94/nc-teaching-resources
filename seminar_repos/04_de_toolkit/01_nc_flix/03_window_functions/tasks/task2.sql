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

SELECT sales_period,
     album_title,
     artist_name,
     copies_sold,
     SUM(copies_sold) OVER(ORDER BY sales_period ASC) AS cumulative_sum
FROM album_catalogue
JOIN artists ON artists.artist_id = album_catalogue.artist_id
JOIN sales_periods ON sales_periods.period_id = album_catalogue.sales_period_id
WHERE album_title = 'Licensed to Ill';