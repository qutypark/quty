---
title: "Programmers_Python_Hash_전화번호목록"
date: 2021-06-11
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/lessons/42577)

{% include adsense.html %}

### 프로그래머스_해쉬_전화번호목록
- 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return
- *해쉬 문제지만 다른 알고리즘으로도 풀이 가능

### (다른 사람 풀이 참고)풀이방식
1. [startswith](https://www.w3schools.com/python/ref_string_startswith.asp)함수 이용

- 정렬 -> 인접한 요소만 비교하도록
- startswith를 이용하여 접두어가 되면 False 출력

#### 코드_1

```python
# pb = ["97674223", "119", "1195524421"]
def solution(pb):
    # 1. 정렬
    pb = sorted(pb)
    # 2. 전 요소가 그 후 요소의 접두어가 되는지를 확인
    for p1, p2 in zip(pb, pb[1:]):
        if p2.startswith(p1):
            return False
    return True
```
### (다른 사람 풀이 참고)풀이방식
2. HashKey

- 각 전화번호를 해쉬키로 작성
- 스트링 요소를 더해나가는 tmp 빈 문자열 생성
- tmp가 해쉬키에 포함되고, 해당요소와는 같지 않다면(더 짧음)<br>
 -> 접두어가 된다는 뜻으로 return False

#### 코드_2

```python
def solution(pb):
    hash = {}
    for p in pb: # 해쉬키 작성
        hash[p]=1
    for p in pb:
        tmp = ''
        for element in p:
            tmp+=element
            if tmp in hash and tmp != p:
                return False
    return True
```
