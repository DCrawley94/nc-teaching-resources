-- EXAMPLE ONLY - build up in seminar
\c imdb_2

DROP TABLE IF EXISTS films;

-- students to choose appropriate data types
CREATE TABLE films (
    film_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    director_name VARCHAR(200) NOT NULL,
    release_date DATE NOT NULL,
    rating INT NOT NULL
);