---
title: Bar chart 막대 그래프 구현

date: 2021-11-27
categories: Visualization
---

> 사용한 데이터셋: 타이타닉 데이터
>> 설명: 타이타닉 호 침몰 사건 당시의 승객 정보 및 사망 여부가 담긴 데이터<br>
>> 출처: [캐글 링크](https://www.kaggle.com/c/titanic)

# 목차
- python으로 구현
- Tableau로 구현

+)  [overall](https://tododata101.github.io/visualization/%EB%8D%B0%EC%9D%B4%ED%84%B0%EA%B0%80%EC%8B%9C%ED%99%94Overall/)


# ■ 1. python으로 구현

## 준비

```python
# 필요 라이브러리 설치
import pandas as pd
import numpy as np

# 시각화를 위한 라이브러리
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# 데이터 불러오기
train = pd.read_csv(".../train.csv")
```
## Python으로 bar chart 구현 방법

#### 1. pandas plot() 함수 사용
- kind = 'bar' <br>
- 혹은 df.plot.bar() <br>
을 통해 bar chart 구현 가능
``` python
# dataframe: df
# 카테고리 변수: var
# 값 : value
# 1)
df.plot('var', kind='bar')
# 2)
df.plot.bar(x='var', y='value')
```

#### 2. matplotlib.pyplot사용
plt.bar(

```python
x = np.arange(3)
years = ['2018', '2019', '2020']
values = [100, 400, 900]

plt.bar(x, values)
plt.xticks(x, years)

plt.show()
```

## 카테고리 변수(=이산형) 별 생존 평균 집계
#### 1. 카테고리 변수 : 성별

```python
ss = train[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False)
ss.plot("Sex",kind="bar").set_xlabel("Sex")

# or
ss.plot.bar(x='Sex', y='Survived')
```


