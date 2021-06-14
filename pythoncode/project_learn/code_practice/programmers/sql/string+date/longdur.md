### 프로그래머스_SQL_String+date_오랜기간보호한동물
[문제링크](https://programmers.co.kr/learn/courses/30/parts/17047)

- 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL. 
- 이때 결과는 보호 기간이 긴 순으로 조회.

#### solution
> datediff

```mysql
SELECT o.animal_id, o.name
from animal_outs o
join animal_ins i 
on o.animal_id = i.animal_id
order by datediff(o.datetime, i.datetime) desc
limit 2;

```
