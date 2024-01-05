-- EXAMPLE ONLY - Delete and build up in seminar, these are just suggestions.
-- Focus: Different join behaviours, including a complex join using the new junction table. 
-- Bonus: Build up an advanced query that includes an aggregate function.
\c imdb_2

-- QUERY FOR FILM TITLES, RELEASE DATE AND DIRECTORS


SELECT title, release_date, director_name FROM films
JOIN directors
ON films.director_id = directors.director_id;



-- select all the films and all the actors using the junction table

SELECT title, actor_name
FROM film_actors
JOIN films ON films.film_id = film_actors.film_id
JOIN actors ON actors.actor_id = film_actors.actor_id;
-- select all the actors that are not in any movies

SELECT actor_name
FROM film_actors
JOIN films ON films.film_id = film_actors.film_id
RIGHT OUTER JOIN actors ON actors.actor_id = film_actors.actor_id
WHERE title IS NULL;

-- using an aggregate function, list the names of all the associated actors in the db for each film with a rating less than 5

-- Maybe count the number of actors instead? No group by but it does introduce aggregate functions

SELECT actor_name
FROM film_actors
JOIN films ON films.film_id = film_actors.film_id
JOIN actors ON actors.actor_id = film_actors.actor_id
WHERE rating < 5;