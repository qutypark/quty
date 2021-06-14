###프로그래머스_String+date_루시와엘라

- 동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 <br>
동물의 아이디와 이름, 성별 및 중성화 여부를 조회하는 SQL 문.

#### solution

> 1. REGEXP (시작 끝의 제한필요)
```mysql
SELECT animal_id, name, sex_upon_intake
from animal_ins
REGEXP "^(Lucy|Ella|Pickle|Rogan|Sabrina|Mitty)$"
order by animal_id
```

> 2. IN
```mysql
SELECT animal_id, name, sex_upon_intake
from animal_ins
where name in ("Lucy","Ella","Pickle", "Rogan", "Sabrina", "Mitty")
order by animal_id;
```
