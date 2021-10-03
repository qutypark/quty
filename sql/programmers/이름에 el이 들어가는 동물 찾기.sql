SELECT animal_id, name
from animal_ins
where name regexp "EL" and animal_type = 'Dog'
order by name;

/*
or
*/

SELECT animal_id, name
from animal_ins
where name like "%el%" and animal_type = 'Dog'
order by name;
