### 프로그래머스_SQL_Join_오랜 기간 보호한 동물
[문제링크](https://programmers.co.kr/learn/courses/30/parts/17046)

- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회. 
- 이때 결과는 보호 시작일 순.

#### 풀이방식(mysql)
> 1.without join

```mysql
SELECT name, datetime
from animal_ins
where animal_id not in (select animal_id from animal_outs)
order by datetime
limit 3;
```

> 2. left join
```mysql
select i.name, i.datetime
from animal_ins i
left join animal_out o using(animal_id)
where o.animal_id -- animal_id doesn't exist
order by i.datetime
limit 3;

```
