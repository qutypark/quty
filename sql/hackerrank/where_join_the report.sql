

select (select (case when grades.grade<8 then "NULL" else students.name end)) as name, grades.grade, students.marks
from students, grades
where students.marks between grades.min_mark and grades.max_mark
order by grades.grade desc, students.marks desc, name;


select (case when g.grade<8 then null else s.name end) as name, g.grade, s.marks
from students as s
join grades as g on s.marks between g.min_mark and g.max_mark
order by g.grade desc, name;
