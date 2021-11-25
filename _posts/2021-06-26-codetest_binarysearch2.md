---
title: “Programmers_Python_이분탐색_징검다리"
date: 2021-06-26
categories: Algorithms
---


> [문제링크](https://programmers.co.kr/learn/courses/30/lessons/43236)

{% include adsense.html %}

### 프로그래머스_python_이분탐색_징검다리

- 출발지점부터 도착지점까지의 거리 distance, 바위들이 있는 위치를 담은 배열 rocks, 제거할 바위의 수 n이 매개변수로 주어질 때, <br>
- 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return

#### 풀이방법

> 이분탐색
> - 해당 조건:  바위 간 거리가 추정치보다 짧음
> - 위의 조건을 만족할 때 돌을 제거해나감

```python
def soltuion(dis, rock, n):
    rock.sort()
    ans = 0
    left, right = 1, dis
    while left <= right:
        mid = (left+right)//2
        b_rock = 0
        cnt = 0
        mn = dis
        for r in rock:
            dis_b = r-b_rock
            if dis_b < mid:
                cnt += 1
            else:
                mn = min(mn, dis_b)
                b_rock = r 
        if cnt > n:
            right = mid-1
        else:
            left = mid+1
            ans = mn
    return ans
```

#### 풀이 코멘트 포함

```python
def soltuion(dis, rock, n):
    rock.sort()
    ans = 0
    left, right = 1, dis
    while left <= right:
        mid = (left+right)//2 # 추정치
        b_rock = 0 # 거리 계산 용 기준점
        cnt = 0 # 제거할 돌 갯수
        mn = dis # 최초 최솟값 = 총 거리
        for r in rock:
            dis_b = r-b_rock
            if dis_b < mid: # 바위 간 거리가 추정치보다 짧음
                cnt += 1 # 제거할 돌 갯수 추가
            else: # 바위 간 거리가 추정치보다 멂
                mn = min(mn, dis_b)  # 거리 최솟값을 갱신
                b_rock = r # 거리 계산 용 기준점을 해당 바위로 갱신
        if cnt > n: # 제거한 돌 갯수가 많으면
            right = mid-1 # 추정치를 줄여나감
        else:
            left = mid+1
            ans = mn
    return ans
```


> 실패 (시간 효율 X)
>> brute_force
>>> 제거 돌의 조합으로 -> 최솟값을 계산해나감

```python
from itertools import combinations

def solution(dis, rock, n):
    rock.sort()
    c_list = list(combinations(rock, n))
    m = 0
    for c_set in c_list:
        rock2 = rock.copy()
        for c in c_set:
            rock2.remove(c)
        if not rock2:
            m = dis
        else:
            dis_b = [rock2[0]]
            rock2.append(dis)
            for i in range(len(rock2)-1):
                dis_b.append(rock2[i+1]-rock2[i])
            m = max(m, min(dis_b))
    return m
```
