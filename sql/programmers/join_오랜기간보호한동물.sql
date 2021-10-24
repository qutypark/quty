-- most simple

select NAME, DATETIME
from ANIMAL_INS
where ANIMAL_ID not in (select ANIMAL_ID from ANIMAL_OUTS)
order by DATETIME
limit 3;

-- else

select name, datetime
from animal_ins
where animal_id not in(select i.animal_id from animal_ins as i
                       join animal_outs as o
                       on i.animal_id=o.animal_id)
order by datetime asc
limit 3;

-- else

SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS AS I
LEFT JOIN ANIMAL_OUTS AS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL
ORDER BY I.DATETIME ASC
LIMIT 3
