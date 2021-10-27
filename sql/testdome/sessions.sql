-- https://www.testdome.com/questions/35738
-- Write a query that selects userId and average session duration for each user who has more than one session.

with cte as(
select userid, count(id) as cnt, avg(duration) as avdu
from sessions
group by userid
having cnt>1)

select userid, avdu
from cte;

