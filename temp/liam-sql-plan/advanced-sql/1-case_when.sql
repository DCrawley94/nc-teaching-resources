\c nc_heroes

-- get aliases if identity is secret, otherwise select real names

SELECT CASE 
  WHEN is_identity_secret = TRUE 
    THEN alias
    ELSE real_name
  END AS hero
FROM superheroes;

-- get a count of the number of superheroes with known identities

SELECT
  teams.team_name,
  COUNT(CASE WHEN superheroes.is_identity_secret = FALSE THEN 1 END) AS known_identities_count
FROM teams
LEFT JOIN superheroes ON superheroes.team_id = teams.team_id
GROUP BY teams.team_name;

