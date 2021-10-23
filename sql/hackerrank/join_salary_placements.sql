
select s.name from students s
join friends f on s.id=f.id
join packages p1 on s.id=p1.id
join packages p2 on f.friend_id=p2.id
where p2.salary>p1.salary
order by p2.salary;

-- or


select s.name as name
from students as s
join friends as f on f.id = s.id
join packages as p on p.id = s.id
where p.salary < (select p2.salary from packages as p2 where p2.id = f.friend_id)
order by (select p2.salary from packages as p2 where p2.id = f.friend_id);

