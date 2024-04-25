\c nc_heroes

-- Rank superheroes by movie_appearances, grouped within their individual teams

SELECT 
  alias, 
  team_name,
  RANK() OVER (
    PARTITION BY team_name ORDER BY movie_appearances DESC
  ) AS most_popular_team_member
FROM superheroes
JOIN teams ON teams.team_id = superheroes.team_id;