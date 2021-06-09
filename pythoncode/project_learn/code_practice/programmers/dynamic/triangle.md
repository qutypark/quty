### 프로그래머스_동적계획법(DP)_정수 삼각형
- 삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return.
- 제한조건:아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능

#### 풀이방식
1. 모서리 조건: 윗층 리스트 중 인덱스가 같은 값만 더할 수 있음<br>
2. 중간에 위치한 값들은, 바로 윗층 리스트에서 인덱스가 1개 전 혹은 같은 값 중 최대값을 선택 가능<br>
3. 다 더한 후, 최종 층의 최댓값을 출력

```python
def solution(tri):
    for i in range(1, len(tri)):
        if len(tri[i]) <= 2: # 두번째 층이면 첫번째 층 1개의 값만 더할 수 있음
            tri[i] = [(tri[i][0]+tri[i-1][0]), tri[i][-1]+tri[i-1][0]]
        else:
            for j in range(len(tri[i])):
                if j == 0: # 모서리
                    tri[i][j] += tri[i-1][j]
                elif j == len(tri[i])-1: # 모서리
                    tri[i][j] += tri[i-1][-1]
                else: # 중간 값은, 윗 층 값에서 최댓값 선택해서 더함
                    m = max(tri[i-1][j-1], tri[i-1][j])
                    tri[i][j] += m
    return max(tri[-1]) # 최종 층의 최댓값 출력
```
> ### 다른 사람의 풀이<br>
> 풀이방식<br>
>> 1. 한 층을 제거한 traingle을 첫번째 input, 이동거리 배열을 두 번째 input으로 넣어줌<br>
>> 2. [0] + l, l + [0] 을 이용하여 모서리 조건을 해결.
```python
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
```
