-- Say my name
-- A script that lists all records of the table
-- second_table.
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
