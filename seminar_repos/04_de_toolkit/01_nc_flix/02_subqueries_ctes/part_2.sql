\c nc_art_gallery

-- List all the collectors who have purchased paintings from the gallery
\! echo "\nCollectors who have purchased from our gallery:\n"

SELECT first_name, last_name
FROM collectors
WHERE collector_id IN (
    SELECT collector_id
    FROM sales
);

SELECT DISTINCT first_name, last_name
FROM sales
LEFT JOIN collectors
ON sales.collector_id = collectors.collector_id; 