\c imdb_2

CREATE TABLE film_actors (
  film_actor_id SERIAL PRIMARY KEY,
  film_id INT REFERENCES films(film_id),
  actor_id INT REFERENCES actors(actor_id)
);

INSERT INTO film_actors (film_id, actor_id) VALUES
(1, 1), (1, 2), (1, 3),
(2, 4), (2, 5), (2, 6),
(3, 7), (3, 8), (3, 9),
(4, 10), (4, 11), (4, 12),
(5, 20), (5, 21), (6, 8),
(6, 13), (6, 14), (7, 15),
(7, 16), (7, 17), (8, 4),
(8, 18), (8, 19), (9, 22);

\! echo "\n Junction Table:"
SELECT * FROM film_actors;