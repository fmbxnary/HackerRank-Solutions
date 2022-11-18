SELECT
    Doctor,
    Professor,
    Singer,
    Actor
FROM
    (
        SELECT
            name,
            occupation,
            row_number() over(
                partition by occupation
                order by
                    name
            ) rowno
        FROM
            occupations
    ) AS PivotData PIVOT (
        max(name) FOR occupation IN (Doctor, Professor, Singer, Actor)
    ) as PivotTable
