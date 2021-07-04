---
title: “Programmers_Python_DP_도둑질"
date: 2021-06-20
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/lessons/42897)


### 프로그래머스_동적계획법(DP)_도둑질
- 각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보 울림.
- 각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 
- 제한 조건:   모든 집들은 동그랗게 배치되어 있음 = **첫번째 집과 마지막 집은 서로 인접**

#### 풀이방법
> [동적계획법](https://ko.wikipedia.org/wiki/동적_계획법)
>> 일반적으로 주어진 문제를 풀기 위해서, 문제를 여러 개의 하위 문제(subproblem)로 나누어 푼 다음, <br>
>> 그것을 결합하여 최종적인 목적에 도달하는 것이다. 
> - 첫번째 집 털 경우 / 첫번째 집을 털지 않을 경우  로 나누어야 함
> - 재귀를 이용해야 함
>> 1. i-1 집을 털었다면, i 집은 털지 못함 = i-1 째 집까지 턴 금액의 합산이 됨 = dp[i-1]
>> 2. i-1 집을 털지 않았다면, i 집 가능 = i-2 째 집까지 턴 금액과(= dp[i-2]) i 집의 합산
>> 3. 이를 dp [] 를 통해 재귀 완성


```python
def solution(home):
    # 첫번째 집 털 경우 = 마지막 집은 포함하지 않음
    dp1 = [0] * len(home)
    # 2번째 집은 못터므로, 첫번째 집 값으로 유지
    dp1[0], dp1[1] = home[0], home[0]
    for i in range(2, len(home)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+home[i])

    # 첫번째 집을 털지 않을 경우 = 마지막 집도 포함
    dp2 = [0] * len(home)
    dp2[1] = home[1]
    for i in range(2, len(home)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + home[i])
    return max(max(dp1), max(dp2))
```
