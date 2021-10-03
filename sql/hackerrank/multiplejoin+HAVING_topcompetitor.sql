/*
 Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. 
 Order your output in descending order by the total number of challenges in which the hacker earned a full score. 
 If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.
*/

select h.hacker_id,h.name
from hackers h
inner join submissions s on h.hacker_id=s.hacker_id
inner join Challenges c on s.challenge_id=c.challenge_id
inner join difficulty d on c.difficulty_level=d.difficulty_level
where s.score=d.score and c.difficulty_level=d.difficulty_level
group by h.hacker_id,h.name
having count(s.hacker_id)>1
order by count(s.hacker_id) desc, s.hacker_id asc;
