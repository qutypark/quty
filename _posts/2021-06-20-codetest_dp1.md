---
title: “Programmers_Python_DP_N으로표현"
date: 2021-06-18
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12263)


### 프로그래머스_동적계획법(DP)_N으로 표현하기
- 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return <br>
- 제한조건: 최솟값이 8보다 크면 -1을 return
#### 풀이방식
1~8동안의 루프에서 만들어지는 수 집합 중, number가 있는 최소 수를 찾아내기


```python
def solution(N, number):
    if number == N: # 자기자신은 자기자신 1개이므로 1 return
        return 1
    ans = 0
    DP = [set() for i in range(8)] # N NN NNN ... 의 집합 생성
    for i, e in enumerate(DP, start=1):
        e.add(int(str(N)*i))
    for i in range(1, 8): # 1부터 7까지(맨 앞 인덱스는 제외)-> 0은 아래의 j루프 불가능
        for j in range(i): 
            for tmp1 in DP[j]:
                for tmp2 in DP[i-j-1]: # 0부터 i-1까지의 모든 인덱스 값의 사칙연산 가능
                    DP[i].add(tmp1 + tmp2)# 사칙연산 +
                    DP[i].add(tmp1 - tmp2)# 사칙연산 -
                    DP[i].add(tmp1 * tmp2)# 사칙연산 *
                    if tmp2 != 0:# 사칙연산 // (DIV/0 error)
                        DP[i].add(tmp1 // tmp2)
        if number in DP[i]: # number에 해당되는 수가 있다면 멈춤(최소)
            ans += i+1 
            break
    else: # 8까지의 집합에 number가 없다면 그 이상이라는 뜻으로 -1을 return
        ans -= 1
    return ans
```
