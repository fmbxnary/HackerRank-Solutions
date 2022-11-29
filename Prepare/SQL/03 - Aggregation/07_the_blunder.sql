SELECT
    CEILING(
        AVG(CAST(SALARY as DECIMAL(9, 2))) - AVG(CAST(REPLACE(Salary, '0', '') as DECIMAL(9, 2)))
    )
from
    EMPLOYEES