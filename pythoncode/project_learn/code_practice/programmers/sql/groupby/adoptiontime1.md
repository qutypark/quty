### 프로그래머스_SQL_Groupby_입양시각 구하기
[문제링크](https://programmers.co.kr/learn/courses/30/parts/17044)

- 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문.
- 09:00부터 19:59까지.
- 결과는 시간대 순으로 정렬.

#### 풀이방법(mysql)
> 핵심:  시간대 뽑아내기

```sql
SELECT hour, cnt
from (select DATE_FORMAT(datetime, "%H") as hour, count(*) as cnt -- hour(datetime) as hour 도 가능
     from animal_outs
     group by hour) tmp
where hour between 9 and 19
order by hour;
```
