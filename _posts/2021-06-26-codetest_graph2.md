---
title: “Programmers_Python_그래프_가장 먼 노드"
date: 2021-06-26
categories: Algorithms
---


> [문제링크](https://programmers.co.kr/learn/courses/30/parts/14393)


### 프로그래머스_python_graph_가장 먼 노드

- 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, <br>
  1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return.
- 제한사항
> - 노드의 개수 n은 2 이상 20,000 이하
> - 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선
> - vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미.

#### 풀이방법
> BFS 

```python
from collections import defaultdict
from collections import deque

# bfs로 탐색 및 1부터의 거리누적
def bfs(graph, start, distances):
    q = deque([start])
    vis= set([start])

    while que:
        current = q.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                distances[neighbor] = distances[current] + 1

def solution(n, edge):
    # 그래프 만들기
    graph = defaultdict(list)
    # 간선은 양방향
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # bfs 탐색 (거리 누적은 0부터 시작)
    distances = [0]*(n+1)
    bfs(graph, 1, distances)
    
    # 최대 거리 계산 후, 그 거리를 가진 노드 개수
    max_distance = max(distances)
    ans = 0 
    for d in distances:
        if d == max_distance:
            answer += 1

    return answer
```
>>  실패 코드
>>> 풀이방식은 bfs로 비슷하나, dictionary중복사용으로 시간효율 X

```python

from collections import defaultdict

def solution(n, vertex):
    vertex.sort(key=lambda x: x[0])

    grph = defaultdict(list)
    save = dict()
    for v in vertex:
        grph[v[0]].append(v[1])
        grph[v[1]].append(v[0])
        
    org = grph.pop(1)
    lis = org.copy()
    while lis:
        i = lis.pop()
        if i not in save:
            if i not in org:
                save[i] = 1
            else:
                save[i] = 0
        tmp = grph.pop(i)
        for t in tmp:
            if t not in org:
                try:
                    save[t] += 1
                except:
                    save[t] = 1
                if t in grph:
                    lis.append(t)
        if not lis:
            if grph:
                lis.append(list(grph.keys())[0])
            else:
                break
    m = max(list(save.values()))
    ans = [i for i in list(save.keys()) if save[i]==m]
    return len(ans)

```
