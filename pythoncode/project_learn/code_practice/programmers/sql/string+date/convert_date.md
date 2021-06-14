### 프로그래머스_SQL_String+date_datetime에서date로 형변환
[문제링크](https://programmers.co.kr/learn/courses/30/parts/17047)

- 각 동물의 아이디와 이름, 들어온 날짜1를 조회하는 SQL문. 
- 이때 결과는 아이디 순으로 조회.
- 날짜(년-월-일)만

```mysql
SELECT animal_id, name, date_format(datetime, "%Y-%m-%d") as date
from animal_ins
order by animal_id;
```
