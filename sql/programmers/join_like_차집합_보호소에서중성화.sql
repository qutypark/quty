-- simple
select ANIMAL_ID, ANIMAL_TYPE, NAME
from ANIMAL_INS as ins
where SEX_UPON_INTAKE != 
(select SEX_UPON_OUTCOME from ANIMAL_OUTS where ANIMAL_ID = ins.ANIMAL_ID)
order by ANIMAL_ID;


/*
like %%
*/
SELECT o.animal_id, o.animal_type, o.name
from animal_outs o
join animal_ins i on o.animal_id = i.animal_id
where (i.sex_upon_intake like 'intact%') and (
    (o.sex_upon_outcome like 'Spayed%') or (o.sex_upon_outcome like 'Neutered%'))
order by o.animal_id;

/*
차집합
*/

select o.animal_id, o.animal_type, o.name
from animal_outs o
left join animal_ins i 
on o.animal_id = i.animal_id
where i.sex_upon_intake != o.sex_upon_outcome
order by o.animal_id;



select ai.animal_id, ai.animal_type, ai.name
from 
animal_ins as ai
join animal_outs as ao
on ao.animal_id = ai.animal_id
where ai.SEX_UPON_INTAKE like "%intact%" and ao.SEX_UPON_outcome not like "%intact%"
order by animal_id;
