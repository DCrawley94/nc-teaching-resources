\c imdb_2

DROP TABLE IF EXISTS films;
DROP TABLE IF EXISTS actors;
DROP TABLE IF EXISTS directors;

-- directors table
CREATE TABLE IF NOT EXISTS directors (
    director_id SERIAL PRIMARY KEY,
    director_name VARCHAR(255) NOT NULL
);

-- actors table
CREATE TABLE IF NOT EXISTS actors (
    actor_id SERIAL PRIMARY KEY,
    actor_name VARCHAR(255) NOT NULL
);

-- movies table
CREATE TABLE IF NOT EXISTS films (
    film_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_date DATE NOT NULL,
    rating INT NOT NULL,
    director_id INT REFERENCES directors(director_id) ON DELETE CASCADE
);
