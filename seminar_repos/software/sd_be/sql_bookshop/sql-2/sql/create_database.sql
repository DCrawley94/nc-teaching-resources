DROP DATABASE IF EXISTS imdb_2;
CREATE DATABASE imdb_2;

\c imdb_2

-- directors table
CREATE TABLE directors (
    director_id SERIAL PRIMARY KEY,
    director_name VARCHAR(255) NOT NULL
);

-- actors table
CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    actor_name VARCHAR(255) NOT NULL
);

-- movies table
CREATE TABLE films (
        film_id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        release_date DATE NOT NULL,
        rating INT NOT NULL,
        director_id INT REFERENCES directors(director_id)
);

-- insert data into directors, actors, awards, and movies tables
INSERT INTO directors (director_name) VALUES
    ('Christopher Nolan'),
    ('Damien Chazelle'),
    ('Frank Darabont'),
    ('Steven Spielberg'),
    ('Tommy Wiseau'),
    ('David Fincher'),
    ('Greta Gerwig'),
    ('Mark Jones');

INSERT INTO actors (actor_name) VALUES
    ('Leonardo DiCaprio'),
    ('Elliot Page'),
    ('Joseph Gordon-Levitt'),
    ('Ryan Gosling'),
    ('Emma Stone'),
    ('John Legend'),
    ('Tim Robbins'),
    ('Morgan Freeman'),
    ('Bob Gunton'),
    ('Sam Neill'),
    ('Laura Dern'),
    ('Jeff Goldblum'),
    ('Brad Pitt'),
    ('Kevin Spacey'),
    ('Matthew McConaughey'),
    ('Anne Hathaway'),
    ('Jessica Chastain'),
    ('Margot Robbie'),
    ('America Ferrera'),
    ('Jennifer Aniston'),
    ('Warwick Davis'),
    ('Tommy Wiseau'),
    ('John Hurt'),
    ('Angelina Jolie'), 
    ('Elijah Wood'),
    ('Viola Davis');

INSERT INTO films (title, director_id, release_date, rating) VALUES
    ('Inception', 1, '2010-07-16', 9),
    ('La La Land', 2, '2016-12-09', 8),
    ('The Shawshank Redemption', 3, '1994-09-10', 10),
    ('Jurassic Park', 4, '1993-06-11', 8),
    ('Leprechaun', 8, '1993-01-08', 3),
    ('Seven', 6, '1995-09-22', 9),
    ('Interstellar', 1, '2014-11-05', 8),
    ('Barbie', 7, '2023-07-21', 8),
    ('The Room', 5, '2003-06-27', 2);

\! echo "\n\nActors table:"
SELECT * FROM actors;


\! echo "Films table:"
SELECT * FROM films;


\! echo "Directors table:"
SELECT * FROM directors;