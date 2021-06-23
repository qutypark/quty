---
title: “Programmers_Python_DFS+BFS_정수삼각형"
date: 2021-06-23
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12421)

### 프로그래머스_DFS+BFS_네트워크


- 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return
- 제한 사항
> - 컴퓨터의 개수 n은 1 이상 200 이하인 자연수
> - 각 컴퓨터는 0부터 n-1인 정수로 표현
> - i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현
> - computer[i][i]는 항상 1

#### 풀이 방법
- BFS 
> 탐색 큐와 방문 노드 지정하는 리스트
```python
from collections import deque
def solution(n, com):
    ans = 0
    bfs = deque()
    vis = [0]*n
    while 0 in vis:
        idx = vis.index(0)
        bfs.append(idx)
        vis[idx] = 1 
        
        while bfs: 
            node = bfs.popleft()
            vis[node] = 1
            
            for i in range(n):
                if com[node][i] == 1 and vis[i] == 0: 
                    bfs.append(i)
                    vis[i] = 1
                    
        ans += 1 
    return(ans)

```
> 풀이 코멘트 포함
```python
from collections import deque
def solution(n, com):
    ans = 0 # 네트워크 갯수
    bfs = deque() # 탐색 큐
    vis = [0]*n # 방문 노드
    
    while 0 in vis: # 모든 노드를 다 방문할 때 까지
        idx = vis.index(0) # 방문하지 않은 노드의 인덱스
        bfs.append(idx) # 탐색 대상에 해당 노드를 추가
        vis[idx] = 1 # 해당 노드는 방문한 것으로 처리
        
        while bfs: # "해당 노드"에 대해, 다 탐색할 때 까지
            node = bfs.popleft() # 해당 노드를 꺼냄
            vis[node] = 1 # 방문한 것으로 처리
            
            for i in range(n): # 해당 노드의 "인접 노드"를 방문하기 위해
                if com[node][i] == 1 and vis[i] == 0: # 인접 노드와 연결되어있고, 그 인접노드를 방문하지 않았다면
                    bfs.append(i) # 탐색 대상에 인접 노드를 포함시킴
                    vis[i] = 1 # 그 인접 노드를 방문한 것으로 처리
                    
        ans += 1 # 해당 노드에 대한 네트워크 탐색이 끝났으므로, 갯수 추가
    return(ans)

```
