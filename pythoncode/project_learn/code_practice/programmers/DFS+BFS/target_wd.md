### 프로그래머스_DFS+BFS_단어변환
- 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, <br>
  최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return .
- 제한조건
> 1. 한 번에 한 개의 알파벳만 바꿀 수 있음.<br>
> 2. words에 있는 단어로만 변환할 수 있음.

#### 풀이방식
- DFS
> 1. 방문체크 리스트<br>
> 2. 비교대상 갱신용 리스트

```python
def solution(begin, target, wd):
    if target not in wd:
        return 0
    ans = 0
    vis = [0]*len(wd) # 방문
    curr = [begin]    # 비교 대상을 갱신할 리스트
    while curr:
        c = curr.pop() # 비교 대상 갱신
        if c == target:
            return ans
        for i, e in enumerate(wd):
            cnt = 0
            for a, b in zip(c, e): # 같은 단어의 수 count
                if a == b:
                    cnt += 1
            if vis[i] == 0: # 방문하지 않았다면
                if cnt == len(e)-1: # 1밖에 차이가 나지 않을 때
                    vis[i] = 1  # 방문 체크 후
                    curr.append(e) # 비교 대상 갱신
        ans+=1
```
