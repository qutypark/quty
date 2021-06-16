---
title: "Programmers_Python_heap_이중우선순위큐"
date: 2021-06-11
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12117)


{% include adsense.html %}


### 프로그래머스_힙_이중우선순위큐
- I 숫자	: 큐에 주어진 숫자를 삽입
- D 1	   : 큐에서 최댓값을 삭제 
- D -1	 : 큐에서 최솟값을 삭제

- 이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return

- operaion = ["I 16","D 1"]
#### 풀이방식
[heapq](https://docs.python.org/3/library/heapq.html)사용

```python
import heapq
def solution(lis):
    ans=[]
    for e in lis:
        e0 = e.split()[0]
        e1 = int(e.split()[1])
        if e0=='I':
            heapq.heappush(ans,e1)
        elif e0=='D' and e1==1:
            try:ans.pop(-1)
            except: pass
        elif e0=='D' and e1==-1:
            try:ans.pop(0)
            except: pass
    if len(ans)>1:
        return [max(ans),min(ans)]
    else:
        return [0,0]
```
