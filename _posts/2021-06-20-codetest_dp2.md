---
title: “Programmers_Python_DP_등굣길"
date: 2021-06-20
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12263)

### 프로그래머스_동적계획법(DP)_등굣길
- 격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수. 
- 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return.
- 제한 조건: 오른쪽 아래쪽으로만 움직임

#### 풀이방법 
> [동적계획법](https://ko.wikipedia.org/wiki/동적_계획법)
>> 문제를 여러 개의 하위 문제(subproblem)로 나누어 푼 다음, <br>
>> 그것을 결합하여 최종적인 목적에 도달하는 것이다
> - 최단거리 갯수 구하는 공식 중 [**1,1,1 법칙**](https://namu.wiki/w/최단거리) 응용
> - 출발지점(1,1)과 같은 행, 열 지점의 최단 거리 갯수는 무조건 1 
> - 웅덩이의 행과 열이 1이면 <br>
     -> 1행의 모든 열 / 1열의 모든 행은 가지 못함

```python
def solution(m, n, pud):
    dp_matrix = [[1] * m for _ in range(n)] #1,1,1 법칙
    
    for p in pud: # 웅덩이 행, 열이 1이면, 그 행의 모든 열, 그 열의 모든 행은 가지 못함 
        if p[0] == 1: 
            for k in range(p[1]-1, n):
                dp_matrix[k][0] = 0
        if p[1] == 1:
            for k in range(p[0]-1, m):
                dp_matrix[0][k] = 0
        dp_matrix[p[1] - 1][p[0] - 1] = 0 # 웅덩이도 0
    for i in range(n):
        for j in range(m):
            if i>0 and j>0: #출발선과 같은 행, 열, 못가는 지점 제외하고 갯수 합 더함
                if dp_matrix[i][j] > 0: 
                    dp_matrix[i][j] = dp_matrix[i-1][j]+dp_matrix[i][j-1]
    final = dp_matrix[n-1][m-1] #도착 지점의 값 -> 총 갯수
    
    return final % 1000000007
```
