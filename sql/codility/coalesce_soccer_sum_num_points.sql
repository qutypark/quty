-- write your code in PostgreSQ / ver1

select team_id, team_name, 
coalesce(sum(case when team_id = host_team then 
    (
    case when host_goals > guest_goals then 3
    when host_goals = guest_goals then 1
    when host_goals < guest_goals then 0
    end
    ) 
when team_id = guest_team then
    (
    case when guest_goals > host_goals then 3
    when guest_goals = host_goals then 1
    when guest_goals < host_goals then 0
    end
    )
    end), 0) as num_points
from Teams
left join Matches
on 
Teams.team_id = Matches.host_team
or Teams.team_id = Matches.guest_team
group by team_id, team_name
order by num_points desc, team_id;

-- write your code in PostgreSQL / ver2

SELECT t.team_id, t.team_name, sum(num_points) as num_points
from teams as t
join
(select t1.team_id as team_id, sum(t1.num) as num_points
from
(select host_team as team_id, (case when host_goals > guest_goals then 3
when host_goals = guest_goals then 1
else 0 end) as num from matches) as t1
group by t1.team_id) as host
on t.team_id = host.team_id
join
(select t2.team_id as team_id, sum(t2.num) as num_points
from
(select guest_team as team_id, (case when guest_goals > host_goals then 3
when host_goals = guest_goals then 1
else 0 end) as num from matches) as t2
group by t2.team_id) as guest
on t.team_id = guest.team_id
group by t.team_id, t.team_name
order by num_points desc, t.team_id asc;


