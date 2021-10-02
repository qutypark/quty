

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

