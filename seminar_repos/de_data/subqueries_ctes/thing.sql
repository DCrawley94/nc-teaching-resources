DROP DATABASE IF EXISTS nc_art_gallery;
CREATE DATABASE nc_art_gallery;

\c nc_art_gallery

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR,
  last_name VARCHAR
)

CREATE TABLE paintings (
  id SERIAL PRIMARY KEY,
  artwork_name VARCHAR,
  artist_id INT,
  listed_price DECIMAL
)
