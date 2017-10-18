-- script that lists all the cities of California that
-- can be found in the database

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id;
