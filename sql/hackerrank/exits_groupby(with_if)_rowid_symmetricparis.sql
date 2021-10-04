

SELECT f1.X, f1.Y FROM Functions AS f1 
WHERE f1.X = f1.Y AND 
(SELECT COUNT(*) FROM Functions WHERE X = f1.X AND Y = f1.X) > 1
UNION
SELECT f1.X, f1.Y FROM Functions AS f1
WHERE EXISTS(SELECT X, Y FROM Functions WHERE f1.X = Y AND f1.Y = X AND f1.X < X)
ORDER BY X;

/*
another solution by others leaderboard
*/

SELECT if(X < Y, X, Y) as fx, if (X < Y, Y, X) as fy
FROM Functions
GROUP BY fx,fy
HAVING count(*) > 1
order by fx;


/*
rowid
*/

select a.x, a.y
from
(SELECT @row_number:=@row_number+1 AS rowid,x,y FROM functions, (SELECT @row_number:=0)as t order by x) as a
inner join 
(SELECT @row_number1:=@row_number1+1 AS rowid,x,y FROM functions, (SELECT @row_number1:=0)as t order by x) as b
on a.x = b.y and a.y = b.x and a.rowid < b.rowid
order by a.x;


/*
union all
*/

select x, y
from
(
    select x, y 
    from   functions 
    where  x = y
    group by x, y 
    having count(*) > 1
    union all
    select distinct f1.x, f1.y
    from   functions f1 
    join   functions f2 on  f1.x = f2.y
                        and f1.y = f2.x
                        and f1.x != f2.x
) a
where a.x <= a.y
order by a.x
;
