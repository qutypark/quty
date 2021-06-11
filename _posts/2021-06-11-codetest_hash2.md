---
title: "Programmers_Python_Hash_전화번호목록"
date: 2021-06-11
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12077)

### 프로그래머스_해쉬_전화번호목록
- 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return
- pb = ["97674223", "119", "1195524421"]

#### 풀이방식
- startswith 함수 이용
```python
def solution(pb):
    # 1. 정렬
    pb = sorted(pb)
    # 2. 전 요소가 그 후 요소의 접두어가 되는지를 확인
    for p1, p2 in zip(pb, pb[1:]):
        if p2.startswith(p1):
            return False
    return True
```

