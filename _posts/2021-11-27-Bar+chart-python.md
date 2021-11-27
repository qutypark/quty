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


# ■ Bar chart
범주데이터(카테고리 데이터)의 요약 그래프로,<br>
각 막대는 각 범주를, 각 막대 높이는 각 범주의 특정 집계를 의미한다.
<br>
크고 작음을 한 눈에 이해하기에 가장 편리하다.<br>
가독성 면에선 항목이 적을수록 가로가 좋고 항목이 많을수록 세로가 좋다.<br>

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
plt.bar()

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
<img src="https://raw.githubusercontent.com/tododata101/tododata101.github.io/master/_posts/beforepost/barplot_survive.png"  width='50%' height='50%'>

#### 2. 카테고리 변수: 객실 등급(Pclass)
성별을 색깔로 구별해줌<br>
- 먼저 카테고리 변수(성별, 객실등급) 별 생존 평균 데이터프레임 생성
- 객실 등급을 인덱스로 피벗 테이블 생성
- Stacked 막대 차트 생성

```python
#먼저 카테고리 변수(성별, 객실등급) 별 생존 평균 데이터프레임 생성
sp = train[['Sex', 'Pclass', 'Survived']].groupby(['Sex', 'Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False)
# 인덱스 생성
sp.set_index(['Sex', 'Pclass', 'Survived'], append=True)

#객실 등급을 인덱스로 피벗 테이블 생성
sp2 = sp.pivot(index='Pclass', columns='Sex', values='Survived')

#Stacked 막대 차트 생성
sp2.plot.bar(stacked=True)
```

<img src="https://raw.githubusercontent.com/tododata101/tododata101.github.io/master/_posts/beforepost/stacked.%3D.png"  width='50%' height='50%'>


# ■ 2. Tableau로 구현



