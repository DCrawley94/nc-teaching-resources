\c nc_art_gallery

-- Get the artwork_name and listed_price of all 
--   paintings that are above the average price  

\! echo "Paintings that are above average price:"

SELECT painting_name, listed_price
FROM paintings
WHERE listed_price > (
  SELECT AVG(listed_price)
  FROM paintings
);


-- Get the artist and painting name of the painting 
--    that sold for the least amount of money

\! echo "Painting that sold the the least amount of money:"

SELECT first_name || ' ' || last_name, painting_name
FROM sales
JOIN paintings ON paintings.painting_id = sales.painting_id
JOIN artists ON sales.artist_id = artists.artist_id
WHERE sales_price = (
  SELECT MIN(sales_price)
  FROM sales
);

