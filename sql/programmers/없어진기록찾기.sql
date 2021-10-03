select animal_id, name
from animal_outs
where animal_id not in(SELECT o.animal_id
                       from animal_outs o
                       join animal_ins i 
                       on o.animal_id=i.animal_id)
order by animal_id;
