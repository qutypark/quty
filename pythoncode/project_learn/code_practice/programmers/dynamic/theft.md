### 프로그래머스_동적계획법(DP)_도둑질
- 각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보 울림.
- 각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 
- 제한 조건:   모든 집들은 동그랗게 배치되어 있음 = **첫번째 집과 마지막 집은 서로 인접**

#### 풀이방법
- 첫번째 집 털 경우 / 첫번째 집을 털지 않을 경우  로 나누어야 함

```python
def solution(home):
    # 첫번째 집 털 때
    dp1 = [0] * len(home)
    # 2번째 집은 못터므로, 첫번째 집 값으로 유지
    dp1[0], dp1[1] = home[0], home[0]
    for i in range(2, len(home)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+home[i])

    # 마지막 집 털 때
    dp2 = [0] * len(home)
    dp2[1] = home[1]
    for i in range(2, len(home)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + home[i])
    return max(max(dp1), max(dp2))
```
