/*
 Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to  decimal places.
*/

SET @rowindex := -1;
 
SELECT
   round(AVG(s.lat_n),4) as Median 
FROM
   (SELECT @rowindex:=@rowindex + 1 AS rowindex,
           station.lat_n AS lat_n
    FROM station
    ORDER BY station.lat_n) AS s
WHERE
s.rowindex IN (FLOOR(@rowindex / 2), CEIL(@rowindex / 2));

/*
or
*/

SELECT round(lat_n,4) from (SELECT @rowid:=@rowid+1 as rowid,lat_n
FROM station, (SELECT @rowid:=0) as init
ORDER BY lat_n) as s 
where rowid=(select round(count(*)/2) from station);


