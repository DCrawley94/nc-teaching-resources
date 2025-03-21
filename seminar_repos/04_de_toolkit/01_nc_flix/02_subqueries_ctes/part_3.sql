\c nc_art_gallery

-- The boss wants a sales report, the report should include the following data:
--    > the sale_price of each artwork sold
--    > the minimum sale_price
--    > the maximum sale_price
--    > the average sale_price
--    > the difference between each artworks sale price and the average


SELECT 
  sales_price,
  (SELECT MIN(sales_price) FROM sales) AS min,
  (SELECT MAX(sales_price) FROM sales) AS max,
  ROUND((SELECT AVG(sales_price) FROM sales), 2) AS average,
  ROUND(sales_price - (SELECT AVG(sales_price) FROM sales), 2) AS price_diff_from_average
FROM sales
ORDER BY price_diff_from_average DESC;

-- CTE (sales_details):
--  - sales_price
--  - min
--  - max
--  - average

WITH sales_details AS (
    SELECT
        sales_price,
        (SELECT MIN(sales_price) FROM sales) AS min,
        (SELECT MAX(sales_price) FROM sales) AS max,
        ROUND((SELECT AVG(sales_price) FROM sales), 2) AS average
    FROM sales
)
SELECT 
    sales_price,
    min,
    max,
    average,
    sales_price - average AS price_diff_from_average
FROM sales_details
ORDER BY price_diff_from_average DESC;

-- Final Output:
--  - sales_price
--  - min
--  - max
--  - average
--  - price_difference
--  ORDERED 