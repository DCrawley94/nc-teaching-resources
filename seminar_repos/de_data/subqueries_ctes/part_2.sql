\c nc_art_gallery

-- List all the collectors who have purchased paintings from the gallery
\! echo "Collectors who have purchased from our gallery:"

SELECT first_name, last_name
FROM collectors
WHERE collector_id 
IN (
  SELECT collector_id
  FROM sales
);

SELECT * FROM collectors;