---
title: "Programmers_Python_heap_디스크 컨트롤러"
date: 2021-06-11
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12117)



### 프로그래머스_힙_디스크 컨트롤러

- 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 
- 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return.


### 풀이방식
#### 핵심
- [First Come First Served(FCFS)](https://www.geeksforgeeks.org/program-for-fcfs-cpu-scheduling-set-1/)이 아닌 ->  " [Shortest Job First(SJF)](https://www.guru99.com/shortest-job-first-sjf-scheduling.html)"<br>
즉 요청이 오는 순서대로가 아닌, **작업 소요시간이 짧은** 순서대로 처리하는 것<br>

- [heapq](https://docs.python.org/3/library/heapq.html)사용(힙 우선순위 큐)

#### 코드 구현
-  누적 시간, 현 시점, 처리량, 시작 시점의 변수 생성
-  처리량이 총 작업 수보다 작을 때까지

>   소요시간 짧은 순서대로 큐 생성<br>
>>      시작 시점과 현 시점 사이에 있는 시점 큐가 존재하면<br>
>>>         시작 시점을 현 시점으로 갱신<br>
>>>         짧은 순서대로 ->  현 시점 = 각 소요시간을 누적<br>
>>>         짧은 순서대로 ->  총 걸린 시간 = (현 시점 -  각 요청시점)을 누적<br>

>>      시작 시점과 현 시점 사이에 있는 시점 큐가 존재하지 않으면<br>
>>>     현 시점을 +1 해나감

- 다 처리 했다면, 평균 구함

```python
# job = [[0, 3], [1, 9], [2, 6]]
import heapq
def solution(jobs):
    ans,now,i = 0,0,0
    start = -1 
    h = []
    while i < len(jobs):
        for e in jobs:
            # 소요시간이 짧은 대로 리스트 추가 ( " Shortest Job First(SJF)" )
            if start < e[0] <= now: 
                heapq.heappush(h, [e[1],e[0]]) 
        if len(h)>0:
            curr = heapq.heappop(h)
            start = now # 시작 지점을 갱신 
            now += curr[0] # 소요시간을 누적
            ans += (now-curr[1]) # 총 걸린 시간 => (누적 소요시간 - 각 요청시점)을 누적
            i+=1
        # 맨 처음은 -1< < 0이니, 해당되는 요소가 없어 h가 비게 됨
        # now를 늘려나감
        else:
            now+=1
    # 평균
    return int(ans/len(jobs))
```
