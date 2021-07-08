---
title: “Programmers_Python_모든문제_문자열 압축"
date: 2021-07-08
categories: Algorithms
---

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/60057)


### 프로그래머스_모든문제_문자열 압축

압축할 문자열 s가 매개변수로 주어질 때, <br>
1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return


<details>
  <summary>문제 설명</summary>

  문자열에서 같은 값이 연속해서 나타나는 것을 <br>
  그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.<br>
  <br>
- 간단한 예 
  > "aabbaccc"의 경우 <br>
   "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있음<br>
  
  > "ababcdcdababcdcd"의 경우 <br>
    문자를 1개 단위로 자르면 전혀 압축되지 않지만, <br>
    2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다. <br>
    다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법<br>
</details>


### 풀이방법

1. 해당 단위로 자름
2. 해당 단위가 반복된다면 압축
3. 해당 단위가 전체 글자 수의 반 이하일 때까지 반복
4. 가장 작은 글자 수를 출력

#### 코드

```python
def solution(word):
    cnt, ans = 1, len(word)
    # 해당 단위가 전체 글자 수의 반 이하일 때까지 반복
    while cnt <= len(word)//2:
        # 해당 단위로 자름
        phr = []
        i = 0
        while i <= len(word)-cnt:
            phr.append(word[i:i+cnt])
            i += cnt
            if len(word)-i < cnt:
                phr.append(word[i:])
        cur, loc = 0, 1
        while cur < len(phr):
            try:
                # 해당 단위가 반복된다면 압축
                while phr[cur] == phr[cur+loc]:
                    if phr[cur]=="":
                        break
                    loc += 1
                    if phr[cur] != phr[cur+loc]:
                        break
            except:
                pass
            if loc > 1:
                if cur < len(phr)-1:
                    phr[cur] = str(loc)+phr[cur]
                    for i in range(cur+1, cur+loc):
                        phr[i] = ""
                loc = 1
            cur += loc
            if cur >= len(phr)-1:
                break
        tmp = ''.join(phr)
        cnt += 1
        # 가장 작은 글자 수를 출력
        ans = min(ans, len(tmp))
    return ans
```
