---
title: "Programmers_Python_heap_더맵게"
date: 2021-06-11
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12117)

{% include adsense.html %}


### 프로그래머스_힙_더맵게
- 계산식: 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

- 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return
- 불가능하면  -1 return

#### 풀이방식
- [heapq](https://docs.python.org/3/library/heapq.html)를 이용

```python
import heapq 
def solution(sco,k):
    cnt=0
    h=[]
    for e in sco:
        heapq.heappush(h,e)
    while h[0]<k:
        try:
            heapq.heappush(h,(heapq.heappop(h)+heapq.heappop(h)*2))
        except:
            return -1
        cnt+=1
    return cnt
```
