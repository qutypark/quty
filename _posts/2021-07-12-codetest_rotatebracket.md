---
title: “Programmers_Python_모든문제_괄호회전하기"
date: 2021-07-12
categories: Algorithms
---

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/76502)


### 프로그래머스_모든문제_괄호회전하기

(), [], {} 는 모두 올바른 괄호 문자열입니다.<br>

대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. <br>

이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 <br>
올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.<br>


### 풀이방법
1. 괄호요소를 스택에 쌓아, 올바른 괄호인지 탐색 함수
2. 문자열을 회전시키며, 탐색 함수 실행

#### 코드

```python

def valid(words):
    dic = {'[': ']', '(': ')', '{': '}'}
    stack = []
    for w in words:
        if not stack:
            stack.append(w)
        elif stack[-1] in dic.keys():
            if w == dic[stack[-1]]:
                stack.pop()
            else:
                stack.append(w)
    if stack:
        return False
    else:
        return True

def solution(s):
    ans = 0
    for i in range(len(s)):
        words = s[i:] + s[:i] # 회전
        if valid(words):
            ans += 1
    return ans

```
