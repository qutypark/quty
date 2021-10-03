/*
Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
*/
select distinct(city) from station
where lower(substr(city, -1, 1)) in ('a','e','i','o','u');

/*
regexp
*/
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '[aeiouAEIOU]$';
