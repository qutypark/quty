-- 2022-10-09
select
    c.company_code
    , c.founder
    , count(distinct l.lead_manager_code)
    , count(distinct s.senior_manager_code)
    , count(distinct m.manager_code)
    , count(distinct e.employee_code)
from company c
left join lead_manager l on c.company_code = l.company_code
left join senior_manager s on c.company_code = s.company_code and l.lead_manager_code = s.lead_manager_code
left join manager m on c.company_code = m.company_code and s.senior_manager_code = m.senior_manager_code
left join employee e on c.company_code = e.company_code and e.manager_code = m.manager_code
group by 1, 2
order by 1

--- past

select c.company_code, c.founder, em.lead_manager_code, em.senior_manager_code, em.manager_code, em.employee_code
from company as c
left join 
(select company_code, count(distinct(lead_manager_code)) as lead_manager_code, count(distinct(senior_manager_code)) as senior_manager_code, 
 count(distinct(manager_code)) as manager_code, count(distinct(employee_code)) as employee_code from employee group by company_code) as em
on c.company_code = em.company_code
order by c.company_code asc;



SELECT 
    c.company_code, c.founder, lm.cc, sm.cc, m.cc, e.cc
FROM
    company c
    LEFT JOIN ( SELECT COUNT( company_code ) AS cc, company_code FROM lead_manager GROUP BY company_code ) lm ON c.company_code = lm.company_code

    LEFT JOIN ( SELECT COUNT( company_code ) AS cc, company_code FROM senior_manager GROUP BY company_code ) sm ON c.company_code = sm.company_code
    LEFT JOIN ( SELECT COUNT( company_code ) AS cc, company_code FROM manager GROUP BY company_code ) m ON c.company_code = m.company_code
    LEFT JOIN ( SELECT COUNT( company_code ) AS cc, company_code FROM employee GROUP BY company_code ) e ON c.company_code = e.company_code
ORDER BY c.company_code
