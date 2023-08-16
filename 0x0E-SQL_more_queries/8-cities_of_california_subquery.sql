-- Lists all cities of California from the database
-- Retrieves the state ID for California from the states table
-- Results are sorted in ascending order by cities.id
SELECT id, name
FROM cities
WHERE state_id = (
  SELECT id
  FROM states
  WHERE name='California'
)
ORDER BY cities.id ASC;
