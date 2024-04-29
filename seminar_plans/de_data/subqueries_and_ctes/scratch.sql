\c nc_art_gallery;


-- 1 - scalar
SELECT painting_name, listed_price
FROM paintings
WHERE listed_price > (
    SELECT AVG(listed_price)
    FROM paintings
);

-- 2 - scalar
SELECT first_name, last_name, painting_name, sales_price
FROM sales
JOIN paintings ON sales.painting_id = paintings.painting_id
JOIN artists on sales.artist_id = artists.artist_id
WHERE sales_price = (
  SELECT MIN(sales_price)
  FROM sales
);
  

-- 3 - multi row
SELECT first_name, last_name
FROM collectors
WHERE collector_id IN (
    SELECT collector_id
    FROM sales
);


-- subqueries -> CTE
SELECT 
  sales_price,
  (SELECT MIN(sales_price) FROM sales) AS min,
  (SELECT MAX(sales_price) FROM sales) AS max,
  ROUND((SELECT AVG(sales_price) FROM sales), 2) AS average,
  ROUND(sales_price - (SELECT AVG(sales_price) FROM sales), 2) AS price_diff_from_average
FROM sales
ORDER BY price_diff_from_average DESC;

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