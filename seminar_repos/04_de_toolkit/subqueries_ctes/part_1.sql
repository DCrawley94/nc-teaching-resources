\c nc_art_gallery

-- Get the artwork_name and listed_price of all 
--   paintings that are above the average price  

\! echo "\nPaintings that are above average price:\n"

SELECT artwork_name, listed_price
FROM paintings
WHERE listed_price > (
    SELECT AVG(listed_price)
    FROM paintings
);

-- Get the artist's *full name* and painting name of the painting 
--    that sold for the least amount of money

\! echo "\nPainting that sold for the the least amount of money:\n"

SELECT CONCAT(first_name, ' ', last_name) AS full_name, artwork_name
FROM sales
JOIN paintings ON paintings.painting_id = sales.painting_id
JOIN artists ON sales.artist_id = artists.artist_id
WHERE sales_price = (
    SELECT MIN(sales_price)
    FROM sales
);

