### 프로그래머스_python_이분탐색_입국심사
[문제링크](https://programmers.co.kr/learn/courses/30/parts/12486)

- 입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때,<br>
  모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return
  
#### soltuion
- binary search
> 1. sum(mid (=추정 시간) / 각 심사위원의 심사 시간) = 심사 가능한 인원 수
> 2. 추정 시간(mid) = 최소시간(시작 = 1) 과 최대시간(시작 = 가장 긴 시간 * 인원 수) 의 중앙값
> 2. 심사 가능한 인원 수가 n명과 같아질 때까지 추정 시간(mid)를 줄여/늘려 나감
  
```python

def solution3(n, time):
    time.sort()
    mn, mx = 1, time[-1]*n
    ans = mx
    while mn <= mx:
        mid = (mn+mx)//2
        f_num = sum(mid // t for t in time)
        if f_num >= n:
            if ans >= mid: # 최솟값을 구하기 위해 작은 값으로 갱신
                ans = mid
            mx = mid-1 # 시간효율성을 위해, mid-1 로 갱신
        else:
            mn = mid+1 # 시간효율성을 위해, mid+1 로 갱신
    return ans

```
