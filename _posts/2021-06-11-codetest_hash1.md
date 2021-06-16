---
title: "Programmers_Python_Hash_완주하지못한선수"
date: 2021-06-11
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12077)

{% include adsense.html %}


### 프로그래머스_해쉬_완주하지못한선수
- 완주하지 못한 선수를 찾아냄(완주하지 못한 선수는 1명)
- 참가선수(part): ["leo", "kiki", "eden"]
- 완주선수(com): ["eden", "kiki"]
- 완주 못한 선수(정답): 'leo'

#### 풀이방식
- dictionary를 이용

```python
def solution(part, com):
    dic = dict()
    for p in part:
        if p not in dic:
            dic[p] = 1
        else:
            dic[p] += 1
    for c in com:
        dic[c] -= 1

    for k,v in dic.items():
        if v > 0:
            return k
``` 

