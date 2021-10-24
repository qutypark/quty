/*
instr
*/

SELECT ANIMAL_ID, NAME, IF(INSTR(SEX_UPON_INTAKE, 'Intact') > 0, 'X', 'O') AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

/*
regexp
*/

SELECT animal_id, name, if(sex_upon_intake regexp 'intact', "X", "O") as net
from animal_ins
order by animal_id;

-- case
select ANIMAL_ID, NAME, (case when SEX_UPON_INTAKE like "%intact%" then "X" else "O" end ) as net
from ANIMAL_INS
order by ANIMAL_ID;
