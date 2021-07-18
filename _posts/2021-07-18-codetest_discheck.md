---
title: “Programmers_Python_모든문제_거리두기확인하기"
date: 2021-07-18
categories: Algorithms
---

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/81302)


### 프로그래머스_모든문제_거리두기확인하기
카카오 2021 채용연계형 인턴십 문제

아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.

- 대기실은 5개이며, 각 대기실은 5x5 크기입니다.
- 거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
- 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.
- 응시자:P / 빈자리: O / 파티션: X
- 가로 세로 및 대각선도 고려
- 맨해튼 거리: 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2) ->  |r1 - r2| + |c1 - c2| 

#### 예시

아래처럼 자리 사이에 파티션이 존재한다면 맨해튼 거리가 2여도 거리두기를 지킨 것입니다.<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/8c056cac-ec8f-435c-a49a-8125df055c5e/PXP.png" width="15%" height="15%">
<br>

아래처럼 파티션을 사이에 두고 앉은 경우도 거리두기를 지킨 것입니다.<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/d611f66e-f9c4-4433-91ce-02887657fe7f/PX_XP.png" width="15%" height="15%">
<br>

아래처럼 맨해튼 거리 2이고 사이에 빈 테이블이 있는 경우는 거리두기를 지키지 않은 것입니다.<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/ed707158-0511-457b-9e1a-7dbf34a776a5/PX_OP.png" width="15%" height="15%">



### 풀이방법
인덱스 조정하며 완전 탐색으로 문제 풀이<br>
(대기실 수 및 대기실 크기 5X5 이므로 완전탐색 가능)

#### 코드

```python
def solution(place):
    ans = []
    for pl in place:
        cnt = 0
        pep, part, vac = [], [], []
        for i, p in enumerate(pl, start=1):
            lis = list(p)
            for j, e in enumerate(lis, start=1):
                if e == 'P':
                    pep.append([i, j])
                if e == 'X':
                    part.append([i, j])
                if e == 'O':
                    vac.append([i, j])
        if len(pep) >= 2:
            idx = 0
            while idx < len(pep):
                k = idx
                while k < len(pep):
                    k += 1
                    if k == len(pep):
                        break
                    dis = abs(pep[k][0]-pep[idx][0]) + abs(pep[k][1]-pep[idx][1])
                    if dis > 2:
                        if idx == len(pep)-2:
                            break
                    elif dis == 1:
                        idx = len(pep)
                        cnt += 1
                        break
                    elif dis == 2:
                        if pep[idx][0] == pep[k][0]:
                            mx = max(pep[idx][1], pep[k][1])
                            if [pep[idx][0], mx-1] in vac:
                                cnt += 1
                                idx = len(pep)
                                break
                            else:
                                if idx == len(pep) - 2:
                                    break
                        elif pep[idx][1] == pep[k][1]:
                            mx = max(pep[idx][0], pep[k][0])
                            if [mx-1, pep[idx][1]] in vac:
                                cnt += 1
                                idx = len(pep)
                                break
                            else:
                                if idx == len(pep)-2:
                                    break
                        elif pep[idx][0] != pep[k][0] and pep[idx][1] > pep[k][1]:
                            if [pep[idx][0], pep[idx][1]-1] in vac or [pep[idx][0]+1, pep[idx][1]] in vac:
                                cnt += 1
                                idx = len(pep)
                                break
                            else:
                                if idx == len(pep) - 2:
                                    break
                        elif pep[idx][0] != pep[k][0] and pep[idx][1] < pep[k][1]:
                            if [pep[idx][0], pep[idx][1]+1] in vac or [pep[idx][0]+1, pep[idx][1]] in vac:
                                cnt += 1
                                break
                            else:
                                if idx == len(pep) - 2:
                                    break
                idx += 1
                if idx >= len(pep)-1:
                    break
        if cnt == 0:
            ans.append(1)
        else:
            ans.append(0)
    return(ans)
```
