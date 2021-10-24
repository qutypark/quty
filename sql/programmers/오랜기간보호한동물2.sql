select outs.ANIMAL_ID, outs.NAME
from ANIMAL_INS as ins
join ANIMAL_OUTS as outs
on ins.ANIMAL_ID = outs.ANIMAL_ID
order by datediff(outs.DATETIME, ins.DATETIME) desc
limit 2;
