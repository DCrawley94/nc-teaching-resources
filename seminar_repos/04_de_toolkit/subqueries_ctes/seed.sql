DROP DATABASE IF EXISTS nc_art_gallery;
CREATE DATABASE nc_art_gallery;

\c nc_art_gallery


CREATE TABLE artists (
  artist_id SERIAL PRIMARY KEY,
  first_name VARCHAR,
  last_name VARCHAR
);

CREATE TABLE paintings (
  painting_id SERIAL PRIMARY KEY,
  artwork_name VARCHAR,
  artist_id INT REFERENCES artists(artist_id),
  listed_price NUMERIC(1000, 2)
);

CREATE TABLE collectors (
  collector_id SERIAL PRIMARY KEY,
  first_name VARCHAR,
  last_name VARCHAR
);

CREATE TABLE sales (
  sales_id SERIAL PRIMARY KEY,
  sale_date DATE,
  painting_id INT REFERENCES paintings(painting_id),
  artist_id INT REFERENCES artists(artist_id),
  collector_id INT REFERENCES collectors(collector_id),
  sales_price NUMERIC(1000, 2)
);

INSERT INTO artists
(first_name, last_name)
VALUES
('Kate', 'Smith'),
('Natali', 'Wein'),
('Nigel', 'Dataman'),
('Francesco', 'Benelli');

INSERT INTO paintings
(artwork_name, artist_id, listed_price)
VALUES
('Miracle', 1, 300.00),
('Sunshine', 1, 700.00),
('Pretty Woman', 2, 2800.00),
('Handsome Man', 2, 2300.00),
('Barbie', 3, 250.00),
('Cool painting', 3, 5000.00),
('Black square #1000', 3, 50.00),
('Mountains', 4, 1300.00);

INSERT INTO collectors
(first_name, last_name)
VALUES
('Brandon', 'Cooper'),
('Laura', 'Fisher'),
('Christina', 'Buffet'),
('Steve', 'Stevenson');

INSERT INTO sales
(sale_date, painting_id, artist_id, collector_id, sales_price)
VALUES
('2024-04-01', 3, 2, 4, 2500.00),
('2024-04-10', 4, 2, 2, 2300.00),
('2024-04-10', 1, 1, 2, 300.00),
('2024-04-15', 6, 3, 3, 4000.00),
('2024-04-22', 5, 3, 3, 200.00),
('2024-04-22', 7, 3, 3, 50.00);