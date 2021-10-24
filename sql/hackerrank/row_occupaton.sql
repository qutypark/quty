set @r1=0, @r2=0, @r3=0, @r4=0;
select min(Doctor), min(Professor), min(Singer), min(Actor) from
(select case occupation when 'Doctor' then @r1:=@r1+1
                        when 'Professor' then @r2:=@r2+1
                        when 'Singer' then @r3:=@r3+1
                        when 'Actor' then @r4:=@r4+1 end 
        as rowline,
        case when occupation='Doctor' then name end as Doctor,
        case when occupation='Professor' then name end as Professor,
        case when occupation='Singer' then name end as Singer,
        case when occupation='Actor' then name end  as Actor
        from occupations order by name) as tem
group by rowline;

-- temporary table

set @r1=0, @r2=0, @r3=0, @r4=0;

with tmp as 
(select case occupation when 'Doctor' then @r1:=@r1+1
                        when 'Professor' then @r2:=@r2+1
                        when 'Singer' then @r3:=@r3+1
                        when 'Actor' then @r4:=@r4+1 end 
        as rowline,
        case when occupation='Doctor' then name end as Doctor,
        case when occupation='Professor' then name end as Professor,
        case when occupation='Singer' then name end as Singer,
        case when occupation='Actor' then name end  as Actor
        from occupations order by name) 
        
select min(Doctor), min(Professor), min(Singer), min(Actor) 
from tmp
group by rowline;
