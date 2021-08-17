---
title: “Programmers_Python_모든문제_Cache"
date: 2021-08-17
categories: Algorithms
---

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/17680)


### 프로그래머스_모든문제_캐시
2018 KAKAO BLIND RECRUITMENT

### 문제 설명

- 입력 형식<br>
> 캐시 크기(cacheSize)와 도시이름 배열(cities)을 입력받는다.<br>
> cacheSize는 정수이며, 범위는 0 ≦ cacheSize ≦ 30 이다.<br>
> cities는 도시 이름으로 이뤄진 문자열 배열로, 최대 도시 수는 100,000개이다.<br>
> 각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. <br>
> 도시 이름은 최대 20자로 이루어져 있다.
<br>

- 출력 형식<br>
> 입력된 도시이름 배열을 순서대로 처리할 때, "총 실행시간"을 출력한다.
<br>

- 조건<br>
> 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.<br>
> cache hit일 경우 실행시간은 1이다.<br>
> cache miss일 경우 실행시간은 5이다.<br>

### 문제 풀이

#### LRU = Least Recently Used Algorithm
- 설명
> 캐시에서 메모리를 다루기 위해 사용되는 알고리즘

- 전제
> 캐시의 리소스 양은 제한되어 있고, 그 제한된 리소스 내에서 캐시는 데이터를 빠르게 저장/접근 할 수 있어야 함.<br>
> 따라서 "가장 최근에 사용된 적이 없는" 캐시의 메모리부터 대체/새로운 데이터로 갱신.

- 동작 방식
1. 캐시 리스트에 데이터가 없다면, 캐시 리스트(오른쪽)에 저장
2. 캐시 리스트에 데이터가 있다면, 그 데이터를 캐시 리스트 맨 오른쪽으로 옮김
3. 캐시 리스트가 제한 사이즈를 초과하면, 캐시 리스트 맨 왼쪽 데이터를 새 데이터로 대체.

- 예시
> 데이터: [a, b, c, b, d]<br>
> 캐시 size: 3<br>
> {} -> {a} -> {a, b} -> {a, b, c} ->. {a, c, b} -> {c, b, d}

### 코드
```python
from collections import deque

def solution(size, cities):    
    cities = list(map(str.upper, cities))
    deq = deque()
    city = deque(cities)
    cnt = 0

    if size > 0:
        while city:
            c = city.popleft()
            if c not in deq:
                if len(deq) < size:
                    deq.append(c)
                elif len(deq) == size:
                    deq.popleft()
                    deq.append(c)
                cnt += 5
            else:
                deq.remove(c)
                deq.append(c)
                cnt += 1
    else:
        cnt = 5*len(city)
    return cnt
```
