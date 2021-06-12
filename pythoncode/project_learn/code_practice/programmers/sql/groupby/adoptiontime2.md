### 프로그래머스_SQL_Groupby_입양시각구하기2
[문제링크](https://programmers.co.kr/learn/courses/30/parts/17044)

- 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문. 
- 테이블에는, 7~19 시간대만 존재 -> 0~6, 20~23 을 0 수동처리.
- 결과는 시간대 순으로 정렬.

#### 풀이방법
> 1. [set](https://www.w3schools.com/sql/sql_ref_set.asp) 과 조회순번 @row_n
> 2. union
> 3. max
```sql
set @row_n = -1; --조회순번을 통해 업데이트, 
select hour, max(cnt) as m_cnt
from (
    (select hour(datetime) as hour, count(*) as cnt
     from animal_outs
     group by hour)
    union
    (select 
     @row_n := @row_n+1 as hour, 0 as cnt
     from animal_outs
     limit 24) -- 23시까지이므로 24통해 0~23으로 리미트
) tmp
group by hour -- for max(cnt)
order by hour;
```
