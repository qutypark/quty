SELECT o.animal_id, o.name
from animal_outs o
join animal_ins i
on o.animal_id = i.animal_id
where o.datetime < i.datetime
order by i.datetime;

select outs.animal_id, outs.name
from animal_outs as outs
join animal_ins as ins
on outs.animal_id = ins.animal_id
and outs.datetime < ins.datetime
order by ins.datetime;
