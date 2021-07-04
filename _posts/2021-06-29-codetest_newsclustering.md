---
title: “Programmers_Python_모든문제_뉴스 클러스터링"
date: 2021-06-29
categories: Algorithms
---

[문제링크](https://programmers.co.kr/learn/courses/30/lessons/17677)


### 프로그래머스_모든문제_뉴스클러스터링


<details>
  <summary>문제설명</summary>

  자카드 유사도는 집합 간의 유사도를 검사하는 여러 방법 중의 하나로 알려져 있다.  <br>
  두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다. <br>
  
  예를 들어 집합 A = {1, 2, 3}, 집합 B = {2, 3, 4}라고 할 때,  <br>
  교집합 A ∩ B = {2, 3}, 합집합 A ∪ B = {1, 2, 3, 4}이 되므로,  <br>
  집합 A, B 사이의 자카드 유사도 J(A, B) = 2/4 = 0.5가 된다.  <br>
  집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다. <br>
  자카드 유사도는 원소의 중복을 허용하는 다중집합에 대해서 확장할 수 있다.  <br>
  다중집합 A는 원소 “1”을 3개 가지고 있고, 다중집합 B는 원소 “1”을 5개 가지고 있다고 하자.  <br>
  이 다중집합의 교집합 A ∩ B는 원소 “1”을 min(3, 5)인 3개, 합집합 A ∪ B는 원소 “1”을 max(3, 5)인 5개 가지게 된다. <br>
  
  
  
  다중집합 A = {1, 1, 2, 2, 3}, 다중집합 B = {1, 2, 2, 4, 5}라고 하면,  <br>
  교집합 A ∩ B = {1, 2, 2}, 합집합 A ∪ B = {1, 1, 2, 2, 3, 4, 5}가 되므로,  <br>
  자카드 유사도 J(A, B) = 3/7, 약 0.42가 된다. <br>
  
  이를 이용하여 문자열 사이의 유사도를 계산하는데 이용할 수 있다.  <br>
  문자열 “FRANCE”와 “FRENCH”가 주어졌을 때, 이를 두 글자씩 끊어서 다중집합을 만들 수 있다.  <br>
  
  
  각각 {FR, RA, AN, NC, CE}, {FR, RE, EN, NC, CH}가 되며,  <br>
  교집합은 {FR, NC}, 합집합은 {FR, RA, AN, NC, CE, RE, EN, CH}가 되므로,  <br>
  두 문자열 사이의 자카드 유사도 J("FRANCE", "FRENCH") = 2/8 = 0.25가 된다. <br>

  > 입력 형식 <br>
  > - 입력으로는 str1과 str2의 두 문자열이 들어온다. 각 문자열의 길이는 2 이상, 1,000 이하이다. <br>
  > - 입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. 이때 영문자로 된 글자 쌍만 유효하고,  <br>
      기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다. <br> 
      예를 들어 “ab+”가 입력으로 들어오면, “ab”만 다중집합의 원소로 삼고, “b+”는 버린다.<br> 
  > - 다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다. <br> 
  > “AB”와 “Ab”, “ab”는 같은 원소로 취급한다. <br>

  > 출력 형식 <br>
  > - 입력으로 들어온 두 문자열의 자카드 유사도를 출력한다.  <br>
  > 유사도 값은 0에서 1 사이의 실수이므로, 이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다. <br>
</details>


#### 풀이방식
> - regex로 알파벳
> - Counter로 교집합<br>
> **중복을 허용하는 다중집합**


```python
from collections import Counter
def solution(st1, st2):
    wd1, wd2 = [], []

    while st1:
        tm = "".join(re.findall("[a-zA-Z]+", st1[:2])).lower()
        if len(tm) == 2:
            wd1.append(tm)
        st1 = st1[1:]
        if len(st1) < 2:
            break
    while st2:
        tm = "".join(re.findall("[a-zA-Z]+", st2[:2])).lower()
        if len(tm) == 2:
            wd2.append(tm)
        st2 = st2[1:]
        if len(st2) < 2:
            break

    inter = len(list((Counter(wd1) & Counter(wd2)).elements()))
    all = len(wd1)+len(wd2)-inter

    if all == 0:
        return 65536
    else:
        return int((inter/all)*65536)
```


>> 다른 사람 풀이1
>> - [isalpha()](https://www.w3schools.com/python/ref_string_isalpha.asp)를 응용

```python
from collections import Counter
def solution(str1, str2):
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if not s1 and not s2:
        return 65536
    c1 = Counter(s1)
    c2 = Counter(s2)
    answer = int(float(sum((c1&c2).values()))/float(sum((c1|c2).values())) * 65536)
    return answer
```

>> 다른 사람 풀이2
>> - 교집합: 
>>> 1. set() & <br>
>>> 2. min count
>> - 합집합:
>>> 1. set() | <br>
>>> 2. max count 

```python
import re

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return int((gyo_sum/hap_sum)*65536)
```
