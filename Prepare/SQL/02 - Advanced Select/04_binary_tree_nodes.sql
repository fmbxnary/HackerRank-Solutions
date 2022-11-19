SELECT
    n,
    CASE
        WHEN p is NULL THEN 'Root'
        WHEN n in (
            SELECT
                p
            FROM
                bst
        ) THEN 'Inner'
        ELSE 'Leaf'
    END
FROM
    bst
ORDER by
    n;
