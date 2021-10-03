
select name, count(name)
from animal_ins
where name in (select name from animal_ins group by name having count(*) >=2 )
group by name
order by name;

/*
simplest
*/

SELECT NAME, COUNT(*) AS count
FROM ANIMAL_INS
GROUP BY NAME
HAVING count(*) > 1
ORDER BY NAME

/*
or
*/

select name, cnt
from (select name, count(*) as cnt
      from animal_ins
      group by name) tmp
where cnt >= 2 and name is not null
order by name;

