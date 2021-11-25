---
title: “Programmers_Python_모든문제_게임 맵 최단거리"
date: 2021-06-29
categories: Algorithms
---


> [문제링크](https://programmers.co.kr/learn/courses/30/lessons/1844)

{% include adsense.html %}

### 프로그래머스_모든문제_게임맵최단거리

<details>
  <summary>문제 설명</summary>
  
  게임 맵의 상태 maps가 매개변수로 주어질 때, <br>
  캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return<br>
  단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return<br>

  > 제한사항<br>
  >> 캐릭터가 움직일 때는 동, 서, 남, 북 방향으로 한 칸씩 이동하며, 게임 맵을 벗어난 길은 갈 수 없습니다.<br>
  >> - maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1 이상 100 이하의 자연수<br>
  >> - n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.<br>
  >> - maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.<br>
  >> - 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1),  상대방 진영은 게임 맵의 우측 하단인 (n, m) <br>
</details> 

#### Solution
> BFS + Deque
>> - 동서남북으로의 위치를 계산
>> - 처음 위치를 기준으로 탐색 큐 생성
>> - 갈 수 있는 블록 = '1' -> 이를 다 더하면 블록 갯수 = 즉 거리
>> - 방문 집합을 통해 시간 효율성 향상

```python

# map = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]


from collections import deque

def solution(map):
    N, M = len(map), len(map[0])
    start = [0, 0, 1]
    direct = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    vis = set((0, 0))
    search = deque([start])
    while search:
        x, y, cnt = search.popleft()
        for i in range(len(direct)):
            tmx, tmy = x+direct[i][0], y+direct[i][1]
            if tmx == N-1 and tmy == M-1:
                return cnt+1
            elif 0 <= tmx < N and 0 <= tmy < M and map[tmx][tmy]:
                if (tmx, tmy) not in vis:
                    search.append([tmx, tmy, cnt+1])
                    map[x][y] = 0
            vis.add((tmx, tmy))
    return -1
```


> 풀이 코멘트 포함


```python

# map = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]


from collections import deque

def solution(map):
    N, M = len(map), len(map[0])
    start = [0, 0, 1] # 시작 위치
    direct = [(0, 1), (1, 0), (-1, 0), (0, -1)] # 동서남북
    vis = set((0, 0)) # 방문 위치 집합
    search = deque([start]) # 탐색 큐
    while search:
        x, y, cnt = search.popleft()
        for i in range(len(direct)):
            tmx, tmy = x+direct[i][0], y+direct[i][1] # 동서남북 위치 계산
            if tmx == N-1 and tmy == M-1: # 해당 진영에 도착했다면
                return cnt+1 # 거리 return
            elif 0 <= tmx < N and 0 <= tmy < M and map[tmx][tmy]: # 도착 전이고 게임 맵 범위에 있다면
                if (tmx, tmy) not in vis:# 방문하지 않은 블록만 탐색 대상에 포함
                    search.append([tmx, tmy, cnt+1])
                    map[x][y] = 0 # 해당 블록은 계산 후. 므로 0으로 표시
            vis.add((tmx, tmy)) # 방문에 포함
    return -1
```
