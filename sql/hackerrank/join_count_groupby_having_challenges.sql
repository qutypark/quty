
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


select ch.hacker_id, hk.name, ch.cnt as challenges_created
from 
(select count(challenge_id) as cnt, hacker_id 
 from challenges 
 group by hacker_id) as ch
 left join Hackers as hk 
 on ch.hacker_id = hk.hacker_id
 where ch.cnt = 
 (select count(challenge_id) as ct from challenges group by hacker_id order by ct desc limit 1)
 or ch.cnt in 
 (select ct from (select count(challenge_id) as ct from challenges group by hacker_id) as tmp1
  group by ct having count(*)=1)
 order by challenges_created desc, ch.hacker_id;

-- error

select ch.hacker_id, hk.name, ch.cnt as challenges_created
from 
(select count(challenge_id) as cnt, hacker_id 
 from challenges 
 group by hacker_id) as ch
 left join Hackers as hk 
 on ch.hacker_id = hk.hacker_id
 where ch.cnt = 
 (select count(challenge_id) as ct from challenges group by hacker_id order by ct desc limit 1)
 or ch.cnt in 
 /*
 (select count(challenge_id) as ct from challenges group by hacker_id having count(*)>1)
 order by challenges_created desc, ch.hacker_id;
  */
