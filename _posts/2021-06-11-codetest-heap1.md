---
title: "Programmers_Python_heap_더맵게"
date: 2021-06-11
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12117)



### 프로그래머스_힙_더맵게
- 계산식: 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

- 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, <br>
  모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return
- 불가능하면  -1 return

### 풀이방식
- [heapq](https://docs.python.org/3/library/heapq.html)를 이용

#### 힙
- 1. [힙(heap)](https://ko.wikipedia.org/wiki/힙_(자료_구조))은 최댓값 및 최솟값을 찾아내는 연산을 빠르게 하기 위해 <br>
  고안된 완전이진트리(complete binary tree)를 기본으로 한 자료구조(tree-based structure)
- 2. 힙으로 최대 최소 값을 찾아 [우선순위 큐](https://ko.wikipedia.org/wiki/우선순위_큐)생성이 가능
- 3. 최소값이면서 K값보다 작은 요소 순서대로 스코빌 지수 생성
- 4. 최소 횟수 도출 가능

#### 코드 구현
- 0. 작은 순서대로 처리하는 우선순위 큐 생성(h)
- 1. 스코빌 지수 리스트를 오름차순 정렬
- 2. 가장 작은 수가 K보다 작을 때까지(<-> 크면 모든 음식 스코빌 지수가 K이상)
> 2.1 heapq.heaqpop를 통해 작은 값을 추출<br>
> 2.2 스코빌 지수 계산식<br>
> 2.3 계산 값을 heapq.heappush 우선순위 큐에 삽입<br>
> 2.4 카운트 처리 <br>
- 3. 불가능하면 return -1

#### 파이썬 코드

```python
import heapq 
def solution(sco,k):
    cnt=0
    h = []
    for s in sco:
        heapq.heappush(h, s)
    while h[0]<k:
        try:
            heapq.heappush(h,(heapq.heappop(h)+heapq.heappop(h)*2))
        except:
            return -1
        cnt+=1
    return cnt
```
