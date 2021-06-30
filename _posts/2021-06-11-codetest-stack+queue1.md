---
title: "Programmers_Python_stack+queue_기능개발"
date: 2021-06-11
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12081)



### 프로그래머스_스택큐_기능개발
- 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와<br>
  각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때<br> 
  각 배포마다 몇 개의 기능이 배포되는지를 return<br> 

### 풀이방식

####  1. dictionary의 value에 값을 더해나감

- 딕셔너리 생성: 시간을 key, 작업량을 value 
- 시간 : 남은 작업량 / 속도
- 현 시간이, 가장 긴 시간 안에 있다면 
    > 가장 긴 시간 key의 작업량를 더해나감<br>
- 현 시간이, 가장 긴 시간보다 더 길다면
    >  현 시간 key의 작업량를 더해나감

#### 2. queue

- 큐 생성(첫째 요소: 시간, 둘째 요소: 작업 수)
- 시간 : 남은 작업량 / 속도
- 가장 긴 시간보다 현 시간이 길면
    > 현 시간과 작업(초기:1)의 큐를 삽입<br>
- 현 시간이 가장 긴 시간보다 작다면
    >  가장 긴 시간의 작업 수르 더해 나감

#### 코드 1(dictionary이용)

```python
# progress = [93, 30, 55]
# speeds = [1, 30, 5]

import math

def solution(prog, speed):
    dic = {}
    for p, s in zip(prog, speed):
        t = math.ceil((100-p)/s)
        if dic:
            m = max(dic.keys())
            if t <= m:
                dic[m] += 1
            else:
                dic[t] = 1
        else:
            dic[t] = 1
    return list(dic.values())
```    

#### 코드 2(queue이용)

```python
# progress = [93, 30, 55]
# speeds = [1, 30, 5]

import math
def solution(progresses, speeds):
    queue=[]
    for p, s in zip(progresses, speeds):
        t = math.ceil((100-p)/s)
        if len(queue)== 0 or queue[-1][0] < t:
            queue.append([t,1])
        else:
            queue[-1][1] += 1
    return [q[1] for q in queue]
```
