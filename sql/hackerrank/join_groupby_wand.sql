
SELECT id, age, m.coins_needed, m.power FROM 
(SELECT code, power, MIN(coins_needed) AS coins_needed FROM Wands GROUP BY code, power) AS m
JOIN Wands AS w ON m.code = w.code AND m.power = w.power AND m.coins_needed = w.coins_needed
JOIN Wands_Property AS p ON m.code = p.code
WHERE p.is_evil = 0
ORDER BY m.power DESC, age DESC;

/*
or
*/
select id, age, coins_needed, wands.power 
from wands, Wands_Property 
where is_evil = 0 and Wands_Property.code = Wands.code and 
coins_needed <= all 
(select w.coins_needed from wands as w where wands.code = w.code AND wands.power = w.power) 
order by power desc, age desc;
