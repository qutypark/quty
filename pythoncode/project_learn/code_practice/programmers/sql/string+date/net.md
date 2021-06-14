### 프로그래머스_string+date_중성화여부 파악하기
[문제링크](https://programmers.co.kr/learn/courses/30/parts/17047)

- 중성화된 동물은 SEX_UPON_INTAKE 컬럼에 'Neutered' 또는 'Spayed'.
- 동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성. 
- 중성화가 되어있다면 'O', 아니라면 'X'라고 표시.

#### 풀이방법
>. IF 

```mysql
SELECT animal_id, name, if(sex_upon_intake regexp 'intact', "X", "O") net
from animal_ins
order by animal_id;
```
