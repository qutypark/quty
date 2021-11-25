---
title: “Programmers_Python_greedy_구명보트"
date: 2021-06-18
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12244)

{% include adsense.html %}

### 프로그래머스_탐욕법(그리디)_구명보트

> 사람들의 몸무게를 담은 배열 people / 구명보트의 무게 제한 limit<br>
  ->  모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값 return.<br>
>
> 제한조건<br>
> - 구명보트는 한 번에 "최대 2명"씩 밖에 탈 수 없음
> - 예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 
> - 구명보트의 무게 제한이 100kg이라면  2번째 사람과 4번째 사람은 같이 탈 수 있지만<br>
> - 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 <br>
>   구명보트의 무게 제한을 초과하여 같이 탈 수 없음

```python
def solution(pe, li):
    pe.sort() # 오름차순 정렬
    ans = 0
    left = 0
    right = len(pe)-1
    while left < right: # 인덱스 값을 조정해나가며 리미트 값과 비교(최대 2명이므로, left right)
        if (pe[left]+pe[right]) <= li:
            left += 1
            right -= 1
        else:
            right -= 1
        ans += 1 # 아니면 아닌대로, 맞으면 맞는대로 보트수가 필요함
    if left == right:
        ans +=1 # 리미트 값에 맞는 2명이 존재하지 않다는 의미-> +1

    return ans
```
