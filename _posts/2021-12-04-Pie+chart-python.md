---
title: Pie Chart 파이 그래프 구현

date: 2021-12-04
categories: Visualization
---

> 사용한 데이터셋: 타이타닉 데이터
>> 설명: 타이타닉 호 침몰 사건 당시의 승객 정보 및 사망 여부가 담긴 데이터<br>
>> 출처: [캐글 링크](https://www.kaggle.com/c/titanic)


# 목차
- python으로 구현
- Tableau로 구현

+)  [overall](https://tododata101.github.io/visualization/%EB%8D%B0%EC%9D%B4%ED%84%B0%EA%B0%80%EC%8B%9C%ED%99%94Overall/)


# ■ Pie Chart 파이 그래프 구현
- 전체에 대한 각 항목의 비율을 원 모양으로 나타낸 그래프다.<br>
- 전체에 대한 부분의 비율을 한 눈에 알 수 있기 때문에 비율을 나타낼 때 편리하다. 

{% include adsense.html %}

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

# Python으로 bar chart 구현 방법

### 1. matplotlib.pyplot as plt 사용
plt.pie()

## 카테고리 변수(=이산형) 별 생존 평균 집계
### 카테고리 변수 : 객실 등급 
객실 등급 별 생존(1,0) 평균

```python
sp = train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False)
plt.pie(sp['Survived'], labels = sp['Pclass'], startangle = 90, autopct='%1.1f%%')
plt.show() 
```

<img src = "https://raw.githubusercontent.com/tododata101/tododata101.github.io/master/_posts/beforepost/pie_survived_plcass.png" >


# ■ 2. Tableau로 구현

> 사용 툴: Tableau Public
>> *Tableau 사용방법에 대해서는 생략*

#### 2.1 데이터 종류 변경
'객실 등급'은 카테고리 변수이나 데이터 상으로는 연속형 변수(수치)<br>
따라서 카테고리 변수로 변경 필요
- 1)'객실 등급' 변수 마우스 오른쪽 클릭
- 2) 데이터 타입 변경 > 'String'

<img src="https://raw.githubusercontent.com/tododata101/tododata101.github.io/master/_posts/beforepost/convert_datatype.png"  width='50%' height='50%'>

#### 2.2 가시화

- 2) 새로운 '생존' 변수> measure >'average'
- 3) 'Marks' > 'Pie'유형 선택
- 4) 새로운 '생존' 변수 'Marks' > 'Angle' 로 drag & drop 
- 5) Ctrl 누른 상태로 'Marks' > 'Label' 로 drag & drop
- 5) 새로운 '객실 등급' 변수 'Marks' > 'Color' 로 drag & drop 
- 6) Ctrl 누른 상태로 'Marks' > 'Label' 로 drag & drop

<img src = "https://raw.githubusercontent.com/tododata101/tododata101.github.io/master/_posts/beforepost/Screen%20Shot%202021-12-04%20at%2022.30.29.png" >
