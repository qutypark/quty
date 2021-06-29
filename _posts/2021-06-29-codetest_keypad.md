---
title: “Programmers_Python_모든문제_키패드 누르기"
date: 2021-06-29
categories: Algorithms
---

> [문제링크](https://programmers.co.kr/learn/courses/30/lessons/67256)


### 프로그래머스_모든문제_키패드 누르기


<details>
  <summary>문제 설명</summary>
  
- 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당<br>
- 제한 사항<br>
>> - 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.<br>
>> - 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.<br>
>> - 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.<br>
>> - 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.<br>

- 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, <br>
  각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return.<br>

</details>


#### 풀이방법
-  계산식을 구해, 거리를 구하는 함수로 지정
-  해당 키보드, 왼손 위치, 오른쪽 위치를 저장


```python
def dis(curr, pre):
    global mm
    if pre not in mm:
        if abs(curr-pre)==1:
            return 1
        elif 2<=abs(curr-pre)<=4:
            return 2
        elif 5<=abs(curr-pre)<=7:
            return 3
        else:
            return 4
    else:
        a = abs(curr-pre)//3
        return a
def solution(number, hand):
    lf, rg, tmp = 10, 12, ''
    ans = []
    global mm
    mm = [2, 5, 8, 11]
    ll, rr = [1, 4, 7], [3, 6, 9]
    for e in number:
        if e in ll:
            tmp = 'L'
            lf = e
        elif e in rr:
            tmp = 'R'
            rg = e
        else:
            if e == 0:
                e = 11
            dis_l = dis(e, lf)
            dis_r = dis(e, rg)
            if dis_r < dis_l:
                tmp = 'R'
                rg = e
            elif dis_r > dis_l:
                tmp = 'L'
                lf = e
            else:
                tmp = hand[0].upper()
                if tmp =='R':
                    rg = e
                else:
                    lf = e
        ans.append(tmp)
    return ''.join(map(str,ans))
```
