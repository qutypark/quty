SELECT 
    c.company_code, c.founder, lm.cc, sm.cc, m.cc, e.cc
FROM
    company c
    LEFT JOIN ( SELECT COUNT( company_code ) AS cc, company_code FROM lead_manager GROUP BY company_code ) lm ON c.company_code = lm.company_code

    LEFT JOIN ( SELECT COUNT( company_code ) AS cc, company_code FROM senior_manager GROUP BY company_code ) sm ON c.company_code = sm.company_code
    LEFT JOIN ( SELECT COUNT( company_code ) AS cc, company_code FROM manager GROUP BY company_code ) m ON c.company_code = m.company_code
    LEFT JOIN ( SELECT COUNT( company_code ) AS cc, company_code FROM employee GROUP BY company_code ) e ON c.company_code = e.company_code
ORDER BY c.company_code
