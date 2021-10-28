-- table: bbc

-- 1. Select the code that shows the name, region and population of the smallest country in each region

select name, region, population 
from bbc as x
where population <= all(select population from bbc as y where x.region=y.region and populatoin>0);

-- 2. Select the code that shows the countries belonging to regions with all populations over 50000

select name, region, population 
from bbc as x
where 50000 < all(select population from bbc as y where x.region=y.region and populatoin>0);


-- 3. Select the code that shows the countries with a less than a third of the population of the countries around it

select name, region
from bbc as x
where population < all(select population/3 from bbc as y where x.region=y.region and x.name!=y.name);

-- 4. Select the code that would show the countries with a greater GDP than any country in Africa (some countries may have NULL gdp values).

select name, region 
from bbc
where gdp > (select max(gdp) from bbc where region="Africa")

