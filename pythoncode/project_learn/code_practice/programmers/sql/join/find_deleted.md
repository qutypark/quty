### 프로그래머스_SQL_Join_없어진 기록 찾기
[문제링크](https://programmers.co.kr/learn/courses/30/parts/17046)
- 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL.
- 보호소 들어온 기록 : animal_ins
- 입양을 간 기록 : animal_outs

#### 풀이방식(mysql)
> 1. not in with subquery join
```mysql
select animal_id, name
from animal_outs
where animal_id not in(SELECT o.animal_id
                       from animal_outs o
                       join animal_ins i 
                       on o.animal_id=i.animal_id)
order by animal_id;
```
> 2. not in (without join)

```mysql
select animal_id, name
from animal_outs
where animal_id not in (select animal.id from animal_ins)
order by animal_id;
```
