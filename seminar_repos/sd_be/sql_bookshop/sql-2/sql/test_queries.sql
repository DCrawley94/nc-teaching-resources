\c imdb_2

-- Select all the films and all the actors using the junction table


SELECT films.title, actor_name
FROM film_actors
JOIN films  ON  films.film_id = film_actors.film_id
JOIN actors ON actors.actor_id = film_actors.actor_id;

-- Select all the actors that are not in any movies

SELECT title, actor_name
FROM film_actors
JOIN films  ON  films.film_id = film_actors.film_id
RIGHT OUTER JOIN actors ON actors.actor_id = film_actors.actor_id
WHERE title IS NULL;

-- Count the number of actors that have been in a film that has a rating less than 5

SELECT COUNT(actor_name) AS actor_count
FROM film_actors
JOIN films  ON  films.film_id = film_actors.film_id
JOIN actors ON actors.actor_id = film_actors.actor_id
WHERE rating < 5;