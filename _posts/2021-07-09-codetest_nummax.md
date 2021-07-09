---
title: “Programmers_Python_모든문제_수식 최대화"
date: 2021-07-09
categories: Algorithms
---

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/67257)

연산 수식이 담긴 문자열 expression이 매개변수로 주어질 때,<br> 
우승 시 받을 수 있는 가장 큰 상금 금액을 return

<details>
  <summary>문제 설명</summary>

#### 입출력 예 #1<br>
[* , +, -] 로 연산자 우선순위를 정했을 때, 가장 큰 절댓값을 얻을 수 있습니다.<br>
연산 순서는 아래와 같습니다.<br>
 <br>
100-200*300-500+20<br>
= 100-(200*300)-500+20<br>
= 100-60000-(500+20)<br>
= (100-60000)-520<br>
= (-59900-520)<br>
= -60420<br>
<br>
따라서, 우승 시 받을 수 있는 상금은 |-60420| = 60420 입니다.

</details>


### 문제풀이1
1. 연산자 순열
2. 최대값을 구하는 완전탐색

#### 코드

```python
from itertools import permutations


def solution(ex):
    # 수식을 숫자 / 연산자 로 분리하여 저장
    org, tmp = [], ''
    for i, e in enumerate(ex):
        if e != "*" and e != "+" and e != "-":
            tmp += e
        if e == "*" or e == "+" or e == "-":
            org.append(int(tmp))
            org.append(e)
            tmp = ''
        elif i == len(ex)-1:
            org.append(int(tmp))
    # 연산자 순열
    cal = list(map(list, permutations(["*", "+", "-"])))
    ans = 0
    # 완전 탐색
    for clis in cal:
        lis = org.copy()
        while clis:
            c = clis.pop(0)
            if c in lis:
                while c in lis:
                    idx = lis.index(c)
                    left = lis[idx-1]
                    right = lis[idx+1]
                    if c == "*":
                        tmp = left * right
                    if c == "+":
                        tmp = left + right
                    if c == "-":
                        tmp = left - right
                    lis.insert(idx+2, tmp)
                    lis.pop(idx)
                    lis.pop(idx-1)
                    lis.pop(idx-1)
                    if c not in lis:
                        break

        mx = abs(lis[0])
        # 최댓값 출력
        ans = max(ans, mx)
    return ans
```

### 문제풀이 2
1. 연산자 순열
2. [EVAL](https://www.programiz.com/python-programming/methods/built-in/eval) 을 통해, 문자열을 계산식으로 변환
* Eval이란: 문자열도 수식으로 사용 가능

#### 코드

```python
def solution(expression):
# 연산자 순열
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        # EVAL 로 계산할 문자열을 담을 리스트 생성
        temp_list = []
        # 첫번째 우선순위 연산으로 분할
        for e in expression.split(a):
            # 두번째 우선순위 연산자로 분할하여 괄호로 묶음
            temp = [f"({i})" for i in e.split(b)]
            # 두번째 우선순위 연산자를 기준으로 분할된 괄호열들을 join
            temp_list.append(f'({b.join(temp)})')
        # 첫번째 우선순위 연산자를 기준으로 분할된 괄호열들을 join 후, EVAL
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)
```
