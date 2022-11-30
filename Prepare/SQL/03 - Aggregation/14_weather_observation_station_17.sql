SELECT
    ROUND(long_w, 4)
FROM
    station
WHERE
    lat_N > 38.7780
ORDER BY
    lat_n
LIMIT
    1
