### 프로그래머스_sql_isnull_NULL처리하기
[문제링크](https://programmers.co.kr/learn/courses/30/parts/17045)
- 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 
- 이름이 없는 동물의 이름은 "No name"으로 표시.
#### 풀이방식(mysql)
> 1. [COALESCE](https://www.w3schools.com/sql/func_mysql_coalesce.asp) 이용
```mysql
SELECT animal_type, COALESCE(name, 'No name'), sex_upon_intake
from animal_ins
order by animal_id;
```

> 2. [IFNULL](https://www.w3schools.com/sql/func_mysql_ifnull.asp) 이용
```mysql
SELECT animal_type, IFNULL(name, 'No name'), sex_upon_intake
from animal_ins
order by animal_id;
```
