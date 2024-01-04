-- EXAMPLE ONLY - build up in seminar
\c imdb_2

-- insert data into film table
INSERT INTO films (title, director_name, release_date, rating) VALUES
    ('Inception', 'Christopher Nolan', '2010-07-16', 9),
    ('La La Land', 'Damien Chazelle', '2016-12-09', 8),
    ('The Shawshank Redemption', 'Frank Darabont', '1994-09-10', 10),
    ('Jurassic Park', 'Steven Spielberg', '1993-06-11', 8),
    ('Leprechaun', 'Mark Jones', '1993-01-08', 3),
    ('Seven', 'David Fincher', '1995-09-22', 9),
    ('Interstellar', 'Christopher Nolan', '2014-11-05', 8),
    ('Barbie', 'Greta Gerwig', '2023-07-21', 8),
    ('The Room', 'Tommy Wiseau', '2003-06-27', 2);
