

select (select (case when grades.grade<8 then "NULL" else students.name end)) as name, grades.grade, students.marks
from students, grades
where students.marks between grades.min_mark and grades.max_mark
order by grades.grade desc, students.marks desc, name;


