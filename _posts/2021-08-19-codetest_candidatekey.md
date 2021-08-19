---
title: “Programmers_Python_모든문제_후보키"
date: 2021-08-19
categories: Algorithms
---

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/42890)


### 프로그래머스_모든문제_후보키
2019 KAKAO BLIND RECRUITMENT

### 문제 설명

관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 <br>
유일하게 식별할 수 있는 속성(Attribute) 또는 속성의 집합 중, <br>
다음 두 성질을 만족하는 것을 후보 키(Candidate Key)라고 한다.<br>

#### 유일성(uniqueness)
: 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.

#### 최소성(minimality)
: 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. <br>
즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.
<br>
아래와 같은 학생들의 인적사항이 주어졌을 때, 후보 키의 최대 개수를 구하라.


<img src="https://grepp-programmers.s3.amazonaws.com/files/production/f1a3a40ede/005eb91e-58e5-4109-9567-deb5e94462e3.jpg" width="50%" height="50%" />

### 문제 풀이

1. 속성 수의 크기를 가지는 속성 조합 리스트 생성
2. 유일성: 속성 조합 리스트의 값(튜플)중, 중복 제외
3. 최소성: 다른 집합을 포함하느 집합 제외

#### 코드
```python
from itertools import combinations

def solution(relation):
    col = len(relation[0])

    # 속성 전체 조합
    attlist = []
    for i in range(1, col+1):
        attlist.extend(combinations(range(col),i))

    # 중복검사(유일성)
    uni = []
    for att in attlist:
        tmp = [tuple([r[a] for a in att]) for r in relation]
        if len(set(tmp)) == len(tmp):
            uni.append(set(att))

    # 부분집합 여부 검사 (최소성)

    uniset = uni.copy()

    for i in range(len(uni)):
        for j in range(i+1, len(uni)):
            if uni[i].issubset(uni[j]) and uni[j] in uniset:
                uniset.remove(uni[j])

    return len(uniset)

```

