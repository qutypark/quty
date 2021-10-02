/*
 Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. 
 Order your output in descending order by the total number of challenges in which the hacker earned a full score. 
 If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.
*/

select h.hacker_id, h.name from Hackers h
inner join Submissions s on s.hacker_id = h.hacker_id
inner join Challenges c on c.challenge_id = s.challenge_id 
inner join Difficulty d on d.difficulty_level = c.difficulty_level
where d.score = s.score
group by h.hacker_id having count(*) > 1
order by count(*) desc, h.hacker_id asc;

