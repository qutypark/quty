### 프로그래머스_SQL_GroupBy_고양이와 개는 몇마리 있을까
[문제링크](https://programmers.co.kr/learn/courses/30/parts/17044)

- 동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문.
- 이때 고양이를 개보다 먼저 조회.

### 풀이방법
> 1. Groupby

```sql
select animal_type, count(animal_id)
from animal_ins
where animal_type = 'Cat' or animal_type='Dog'
group by animal_type
order by animal_type;
```

> 2. UNION

```sql
(select animal_type, count(animal_id)
from animal_ins
where animal_type = 'Cat') 
union
(select animal_type, count(animal_id)
from animal_ins
where animal_type = 'Dog')
```
