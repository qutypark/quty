---
title: "Programmers_Python_Hash_위장"
date: 2021-06-11
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12077)


{% include adsense.html %}


### 프로그래머스_해쉬_위장

- 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return
- clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

#### 풀이방식
- 조합: (a+1)(b+1)(c+1)
- 위 조합에서 1 뺌 (1은 아무것도 입지 않았을 경우)
- Counter을 이용

```python
from collections import Counter

def solution(clothes):
    answer = 1
    c = Counter([x[1] for x in clothes])
    for v in c.values():
        answer *= (v+1)
    answer -= 1
    return answer
```
