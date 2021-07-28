---
title: “Programmers_Python_모든문제_영어끝말잇기"
date: 2021-07-28
categories: Algorithms
---

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/12981)


### 프로그래머스_모든문제_영어끝말잇기
Summer/Winter Coding(~2018)

사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, <br>
가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 

### 문제설명
1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있습니다. <br>
영어 끝말잇기는 다음과 같은 규칙으로 진행됩니다.<br>
<br>
> - 1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
> - 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
> - 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
> - 이전에 등장했던 단어는 사용할 수 없습니다.
> - 한 글자인 단어는 인정되지 않습니다.
> - 탈락자가 발생하지 않으면, [0, 0]을 return하면 됩니다.

다음은 3명이 끝말잇기를 하는 상황을 나타냅니다.
<br>
tank → kick → know → wheel → land → dream → mother → robot → tank


끝말잇기를 계속 진행해 나가다 보면, <br>
3번 사람이 자신의 세 번째 차례에 말한 tank 라는 단어는 이전에 등장했던 단어이므로 탈락하게 됩니다.


### 풀이설명
- 완전탐색
- 틀린 단어 인덱스의 몫과 나머지로 번호 및 차례를 구할 수 있음

```python
def solution(n, words):
    ans = []
    for i in range(1, len(words)):
        j = i - 1
        if words[j][-1] != words[i][0] or words[i] in words[:j]:
            a = (i + 1) % n
            b = (i + 1) // n
            if a > 0:
                ans.append(a)
                ans.append(b + 1)
            else:
                ans.append(n)
                ans.append(b)
            break
        else:
            if i == len(words) - 1:
                ans.append(0)
                ans.append(0)
    return ans
```

