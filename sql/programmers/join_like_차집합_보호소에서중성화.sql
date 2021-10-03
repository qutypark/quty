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
