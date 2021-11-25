---
title: “Programmers_Python_모든문제_순위확인"
date: 2021-07-27
categories: Algorithms
---

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/72412)

{% include adsense.html %}

### 프로그래머스_모든문제_순위확인
2021 KAKAO BLIND RECRUITMENT

### 문제설명

카카오는 하반기 경력 개발자 공개채용을 진행 중에 있으며 현재 지원서 접수와 코딩테스트가 종료되었습니다.<br>
이번 채용에서 지원자는 지원서 작성 시 아래와 같이 4가지 항목을 반드시 선택하도록 하였습니다.<br>
<br>
> - 코딩테스트 참여 개발언어 항목에 cpp, java, python 중 하나를 선택해야 합니다.<br>
> - 지원 직군 항목에 backend와 frontend 중 하나를 선택해야 합니다.<br>
> - 지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 합니다.<br>
> - 선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 합니다.<br>
<br>
인재영입팀에 근무하고 있는 니니즈는 코딩테스트 결과를 분석하여 채용에 참여한 개발팀들에 제공하기 위해 <br>
지원자들의 지원 조건을 선택하면 해당 조건에 맞는 지원자가 몇 명인 지 쉽게 알 수 있는 도구를 만들고 있습니다.<br>
<br>
예를 들어, 개발팀에서 궁금해하는 문의사항은 다음과 같은 형태가 될 수 있습니다.<br>

> - 코딩테스트에 java로 참여했으며, 
> - backend 직군을 선택했고, 
> - junior 경력이면서, 
> - 소울푸드로 pizza를 선택한 사람 중 
> - 코딩테스트 점수를 50점 이상 받은 지원자는 몇 명인가?


### 문제풀이

정확성과 효율성 모두를 잡아야 하는 문제<br>
정확성은 통과했으나, 효율성은 다른 사람 풀이를 참고하여 해겨

#### 효율성

#### 1. defaultdict
각 "개발언어, 지원직군, 지원 경력구분, 소울푸드" 별 **조합**으로<br>
리스트를 값으로 하는 딕셔너리 생성

- 개발언어: cpp, java, python, '-'
- 지원직군: backend, frontend, '-'
- 경력구분: junior, senior, '-'
- 소울푸드: pizza, chicken, '-'


#### 2. 해당 점수 이상의 사람을 탐색할 때, **이진탐색** 을 이용

- left, right, mid


### code

#### 정확성 만 통과
- 교집합 사용

```python
def solution(info, query):
    ans = []
    infolist = []

    for l in info:
        lis = l.split(' ')
        score = int(lis.pop())
        infolist.append([set(lis), score])

    for q in query:
        cnt = 0
        qlis = q.replace('and ', '').split(' ')
        qscore = int(qlis.pop())
        qset = set(qlis)
        for lis in infolist:
            res = qset & lis[0]
            if len(res) + qlis.count('-') == 4 and lis[-1] >= qscore:
                cnt += 1
        ans.append(cnt)

    return ans
```

#### 정확성/효율성 둘다 통과(다른사람풀이 참고)

```python
def solution(info, query):
    ans = []

    # 1. defaultdict;; list
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())

    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[-1]))
    for k in data:
        data[k].sort()

    for q in query:
        q = q.replace('and ', '').split()
        val = data[(q[0], q[1], q[2], q[3])]
        score = int(q[-1])
        
        # 2. binary search
        l, r = 0, len(val)
        while l<r:
            mid = (l+r)//2
            if val[mid] >= score:
                r = mid
            else:
                l = mid+1
        ans.append(len(val)-l)

    return ans
```
