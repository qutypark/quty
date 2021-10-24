-- ifnull
SELECT animal_type, IFNULL(name, 'No name'), sex_upon_intake
from animal_ins
order by animal_id;

-- case
select ANIMAL_TYPE, (case when name is null then "No name" else name end) as name, SEX_UPON_INTAKE
from ANIMAL_INS
order by animal_id;

-- coalesce
select ANIMAL_TYPE, (coalesce(name, "No name")) as name, SEX_UPON_INTAKE
from ANIMAL_INS
order by animal_id;
