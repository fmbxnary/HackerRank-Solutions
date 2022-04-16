SELECT
    DISTINCT city
FROM
    station
WHERE
    NOT city RLIKE '^[a, e, i, o, u]'
    AND NOT city RLIKE '[a, e, i, o, u]$';
