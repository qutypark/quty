### 프로그래머스_SQL_Join_있었는데요 없었습니다.
[문제링크](https://programmers.co.kr/learn/courses/30/parts/17046)
- 관리자의 실수로 일부 동물의 입양일이 잘못 입력됨. 
- 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성. 
- 이때 결과는 보호 시작일이 빠른 순으로 조회.

```mysql
SELECT o.animal_id, o.name
from animal_outs o
join animal_ins i
on o.animal_id = i.animal_id
where o.datetime < i.datetime
order by i.datetime;
```
