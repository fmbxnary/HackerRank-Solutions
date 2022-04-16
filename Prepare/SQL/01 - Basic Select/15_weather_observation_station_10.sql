SELECT
    DISTINCT city
FROM
    station
WHERE
    NOT city RLIKE '[a, e, i, u, o]$';
