-- EXAMPLE ONLY - Delete and build up in seminar, these are just suggestions.
-- Focus: Different join behaviours, including a complex join using the new junction table. 
-- Bonus: Build up an advanced query that includes an aggregate function.
\c imdb_2

-- QUERY FOR FILM TITLES, RELEASE DATE AND DIRECTORS


SELECT title, release_date, director_name FROM films
JOIN directors
ON films.director_id = directors.director_id;





-- select all the films and all the actors using the junction table
-- select all the actors that are not in any movies
-- using an aggregate function, list the names of all the associated actors in the db for each film with a rating less than 5