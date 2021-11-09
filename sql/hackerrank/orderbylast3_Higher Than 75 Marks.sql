select name
from students
where marks > 75
order by substr(name,-3,3), id asc;

-- or 

select name
from students
where marks>75
order by right(name, 3), id;

