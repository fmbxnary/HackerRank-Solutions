SELECT
    c.company_code,
    c.founder,
    COUNT(distinct lm.lead_manager_code),
    COUNT(distinct sm.senior_manager_code),
    COUNT(distinct m.manager_code),
    COUNT(distinct e.employee_code)
from
    company c
    JOIN lead_manager lm ON lm.company_code = c.company_code
    JOIN senior_manager sm ON sm.company_code = c.company_code
    JOIN manager m ON m.company_code = c.company_code
    JOIN employee e ON e.company_code = c.company_code
GROUP BY
    c.company_code,
    c.founder
ORDER BY
    c.company_code
