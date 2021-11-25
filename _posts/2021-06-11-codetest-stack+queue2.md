---
title: "Programmers_Python_stack+queue_프린터"
date: 2021-06-11
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/lessons/42587)

{% include adsense.html %}

### 프로그래머스_스택큐_프린터
- 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냄
- 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣음
- 그렇지 않으면 J를 인쇄

### 풀이방식

1. 가장 우선순위가 큰 수와, 현재 위치의 수를 비교
    > 위치 인덱스를 하나씩 앞당겨나감

####  풀이 코멘트 포함 1

```python
def solution(p,l):
    ans = 0
    # 우선순위가 가장 큰 수 
    m = max(p)
    # 프린트 목록 앞부터 1개씩 꺼냄
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            # 위치가 맨 앞이었고 가장 큰 수도 맨 앞이었기 때문에 진행 멈춤
            if l == 0:
                break
            # 아니라면, 프린트 목록 앞부터 1개씩 꺼냈으니 위치를 하나씩 앞으로 당김
            else:
                l -= 1
            # 우선순위가 큰 것을 갱신
            m = max(p)
        else:
            # 꺼내 것을 맨 뒤로 넣음
            p.append(v)
            # 위치가 맨 앞이었다면 앞에 것을 꺼냈다가 뒤로 넣었으니, 위치를 맨 뒤로 갱신
            if l == 0:
                l = len(p)-1
            else:
            # 위치를 하나씩 앞으로 당김
                l -= 1
    return ans
```

### 다른 사람 풀이

1. 앞에서부터 하나씩 요소를 pop
2. [any](https://www.w3schools.com/python/ref_func_any.asp) : 어느 것이라도 보다 큰수가 있으면-> 다시 큐에 넣음
3. 찾고자 하는 위치가 맞을 때까지 카운트를 더해나감 


<details>
    <summary>any()란</summary>
    Definition and Usage
    
    - The any() function returns True if any item in an iterable are true, otherwise it returns False.
    - If the iterable object is empty, the any() function will return False.
</details>


####  풀이 코멘트 포함 2

```python
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)] # 큐 생성
    answer = 0
    while True:
        cur = queue.pop(0) # 비교 대상
        if any(cur[1] < q[1] for q in queue):#어느것이라도 큰 수가 있다면
            queue.append(cur)# 다시 큐에 넣음
        else:
            answer += 1 # 찾고자 하느 위치가 맞을 때까지 카운트 더해나감
            if cur[0] == location:
                return answer

```
