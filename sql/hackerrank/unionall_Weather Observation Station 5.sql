/*
Query the two cities in STATION with the shortest and longest CITY names, 
as well as their respective lengths (i.e.: number of characters in the name). 
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
*/

select * from (select city, length(city) as citylen from station order by citylen asc, city asc limit 1) as a
union
select * from (select city, length(city) as citylen from station order by citylen desc, city desc limit 1) as b;

/*
union all(union) with order by
--> subquery is necessary
*/
