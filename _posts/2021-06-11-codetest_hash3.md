---
title: "Programmers_Python_Hash_베스트앨범"
date: 2021-06-11
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/parts/12077)

### 프로그래머스_해쉬_베스트앨범
- 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시
- 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return

- genre = ["classic", "pop", "classic", "classic", "pop"]
- plays = [500, 600, 150, 800, 2500]	

#### 풀이방식
- dataframe 과 defqultdict이용

```python
import pandas as pd
from collections import defaultdict
def solution(genres,plays):
    answer = []
    df = pd.DataFrame({'gen':genres,'pl':plays})
    d = defaultdict(list)
    for k, v in zip(genres,plays):
        d[k].append(v)
    dic = dict(d)
    
    # play의 sum을 생성 -> sum이 높은 순으로 정렬
    for i in dic.keys():
        ns=sum(dic.get(i))
        dic[i]=ns
    df['sum']=df['gen'].map(dic)
    
    df=df.sort_values(['sum','pl'],ascending=False)
    
    n = len(list(set(genres)))
    dfN=[None]*n
    
    # 인덱스 출력
    for i in range(n):
        un=df['gen'].unique()
        dfN[i]=df[df['gen']==un[i]].sort_values(['sum','pl'],ascending=False)
        answer.extend(dfN[i].iloc[:2,:].index)
        
    return answer
```
