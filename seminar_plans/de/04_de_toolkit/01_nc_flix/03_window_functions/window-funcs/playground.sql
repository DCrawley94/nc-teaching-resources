\c nc_art_gallery


-- All sales with extra column for all sale prices summed up.

-- SELECT
--     ROW_NUMBER() OVER(ORDER BY artist_id) AS row_num,
--     *
-- FROM sales;

-- Rolling sales total over time per artist name.
-- Sales data from sales
-- artist name from artists
-- window function ordered sale_date to make sales cumulative for each partition

SELECT 
    sale_date, 
    CONCAT(first_name, ' ', last_name) AS artist_name,
    sales_price,
    SUM(sales_price) OVER ( PARTITION BY sales.artist_id ORDER BY sales.sale_date) as rolling_total
FROM sales
JOIN artists ON sales.artist_id = artists.artist_id
ORDER BY artist_name
;

SELECT 
    sale_date, 
    CONCAT(first_name, ' ', last_name) AS artist_name,
    sales_price,
    SUM(sales_price) OVER ( PARTITION BY sales.artist_id ORDER BY sales.sale_date) as rolling_total
FROM sales
JOIN artists ON sales.artist_id = artists.artist_id
ORDER BY sales.sale_date
;