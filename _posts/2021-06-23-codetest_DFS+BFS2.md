---
title: “Programmers_Python_DFS+BFS_여행경로"
date: 2021-06-23
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12421)


### 프로그래머스_DFS+BFS_여행경로
- 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return.
- 제한사항
> - 주어진 항공권은 모두 사용.
> - tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미
> - 항상 "ICN" 공항에서 출발
> - 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return.
> - 모든 도시를 방문할 수 없는 경우는 주어지지 않음.

#### 풀이방식
- DFS
> 딕셔너리로 그래프 생성

```python
from collections import defaultdict

def solution(tick):
    # 1. 출발지와 도착지의 딕셔너리 생성
    dic = defaultdict(list)
    for t in tick:
        dic[t[0]].append(t[1])

    # 2. 도착지 기준 내림차순으로 정렬
    # ans list에 도착지점이 막다른 길부터 넣은 후, 마지막에 역순 정렬
    for d in dic.keys():
        dic[d].sort(reverse=True)

    ans = []
    stack = ['ICN'] # 출발 노드를 스택에 넣어줌

    # 3. 딕셔너리(그래프)탐색
    while stack:
        s = stack[-1] # 출발지
        if not dic[s]: # 해당 출발지에서 도착 가능한 지역이 없다면(막다른 길)
            ans.append(stack.pop()) # 해당 출발지를 넣음
        else:
            stack.append(dic[s].pop()) # 해당 출발지의 도착지를 새로운 출발지로

    # 4. ans list 역순
    ans.reverse()
    return ans
```


>> 잘못된 코드
>>> 막다른 길의 존재를 고려하지 않음

```python
def solution(tick):
    tick.sort(key=lambda x: x[-1])

    vis = [0]*len(tick)
    qu = ['ICN']
    ans = ['ICN']
    while qu:
        if 0 not in vis:
            break
        q = qu.pop()
        for i, t in enumerate(tick):
            if t[0] == q:
                if vis[i] == 0:
                    vis[i] = 1
                    ans.append(t[1])
                    qu.append(t[1])
                    break
    return ans
```
