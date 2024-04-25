\c nc_heroes

-- 1. Refactor the subquery example to CTEs 
-- (not super confident this showcases them as being any better though)

WITH superhero_team_sizes AS (
  SELECT COUNT(superheroes.team_id) AS hero_count
  FROM teams
  JOIN superheroes ON teams.team_id = superheroes.team_id
  GROUP BY superheroes.team_id
)
SELECT AVG (hero_count) AS average_heroes_per_team 
FROM superhero_team_sizes;

-- 2. Do this extra wild thing (again, doesn't seem much better as a CTE)

WITH known_hero_identity_team_counts AS (
  SELECT
    teams.team_name,
    COUNT(CASE WHEN superheroes.is_identity_secret = FALSE THEN 1 END) AS known_identities_count
  FROM teams
  LEFT JOIN superheroes ON superheroes.team_id = teams.team_id
  GROUP BY teams.team_name
)
SELECT AVG(known_identities_count) AS avg_known_identities_per_team;