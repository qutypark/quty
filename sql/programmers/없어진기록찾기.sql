select outs.animal_id, outs.name
from animal_ins as ins
right join animal_outs as outs 
on ins.animal_id = outs.animal_id
where ins.animal_id is null
order by outs.animal_id;


select animal_id, name
from animal_outs
where animal_id not in(SELECT o.animal_id
                       from animal_outs o
                       join animal_ins i 
                       on o.animal_id=i.animal_id)
order by animal_id;

/*
or
*/

SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS A LEFT JOIN ANIMAL_INS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
