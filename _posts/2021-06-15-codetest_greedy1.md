---
title: “Programmers_Python_greedy_camera"
date: 2021-06-15
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12244)


### 프로그래머스_탐욕법(Greedy)_단속카메라
> 고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return
#### 풀이방법
: 각 구간을 모두 검사
> 1. 차량을 도입 시점(x[0]) 기준으로 정렬
> 2. 차량의 진출(x[1])시점이 뒷 차량 도입 시점보다 후 시점인 한,<br>
>   2.1 같은 카메라가 유지됨<br>
>   2.2 진출 시점은 현재 탐색한 차량 중 가장 빠른 진출 시점으로 갱신<br>
> 3. 차량의 진출시점이 뒷 차량 도입 시점보다 빠르다면,<br>
>   3.1 더 이상 같은 카메라로 유지가 안됨<br>
>   3.2 진출시점은 뒷 차량 진출 시점으로 갱신

  
```python
def solution(rut):
    rut.sort(key=lambda x: x[0]) # 1. 차량을 도입 시점(x[0]) 기준으로 정렬
    p = rut.pop(0)
    right = p[1] # 맨 처음 차량의 진출 시점
    ans = 1

    for i in rut:
        if i[0] <= right: # 차량의 진출(x[1])시점이 뒷 차량 도임 시점보다 후시점
            ans += 0 # 같은 카메라 유지
            right = min(i[1], right) #진출 시점은 현재 탐색한 차량 중 가장 빠른 진출 시점으로 갱신
        else: #차량의 진출시점이 뒷 차량 도입 시점보다 빠르다면,
            ans += 1  #더 이상 같은 카메라로 유지가 안됨
            right = i[1] # 진출시점은 뒷 차량 진출 시점으로 갱신

    return ans
```


