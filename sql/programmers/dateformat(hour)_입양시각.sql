select hr, cnt
from (select date_format(datetime, '%H') as hr, count(*) as cnt
     from animal_outs 
     group by hr) as tmp
where hr between 9 and 19
order by hr;

/*or*/

SELECT HOUR(DATETIME), count(*) as cnt
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 19
group by HOUR(DATETIME) 
order by HOUR(DATETIME);
