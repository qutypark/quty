### 프로그래머스_SQL_GROUPBY_동명 동물 수 찾기
[문제링크](https://programmers.co.kr/learn/courses/30/parts/17044)

- 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문. 
- 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회.


```sql
select name, cnt
from (select name, count(*) as cnt
      from animal_ins
      group by name) tmp
where cnt >= 2 and name is not null
order by name;
```
