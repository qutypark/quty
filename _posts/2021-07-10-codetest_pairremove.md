---
title: “Programmers_Python_모든문제_짝지어제거하기"
date: 2021-07-10
categories: Algorithms
---

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/12973)

{% include adsense.html %}

### 프로그래머스_모든문제_짝지어제거하기

문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수<br>
성공: return 1 / 아닐 경우: return 0<br>

예를 들어, 문자열 S = baabaa 라면

b aa baa → bb aa → aa →

의 순서로 문자열을 모두 제거할 수 있으므로 return 1


### 풀이방법
1. 효율성: 애초에 문자열 수가 짝수가 아니면 return 0
2. 짝지어 제거할 대상을 스택에 저장
3. 다 탐색 후 스택이 비지 않으면 return 0

#### 코드

```python
def solution(s):
    i = 0
    stack = []
    if len(s) % 2 > 0:
        return 0
    else:
        while i < len(s):
            stack.append(s[i])
            if len(stack) >= 2:
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
            i += 1
            if i == len(s):
                break
    if not stack:
        return 1
    else:
        return 0
```

