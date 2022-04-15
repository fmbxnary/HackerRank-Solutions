SELECT
    DISTINCT city
FROM
    station
WHERE
    city RLIKE '^[a,e,i,o,u].*[a,e,i,o,u]$';
