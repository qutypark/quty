### 프로그래머스_탐욕법(Greedy)_섬연결하기
> n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 
#### 알고리즘: MST (최소신장트리) 중 [Kruskal MST](https://ko.wikipedia.org/wiki/크러스컬_알고리즘)
- 가장 적은 비용으로 모든 노드를 연결하기 위해 사용하는 알고리즘
- 최소 스패닝 트리를 찾음으로써 간선의 가중치의 합이 최솟값이 되도록 하는 알고리즘
- 동작 원리

> 1. 모든 간선들의 가중치를 오름차 순으로 정렬
> 2. 모든 노드를 원소로 갖는 집합 S를 생성
> 3. 가중치가 가장 작은 간선을 선택
> 4. 위에서 선택한 간선이 연결하려는 2개의 노드가 서로 연결되지 않은 상태라면, 2개의 노드를 서로 연결한다.
> 5. 집합 S의 수가 1이 될 때까지 과정을 반복

- 핵심:  사이클이 발생하지 않게 하는 것
> 사이클 생성X: 추가하려는 간선의 양 노드가 같은 집합에 속하지 않는 것<br>
> 이를 위한 판별법: [Union-Find 알고리즘](https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/)

  
```python
def solution(n, costs):
    
    answer = 0
    costs.sort(key=lambda x:x[-1]) # 가중치 오름차순 정렬
    set_S = []

    for i in range(n):
        set_S.append({i}) # 모든 노드를 원소로 갖는 집합 S를 만든다.
    
    for i in costs:  
        temp1 = set()
        temp2 = set()
        for j in set_S: # S가 비어있지 않는 동안
            if i[0] in j:
                temp1 = j
            if i[1] in j:
                temp2 = j
        if temp1 == temp2: # 2개의 노드가 연결된 상태
            continue
        else: # 2개의 노드가 연결되어 있지 않다면
            set_S.remove(temp1) # 집합 S에서 해당 노드를 버리고
            set_S.remove(temp2)
            set_S.append(temp1|temp2) # 2개의 노드를 서로 연결한다.
            answer += i[2]
            if len(set_S) == 1: # 집합 S의 수가 1이 되면 멈춘다.
                break

    return answer
```

>참고
>> https://velog.io/@minidoo/알고리즘-탐욕법Greedy-프로그래머스-3단계-섬-연결하기
