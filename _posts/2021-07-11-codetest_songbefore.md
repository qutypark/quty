---
title: “Programmers_Python_모든문제_방금그곡"
date: 2021-07-11
categories: Algorithms
---

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/17683)

{% include adsense.html %}

### 프로그래머스_모든문제_방금그곡

네오는 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교하려고 한다. <br>
네오가 찾으려는 음악의 제목을 구하여라.

예시 : m= "ABCDEFG"	, musicinfo = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

첫 번째 예시에서 HELLO는 길이가 7분이지만 12:00부터 12:14까지 재생되었으므로 <br>
실제로 CDEFGABCDEFGAB로 재생되었고, 이 중에 기억한 멜로디인 ABCDEFG가 들어있다. <br>


<details>
  <summary>문제설명</summary>
  
  방금그곡 서비스에서는 음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공한다.

  - 네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.<br>
  - 각 음은 1분에 1개씩 재생된다. <br>
      음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다. <br>
      음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다. <br>
  - 음악이 00:00를 넘겨서까지 재생되는 일은 없다.<br>
  - 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. <br>
  - 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.<br>
  - 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.<br>

</details>

### 풀이설명
1. musicinfo의 재생시간과, 반복 멜로디, 음악 제목을 추출
2. C#과 C는 다름 -> #계를 따로 처리
3. 기억 멜로디가 해당 반복 멜로디에 포함되는 곡 딕셔너리 생성
  키: 곡 / 값: 재생시간
4. 값(재생시간)기준 내림차순으로 딕셔너리 정렬
5. 딕셔너리 첫번째 키 출력
6. 딕셔너리가 없다면 '(None)' 출력

#### 코드

```python
import operator 

# #을 따로 처리
def sharp(x):
    lis = list(x)
    for i, e in enumerate(lis):
        if e =='#':
            lis[i-1] = lis[i-1].lower()
            lis[i] = ''
    ans = ''.join(lis)
    return ans

def solution(m, musicinfos):
    # musicinfo의 재생시간과, 반복 멜로디, 음악 제목을 추출
    all = []
    m = sharp(m)
    for i in musicinfos:
        tmp = i.split(',')
        tmp[-1] = sharp(tmp[-1])
        time, t = 0, 0
        time += 60 * (int(tmp[1].split(':')[0]) - int(tmp[0].split(':')[0]))
        time += int(tmp[1].split(':')[1]) - int(tmp[0].split(':')[1])
        le = (time // len(tmp[-1]))+1
        melody = ''
        while t < time:
            melody += (tmp[-1] * le)[t]
            t += 1
            if t == time:
                break
        all.append([tmp[2], time, melody])
    # 기억 멜로디가 해당 반복 멜로디에 포함되는 곡 딕셔너리 생성
    dic = {}
    for e in all:
        if m in e[-1]:
            dic[e[0]] = e[1]
    # 재생시간 기준 딕셔너리 내림차순 정렬
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    if sorted_dic:
        return sorted_dic[0][0]
    else:
        return '(None)'
```
