-- https://sqlzoo.net/wiki/JOIN_Quiz

-- 1. Select the code which shows players, their team and the amount of goals they scored against Greece(GRE).

select player, teamid, count(*)
from game join goal on matchid=id
where (team1 = "GRE" or team2 = "GRE")
and teamid! = "GRE"
group by player, teamid;

-- 2. Select the code which would show the player and their team for those who have scored against Poland(POL) in National Stadium, Warsaw.

select distinct player, teamid
from game join goal on matchid=id
where Stadium = "National Stadium, Warsaw"
and (team1 = "POL" or team2 = "POL")
and teamid! = "POL";

-- 3. Select the code which shows the player, their team and the time they scored, for players who have played in Stadion Miejski (Wroclaw) but not against Italy(ITA).

select distinct player, teamid, time
from game join goal on matchid=id
where Stadium = "National Stadium, Warsaw"
and (team1 = teamid and team2 != "ITA") or (team2 = teamid and team1 != "ITA");


