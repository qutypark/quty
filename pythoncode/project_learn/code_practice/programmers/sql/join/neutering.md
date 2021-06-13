### 프로그래머스_SQL_Join_보호소에서 중성화한 동물
[문제링크](https://programmers.co.kr/learn/courses/30/parts/17046)

- 보호소에 들어올 당시에는 중성화 X
- 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회.
- 결과: 아이디 순으로 조회.

#### 풀이방식(mysql)
> 1. join & like 

```mysql
SELECT o.animal_id, o.animal_type, o.name
from animal_outs o
join animal_ins i on o.animal_id = i.animal_id
where (i.sex_upon_intake like 'intact%') and (
    (o.sex_upon_outcome like 'Spayed%') or (o.sex_upon_outcome like 'Neutered%'))
order by o.animal_id;
```
> 2. left outer join
>> 중성화가 된 후, 중성화가 되지 않는 경우는 없음<br>
>> 따라서 != 로도 해결 가능 
```mysql
SELECT o.animal_id, o.animal_type, o.name
from animal_outs o
left outer join animal_ins i
on o.animal_id = i.animal_id
where i.sex_upon_intake != o.sex_upon_outcome
order by o.animal_id
```
