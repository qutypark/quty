---
title: "Programmers_Python_heap_디스크 컨트롤러"
date: 2021-06-11
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12117)

### 프로그래머스_힙_디스크 컨트롤러

- 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 
- 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return.

- job = [[0, 3], [1, 9], [2, 6]]

#### 풀이방식
- 핵심: 
[First Come First Served(FCFS)](https://www.geeksforgeeks.org/program-for-fcfs-cpu-scheduling-set-1/)이 아닌 ->  " [Shortest Job First(SJF)](https://www.guru99.com/shortest-job-first-sjf-scheduling.html)
"
- [heapq](https://docs.python.org/3/library/heapq.html)사용

```python
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
