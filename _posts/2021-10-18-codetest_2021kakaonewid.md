---
title: “Programmers_Python_2021 KAKAO BLIND RECRUITMENT_신규 아이디 추천"

date: 2021-10-18
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/lessons/72410)


### 2021 KAKAO BLIND RECRUITMENT_신규 아이디 추천

#### 정규식

```python
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
```

#### 규칙대로

```python
def solution2(new_id):
    pos = [".", "-", "_"]
    # step 1
    new_id = new_id.lower()
    answer = ""

    # step 2
    for i in new_id:
        if i in pos or i.isalnum():
            answer += i
    # step 3
    answer += ' '
    for i, c in enumerate(answer):
        if i <= len(answer) - 1:
            while answer[i] == '.' and answer[i + 1] == '.':
                answer = answer[:i] + answer[i + 1:]
    answer = answer[:-1]
    if answer[0] == '.' and len(answer) == 1:
        answer = ''
    elif answer[0] == '.':
        answer = answer[1:]
    elif answer[-1] == '.':
        answer = answer[:-1]

    # step 4, 5, 6, 7

    if len(answer) == 0:
        answer = "a" * 3
    else:
        answer = answer[:15]

    while answer[-1] == ".":
        if answer[-1] == ".":
            answer = answer[:-1]
    if len(answer) <= 2:
        last = answer[-1]
        while len(answer) < 3:
            answer += last
    return answer
```
