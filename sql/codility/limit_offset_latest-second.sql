SELECT e1.event_type as event_type, (e1.value - e2.value) AS value FROM
events e1
JOIN
events e2
ON
e1.event_type = e2.event_type
AND
e1.time = (SELECT time FROM events temp1 WHERE
           temp1.event_type = e1.event_type ORDER BY time DESC LIMIT 1)
AND
e2.time = (SELECT time FROM events temp2 WHERE
           temp2.event_type = e2.event_type ORDER BY time DESC LIMIT 1 OFFSET 1)
order by event_type;

/*
or
*/



SELECT a.event_type as event_type,
       a.value-b.value as value
FROM
  (SELECT e1.*
   FROM EVENTS e1,
     (SELECT event_type,
             max(TIME) AS TIME
      FROM EVENTS
      GROUP BY event_type
      HAVING count(event_type) > 1) MAX
   WHERE e1.event_type = max.event_type
     AND e1.time = max.time) a,

  ( SELECT e1.*
   FROM EVENTS e1,
     (SELECT e1.event_type,
             max(e1.time) AS TIME
      FROM EVENTS e1,
        (SELECT event_type,
                max(TIME) AS TIME
         FROM EVENTS
         GROUP BY event_type
         HAVING count(event_type) > 1) MAX
      WHERE e1.event_type = max.event_type
        AND e1.time < max.time
      GROUP BY e1.event_type) max2
   WHERE e1.event_type = max2.event_type
     AND e1.time = max2.time ) b
WHERE a.event_type = b.event_type
order by event_type;
