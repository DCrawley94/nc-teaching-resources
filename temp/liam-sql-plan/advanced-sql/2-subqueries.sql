\c nc_heroes

-- subquery type 1 - WHERE (...)

SELECT alias, movie_appearances
FROM superheroes
WHERE movie_appearances > (
  SELECT AVG(movie_appearances) FROM superheroes
);

-- subquery type 2 - FROM (good for taking an aggregate of an aggregate)
-- Average number of heroes per team

SELECT AVG(hero_count) AS average_heroes_per_team FROM (
  SELECT COUNT(superheroes.team_id) AS hero_count
  FROM teams
  JOIN superheroes ON teams.team_id = superheroes.team_id
  GROUP BY superheroes.team_id
) sub;

-- POSSIBLE Example for later - to convert to CTEs

SELECT AVG(known_identities_count) AS avg_known_identities_per_team
FROM (
  SELECT
    teams.team_name,
    COUNT(CASE WHEN superheroes.is_identity_secret = FALSE THEN 1 END) AS known_identities_count
  FROM teams
  LEFT JOIN superheroes ON superheroes.team_id = teams.team_id
  GROUP BY teams.team_name
) sub;

-- [OPTIONAL] correlated subqueries??????
-- I could do a WHOLE LECTURE ON SUBQUERIES
-- You can reference a column or alias in an outer query from __within the inner query__
-- What about... if you want to look at fellow super team members who have been in more movies than the average of their team?

SELECT alias 
FROM superheroes
WHERE movie_appearances > (
  SELECT AVG(movie_appearances)
  FROM superheroes AS team_heroes
  WHERE superheroes.team_id = team_heroes.team_id
);

-- Let's not even get into recursive subqueries lmao, I love SQL