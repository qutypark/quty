### 프로그래머스_python_그래프_순위

[문제링크](https://programmers.co.kr/learn/courses/30/parts/14393)


- 선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 <br>
  정확하게 순위를 매길 수 있는 선수의 수를 return
  
#### 풀이방법
> 그래프 탐색
>> - 부모 노드 갯수와 자식 노드의 갯수의 합이 선수의 수(n)-1 인 노드
>> - 비트연산을 통해 부분집합 산출
```python
from collections import defaultdict

def solution(n, res):
    win = defaultdict(set)
    lose = defaultdict(set)
    for r in res:
        win[r[0]].add(r[1])
        lose[r[1]].add(r[0])
    for i in range(1, n+1):
        # 자식 노드
        for w in win[i]:
            lose[w] |= lose[i]
        # 부모 노드
        for l in lose[i]:
            win[l] |= win[i]
    ans = 0
    for i in range(1, n+1):
        # 부모 노드와 자식 노드의 합이 n-1인 노드
        if len(win[i])+len(lose[i])==n-1:
            ans += 1
    return ans
```
