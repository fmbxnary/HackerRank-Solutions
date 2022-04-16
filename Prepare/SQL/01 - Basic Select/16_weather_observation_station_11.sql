SELECT
    DISTINCT city
FROM
    station
WHERE
    NOT city RLIKE '^[a, e, i, o, u].*[a, e, i, o, u]$';