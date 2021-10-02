
select company_code,founder,
(select count(distinct(lead_manager_code)) from employee where employee.company_code = company.company_code),
(select count(distinct(senior_manager_code))from employee where employee.company_code = company.company_code),
(select count(distinct(manager_code)) from employee where employee.company_code = company.company_code),
(select count(distinct(employee_code)) from employee where employee.company_code = company.company_code)
from company
order by company_code asc;

