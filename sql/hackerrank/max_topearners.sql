select max(salary*months), count(*)
from employee
where salary*months = (select max(salary*months) from employee);

/*
or
*/
select salary*months, count(*)
from employee
group by salary*months
order by salary*months desc limit 1;
