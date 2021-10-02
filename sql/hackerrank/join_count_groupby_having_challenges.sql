
select c.hacker_id,h.name,count(c.challenge_id) as cnt 
from challenges c 
join hackers h
on c.hacker_id = h.hacker_id
group by c.hacker_id, h.name
having cnt = 
(select max(counts) from (select count(challenge_id) as counts from challenges group by hacker_id) as countstable1) 
or
cnt in (select counts from (select count(challenge_id) as counts from challenges group by hacker_id) as countstable2 group by counts having count(*)=1)
order by cnt desc,c.hacker_id;


