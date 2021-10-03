select hr, cnt
from (select date_format(datetime, '%H') as hr, count(*) as cnt
     from animal_outs 
     group by hr) as tmp
where hr between 9 and 19
order by hr;
