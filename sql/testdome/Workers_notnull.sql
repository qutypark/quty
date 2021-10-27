-- https://www.testdome.com/questions/50469
-- Write a query that selects only the names of employees who are not managers.

select name
from employees
where id not in (select managerid from employees where managerid is not null);

