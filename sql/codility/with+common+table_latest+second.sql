WITH evt AS
(
  select
    event_type,
    value,
    row_number() over(partition by event_type order by time desc) rn
  from events
)
select
    t1.event_type, t1.value - t2.value
from evt t1, evt t2
where t1.event_type = t2.event_type
and t1.rn = 1
and t2.rn = 2;
