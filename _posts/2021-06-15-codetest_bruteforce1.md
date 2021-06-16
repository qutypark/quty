---
title: “Programmers_Python_bruteforce_primenumber"
date: 2021-06-15
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12230)


{% include adsense.html %}


### 프로그래머스_완전탐색_소수 찾기

- 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 

#### 풀이방법
> 1. [에라토스테네스의 체](https://ko.wikipedia.org/wiki/에라토스테네스의_체)

```python
from itertools import permutations

def solution(num):
    # 1. 만들 수 있는 모든 수의 조합
    lis = []
    for i in range(1, len(num)+1):
        a = list(permutations(num, i))
        for e in a:
            t = int(''.join(e))
            if t not in lis:
                lis.append(t)

    # 2. 소수의 리스트를 만듦: (에라토스테네스의 체)를 통해
    m = max(lis)
    
    sieve = [True] * (m+1)
    
    n = int(m**0.5) # m의 최대 약수가 sqrt(m) 이하이므로 i=sqrt(m)까지 검사
    for i in range(2, n+1): 
        if sieve[i] == True: # 소수일 때
            for j in range(2*i, m+1, i): # 해당 소수의 배수는 FALSE
                sieve[j] = False
    primes = [i for i in range(2, m+1) if sieve[i]==True]

    # 최종. 만들 수 있는 모든 수 조합 중 소수 리스트에 해당되는 카운트
    cnt = 0
    for e in lis:
        if e in primes:
            cnt += 1
    return cnt
```
