-- Select the code that shows the name, region and population of the smallest country in each region
-- table: bbc

select name, region, population 
from bbc as x
where population <= all(select population from bbc as y where x.region=y.region and populatoin>0);


