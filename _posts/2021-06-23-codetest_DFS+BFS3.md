---
title: “Programmers_Python_DFS+BFS_타겟넘버"
date: 2021-06-23
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12421)


### 프로그래머스_DFS+BFS_타겟 넘버

- 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 
- 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 
- 가능한 연산 :  +, - 

#### 풀이방법_1
> #### [DFS 깊이 우선 탐색](https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/)
> 스택과 재귀 이용
>> idx값이 전체 길이와 같고, 값이 타겟값과 같아질 때까지, 덧셈과 뺄셈을 계속하는 재귀함수
```python
ans = 0 # 전역변수
# 재귀함수 지정
def dfs(num, tar, idx, val):
    global ans # 전역변수
    if idx == len(num):
        if val == tar:
            ans += 1
            return
        else:
            return
    else:
        dfs(num, tar, idx+1, val+num[idx]) # 재귀
        dfs(num, tar, idx+1, val-num[idx]) # 재귀
def solution_dfs(num, tar):
    global ans # 전역변수
    dfs(num, tar, 0, 0)
    return ans
```

#### 풀이방법_2
> #### [BFS 넓이 우선 탐색](https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/)
> queue이용
>> 레벨이 전체 길이에 도달했을 때, 타겟과 같은 덧셈 뺄셈 반복의 결과값 갯수
```python
from collections import deque

def solution(num, tar):
    queue = deque([(0, 0)])
    while queue:
        sm, lev = queue.popleft()
        if lev == len(num):
            break
        else:
            lev += 1
            queue.append((sm+num[lev-1], lev))
            queue.append((sm-num[lev-1], lev))
    return list(x[0] for x in queue).count(tar)
```

#### 풀이방법_3
> #### [brute_force](https://en.wikipedia.org/wiki/Brute-force_search)
> product을 이용한 [카르테시안 product](https://en.wikipedia.org/wiki/Cartesian_product)
>> 생성된 카르테시안 product을 합으로 맵핑 후, 타겟 넘버 카운트
```python
from itertools import product

def solution_bf(num, tar):
    l = [(x, -x) for x in num] # 덧셈, 뺄셈
    s = list(map(sum, product(*l))) # 생성된 카르테시안 product을 합으로 맵핑
    return s.count(tar)
```
