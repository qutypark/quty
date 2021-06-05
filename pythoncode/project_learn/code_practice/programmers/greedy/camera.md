### 프로그래머스_탐욕법(Greedy)_단속카메라
> 고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return
#### 각 구간을 모두 검사
> 1. 차량을 도입 시점(x[0]) 기준으로 정렬
> 2. 차량의 진출(x[1])시점이 앞 차량 도입 시점보다 전 시점인 한,<br>
>   2.1 같은 카메라가 유지됨<br>
>   2.2 도입 시점은 가장 느린 도입 시점으로 유지됨<br>
> 3. 차량의 진출시점이 앞 차량 도입 시점보다 느리다면,<br>
>   3.1 더 이상 같은 카메라로 유지가 안됨<br>
>   3.2 도입 시점은 해당 차량의 진출 시점으로 갱신

  
```python
def solution(rut):
    rut.sort(key=lambda x: x[0])
    p = rut.pop(0)
    right = p[1]
    ans = 1

    for i in rut:
        if i[0] <= right:
            ans += 0
            right = min(i[1], right)
        else:
            ans += 1
            right = i[1]

    return ans
```


