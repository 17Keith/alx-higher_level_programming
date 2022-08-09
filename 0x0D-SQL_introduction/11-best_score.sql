-- This script lists all records of a table
-- Score >= 10
-- Score is ordered from top to bottom
-- Displays the name and the score
SELECT
    score,
    name
FROM
    second_table
WHERE
    score >= 10
ORDER BY
    score DESC;