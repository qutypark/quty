---
title: “Programmers_Python_모든문제_삼각달팽이"
date: 2021-08-18
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/lessons/68645)

{% include adsense.html %}

### 프로그래머스_모든문제_삼각달팽이
월간코드 챌린지 시즌 1

### 문제 설명

정수 n이 매개변수로 주어짐. <br>
밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, <br>
첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return.

<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/e1e53b93-dcdf-446f-b47f-e8ec1292a5e0/examples.png" width="50%" height="50%" />

### 풀이 방식

삼각형이므로, 둘레를 '3번' 탐색하며 좌표에 들어갈 값을 생성

1. 삼각형 배열을 생성
2. 좌표를 구성
3. 삼각형 배열을 탐색하며 해당 좌표를 지정
4. 해당 좌표에 대한 값을 지정

#### 1. 삼각형 배열
n = 4 일 경우,아래와 같은 리스트들로 구성된 리스트<br>
[[0] [0,0] [0,0,0] [0,0,0,0]]

#### 2. 좌표를 구성 (x,y)
좌표, 즉 위 삼각형 배열의 인덱스<br>
n = 4 일 경우,아래와 같이 삼각형 및 인덱스로 구성됨<br>

[0,0] = (첫번째 리스트의 첫번째 값)<br>
[1,0][1,1]<br>
[2,0][2,1][2,2]<br>
[3,0][3,1][3,2][3,3]<br>

#### 3. 삼각형 배열을 탐색하며 해당 좌표를 지정

> 둘레가 0(1)번째 일때는 아래로 탐색<br>
> 둘레가 1(2)번째 일때는 오른쪽으로 탐색<br>
> 둘레가 2(3)번째 일때는 위로 탐색<br>

즉<br> 
i%3=0 -> x += 1<br>
i%3=1 -> y += 1<br>
i%3=2 -> x -= 1, y -= 1

#### 4. 해당 좌표에 대한 값을 지정

탐색해나가며 1씩 더해나감

### 코드 구현

```python
def solution(n):
    # 1.삼각형 배열
    ans = [[0]*i for i in range(1, n+1)]
    # 2. 좌표 구성
    x, y = -1, 0
    # 4. 해당 값
    num = 1
    
    # 3. 삼각형 배열을 탐색하며 해당 좌표를 지정
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            #4. 해당 좌표에 값을 지정
            ans[x][y] = num
            num += 1
    res = []
    for lis in ans:
        for l in lis:
            res.append(l)
    return res
```







