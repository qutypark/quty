---
title: “Programmers_Python_sort_H-index"
date: 2021-06-15
categories: Algorithms
---
### 프로그래머스_Python_정렬_H-index

> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12198)



- 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, <br>
  이 과학자의 H-Index를 return
- H-index: 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값

```python
# lis = [3, 0, 6, 1, 5]
def solution(lis):
    ans = 0
    # 기준을 0부터 하나씩 늘려나감
    cnt = 0
    lis.sort()
    while cnt <= len(lis):
        tem = 0
        for e in lis:
            if e >= cnt:
                tem += 1
        if cnt <= tem:
            # h의 최댓값을 위해
            ans = max(ans, cnt)
            cnt += 1
        else:
            cnt += 1
    return ans
 ``` 
