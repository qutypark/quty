---
title: “Programmers_Python_그래프_방의 갯수"
date: 2021-07-01
categories: Algorithms
---


> [문제링크](https://programmers.co.kr/learn/courses/30/lessons/49190)


### 프로그래머스_python_graph_방의 갯수

<img src="https://grepp-programmers.s3.amazonaws.com/files/ybm/ec8f232bf0/a47a6c2e-ec84-4bfb-9d4b-ff3ba589b42a.png" width="35%" height="35%">

<details>
    <summary>문제 설명</summary>
    
ex) 1일때는 오른쪽 위로 이동
그림을 그릴 때, 사방이 막히면 방하나로 샙니다. <br>
이동하는 방향이 담긴 배열 arrows가 매개변수로 주어질 때, 방의 갯수를 return <br>
- 제한사항
    
>배열 arrows의 크기는 1 이상 100,000 이하 입니다.<br>
>arrows의 원소는 0 이상 7 이하 입니다.<br>
>방은 다른 방으로 둘러 싸여질 수 있습니다.<br>
    
- 예시
    
<img src="https://grepp-programmers.s3.amazonaws.com/files/ybm/74fd8df438/22a1ee81-75a6-4220-bd15-6230e35e2931.png" width="35%" height="35%">
    
- (0,0) 부터 시작해서 6(왼쪽) 으로 3번 이동합니다. 
- 그 이후 주어진 arrows 를 따라 그립니다.
- 삼각형 (1), 큰 사각형(1), 평행사변형(1) = 3

    
</details>


### 풀이 방식
[오일러 정리](https://ko.wikipedia.org/wiki/오일러_다면체_정리)를 응용해야 하는 문제
>   V : 꼭지점 개수, E: 선의 갯수, F: 면의 개수<br>
>   F가 바로 구해야 할 방의 갯수<br>

>   수학적 지식을 요하는 문제로,<br>
>   선과 선의 교차로 생기는 방의 개수까지 계산해야 하므로 까다로운 문제<br>
>   ** 2차원에서의 v-e+f = 1

#### 다른 사람의 풀이

```python

def solution(arrows):
    point=set([(0,0)])
    line=set()
    move=[[0,2],[2,2],[2,0],[2,-2],[0,-2],[-2,-2],[-2,0],[-2,2]] 
    pre_point=(0,0)
    for A in arrows:
        next_point=(pre_point[0]+move[A][0],  pre_point[1]+move[A][1] )
        mid_point=(pre_point[0]+move[A][0]//2,  pre_point[1]+move[A][1]//2 ) # 교차 지점을 위해
        point.add(next_point) #V
        point.add(mid_point) #V
        line.add((pre_point,mid_point)) #E
        line.add((mid_point,pre_point)) #E
        line.add((mid_point,next_point)) #E
        line.add((next_point,mid_point)) #E
        pre_point=next_point
    answer = len(line)//2-len(point)+1 # v-e+f = 1 -> f = e-v+1
    return answer if answer>=0 else 0
```


