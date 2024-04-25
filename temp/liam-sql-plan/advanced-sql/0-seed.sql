DROP DATABASE IF EXISTS nc_heroes;
CREATE DATABASE nc_heroes;

\c nc_heroes

-- Create the "teams" table
CREATE TABLE teams (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(100),
    formation_year INTEGER
);

-- Insert data into the "teams" table
INSERT INTO teams (team_name, formation_year) VALUES
    ('X-Men', 1963),
    ('Defenders', 1971),
    ('Avengers', 1963),
    ('Starjammers', 1977);

-- Create the "superheroes" table
CREATE TABLE superheroes (
    superhero_id SERIAL PRIMARY KEY,
    alias VARCHAR(100),
    real_name VARCHAR(100),
    is_identity_secret BOOLEAN,
    movie_appearances INT CHECK (movie_appearances >= 0),
    team_id INTEGER REFERENCES teams(team_id)
);

-- Insert data into the "superheroes" table
INSERT INTO superheroes (alias, real_name, is_identity_secret, movie_appearances, team_id) VALUES
    ('Captain Marvel', 'Carol Danvers', false, 4, 3),
    ('Daredevil', 'Matt Murdoch', true, 2, 2),
    ('Squirrel Girl', 'Doreen Allene Green', false, 0, 3),
    ('Shadowcat', 'Kitty Pryde', false, 4, 1),
    ('Storm', 'Ororo Munroe', false, 7, 1),
    ('Spider-Man', 'Peter Parker', true, 15, 3),
    ('Power Man', 'Luke Cage', false, 0, 2),
    ('Corsair', 'Christopher Summers', true, 0, 4),
    ('Beast', 'Hank McCoy', false, 7, 1);