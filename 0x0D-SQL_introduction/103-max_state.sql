-- Script that displays the max temp of each state
SELECT
    state,
    MAX(value) max_temp
FROM
    temperatures
GROUP BY
    state
ORDER BY
    state;