-- list of cities
SELECT cities.id, cities.name, state.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
