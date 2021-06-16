---
title: "Programmers_Python_stack+queue_프린터"
date: 2021-06-11
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12081)

{% include adsense.html %}


### 프로그래머스_스택큐_프린터
- 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냄
- 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣음
- 그렇지 않으면 J를 인쇄

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
