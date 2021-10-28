-- https://sqlzoo.net/wiki/Using_Null_Quiz
-- table teacher has null value on id

-- 1. Select out of following the code which uses a JOIN to show a list of all the departments and number of employed teachers

select dept.name, count(teacher.name) 
from teacher
right join dept -- table teacher has null value on id
on dept.id = teacher.dept
group by dept.name


