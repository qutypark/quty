-- with multiple temporary table
with t1 as(
    select @row_num := @row_num+1 as hour
    from animal_outs, (select @row_num:=-1) as tmp
    where @row_num < 23),
    t2 as(
        select hour(datetime) as hour, count(*) as cnt 
        from animal_outs group by hour
    )

select t1.hour, coalesce(t2.cnt, 0) as count
from t2
right join t1 on t1.hour = t2.hour
order by t1.hour;
 

-- my own
select t2.hour as hour, coalesce(t1.cnt, 0) as count
from 
(select hour(datetime) as hour, count(animal_id) as cnt
from animal_outs group by hour) as t1
right join
(select @row_number:=@row_number+1 as hour 
 from animal_outs, (select @row_number:=-1) as t limit 24) as t2
 on t1.hour = t2.hour
order by hour;



/*
set @row_n
*/


set @row_n = -1;
select hour, max(cnt) as m_cnt
from (
    (select hour(datetime) as hour, count(*) as cnt
     from animal_outs
     group by hour)
    union
    (select 
     @row_n := @row_n+1 as hour, 0 as cnt
     from animal_outs
     limit 24)
) tmp
group by hour
order by hour;

/*
refer to other ans; 임시테이블 
*/

/* time table with reculsive: 0~23 h */

WITH RECURSIVE TIMETABLE  AS (
    SELECT 0 AS HOUR FROM DUAL
    UNION ALL
    SELECT HOUR + 1 FROM TIMETABLE
    WHERE HOUR < 23
)
SELECT ct.HOUR, IFNULL(COUNT, 0) COUNT
FROM TIMETABLE AS ct
    LEFT JOIN (SELECT HOUR(DATETIME) HOUR, count(ANIMAL_ID) COUNT
            FROM ANIMAL_OUTS
            GROUP BY HOUR
            HAVING HOUR BETWEEN 0 AND 23
            ORDER BY HOUR
    ) AS animal ON ct.HOUR = animal.HOUR
    
    
