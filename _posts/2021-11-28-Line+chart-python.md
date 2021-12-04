---
title: Line chart 선 그래프 구현

date: 2021-11-28
categories: Visualization
---

> 사용한 데이터셋: 경제활동인구조사데이터<br>
>> 설명: 2021년 10월 시점 고용 동향<br>
>> 출처: [통계청](http://kostat.go.kr/portal/korea/kor_nw/1/3/2/index.board)

# 목차
- python으로 구현
- Tableau로 구현

+)  [overall](https://tododata101.github.io/visualization/%EB%8D%B0%EC%9D%B4%ED%84%B0%EA%B0%80%EC%8B%9C%ED%99%94Overall/)


# ■ Line chart 선 그래프
시간에 따라 뭔가가 지속적으로 변화하는 것을 기록할 때 굉장히 유용하다.<br>
- 연속적 자료를 다루거나 통시적 자료를 다룰 경우
- 동일하거나 일련의 관찰대상의 추이를 비교할 경우
- 추세(trend)를 관찰할 경우

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
df = pd.read_csv(".../df.csv")
```
## * datetime으로의 변환
datetime이어야 할 컬럼이<br>
string데이터일 경우,
'pd.to_datetime'을 통해 변환 가능

```python
df['DateTime'] = df['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y.%m'))
df = df.drop(columns='date')
```

## Python으로 line chart 구현 방법

### 1. matplotlib.pyplot as plt 
- plt.plot()<br>

```python
# dataframe = df
# 시간 = datetime
# 값 = value

plt.plot(df['datetime'], df['value'])
plt.xlabel('datetime')
plt.ylabel('value')

plt.show()
```
- area plot<br>
ax = df.plot.area()


- 그래프 서식
```python
# 그래프 크기: 가로 10 세로 10
# 선 굵기: 1
# 그리드 : 표시
plt.rcParams["figure.figsize"] = (10,10)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['axes.grid'] = True 
```


### 2. seaborn as sns
sns.lineplot()
```python
# dataframe = df
# 시간 = datetime
# 값 = value

sns.lineplot(data=df, x="datetime", y="value")
```

## 기간 별 고용률 나타내기

### 1. matplotlib 
```python
plt.rcParams["figure.figsize"] = (14,4)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['axes.grid'] = True 

plt.plot(df['DateTime'], df['employement_rate'], marker='o', color='g')
plt.title('employment_rate')
plt.xlabel('DateTime')
plt.ylabel('employment_rate')
plt.show()
```
### +) area plot

```python
plt.rcParams["figure.figsize"] = (14,4)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['axes.grid'] = True 

ax = df.plot.area(x=df['DateTime'], y=df['employement_rate'], color='g')
plt.xlim(min(df['employment_rate')-1, max(df['employment_rate']))
plt.title('employment_rate')
plt.xlabel('DateTime')
plt.ylabel('employment_rate')
plt.show()
```

<img src="https://raw.githubusercontent.com/tododata101/tododata101.github.io/master/_posts/beforepost/area_chart.png">

### 2. seaborn as sns
```python
sns.lineplot(data=df, x="DateTime", y="employement_rate", marker='o', color='g')
```
<img src="https://raw.githubusercontent.com/tododata101/tododata101.github.io/master/_posts/beforepost/employement_rate.png">   

## 복수 컬럼 한 그래프에 나타내기

### 1. df.set_index()
- 시간 데이터를 인덱스로 설정<br>
- 자동으로 line plot으로 구성

```python
df.set_index('DateTime').plot(marker='o')
```

### 2. df['y'].plot(secondary_y=True)
- 시간 데이터를 인덱스로 설정<br>
- secondary_y = True

```python
df1.set_index('DateTime').employement_rate.plot(label='employment_rate', legend=True, color='g', marker='o')
df1.set_index('DateTime').unemployement_rate.plot(secondary_y=True, label='unemployment_rate', legend=True, color='b', marker='*')
```

<img src = "https://raw.githubusercontent.com/tododata101/tododata101.github.io/master/_posts/beforepost/muliple_ysis.png" >

### 2. seaborn
### 1)  pd.melt() [pd.melt](https://pandas.pydata.org/docs/reference/api/pandas.melt.html)
pd.melt()함수를 이용하여, <br>
dataframe을 재구조화할 필요

- 여러개의 컬럼을 variable 변수로 쌓고
- 컬럼 별 수치 값을 value 변수에 넣어줌
```python
dfm = df.melt('DateTime', var_name='cols', value_name='vals')
```

### 2)
- y = value 변수
- hue= variable 변수
```python
sns.lineplot(data=dfm_rate, x='DateTime', y='vals', hue='cols', marker='o')
```
<img src="https://raw.githubusercontent.com/tododata101/tododata101.github.io/master/_posts/beforepost/multiple_line.png">

# ■ 2. Tableau 으로 구현

## 월별 고용률과 실업률

- 1) date변수의 datatype 변형<br>
  : 마우스 오른쪽 > convert datatype > datetime
- 2) date변수를 'columns'로 drag & drop
- 3) 'columns' data변수 를 month로 변환.
- 4) 고용률 변수를 'rows'로 drag & drop
- 5) 실업률 변수를 오른쪽 Y축에 drag & drop
- 6) date 변수를 그래프 위 축으로 drag & drop
- 7) 6)의 변수를 'Year'로 변형
- 8) workbook 오른쪽 부분 마우스 오른쪽 클릭<br>
-   -> 필터 추가 -> 'Year'선택

<img src = "https://raw.githubusercontent.com/tododata101/tododata101.github.io/master/_posts/beforepost/tb_multiple_yaxis_filter.png" >



