---
title: “Programmers_Python_모든문제_이진변환반복하기"
date: 2021-08-20 
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/lessons/70129)

{% include adsense.html %}

### 프로그래머스_모든문제_이진변환 반복하기
월간코드 챌린지 시즌 1

### 문제 설명

0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환<br>

1. x의 모든 0을 제거합니다.
2. x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
3. 예를 들어, x = "0111010"이라면, 
> x = "0111010" -> "1111" -> "100" 이 됩니다.
<br>
s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때,<br>
이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return

#### 예시

|s   |result   |
|---|---|
|"110010101001"|[3,8]|
|"01110"|[3,3]|
|"1111111"|[4,1]|


### 풀이(코드)
```python
def solution(s):
    cnt, zero = 0, 0
    while True:
        n = len(s)
        z = s.count('0')
        zero += z
        s = str(bin(n-z)[2:])
        cnt += 1
        if s == '1':
            break
    return [cnt, zero]
```
