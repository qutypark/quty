---
title: ToDo-statistics_2
date: 2020/12/28
categories: data_analysis
---

## OLS (Ordinary Least Squares)

### 들어가기 전(용어정리)
- 오차: **모집단**에서, 회귀식의 예측값과 실제 관측값과의 차이
- 잔차: **표본집단**에서, 회귀식의 예측값과 실제 관측값과의 차이

*주로 표본집단이 사용되므로 회귀식에서 사용되는 오차는 잔차를 의미하는 경우가 대부분.*

### 1. OLS란
선형회귀식에 주로 이용되는 파라메터 측정기법 중 하나로,
오차의 제곱의 합이 최소가 되는 원리를 이용

### 2. OLS의 전제조건 (회귀식의 전제조건과도 상응)

OLS추정이 일관되고, 편향성을 가지지 않기 위해서는 크게 3가지의 전제조건이 필요하다.

#### 2.1 독립변수가 외인성(exogenous)이어야 함.
[regressors are exogenous](https://en.wikipedia.org/wiki/Endogeneity_(econometrics))

독립변수는 회귀식 내에서 발생되는 것이 아닌, 외부적 요인에 의한 것이어야 함.<br>
이는 오차가 독립변수(설명변수)와의 상관성이 없음을 의미함.

#### 2.2 오차가 범위가 동질적 = 일정하고 유한해야 함.
[errors are homoscedastic](https://www.statisticssolutions.com/homoscedasticity/)

Homoscedastic=동질적: 모든 무작위 변수가 같은 유한범위를 지니고 있는 것<br>
즉, 설명변수의 변화와 상관없이 오차의 범위가 일정함<br>
이런 성질은 회귀식을 잘 정의시킴.

#### 2.3 오차가 자기상관이 없어야 함.
[errors are serially uncorrelated (=Autocorrelated)](https://en.wikipedia.org/wiki/Autocorrelation)

현 시점에서 발생한 오차와, 후 시점에서 발생한 오차가 서로 상관관계가 없어야 함
= 자기상관

### 3. OLS결과에서 사용되는 측정 정리.

#### 3.1 Omnibus/Prob(Omnibus)
- Omnibus: 잔차의 Skewness, Kurtosis의 종합<br>
           -> 값이 **0**에 가까울 수록 **정규성**을 나타냄
           
- Prob(Omnibus): 잔차가 정규분포를 가질 가능성<br>
           -> 값이 **1**에 가까울 수록 **정규성**을 나타냄
        
 
 *정규분포: 잔차가 정규분포되어있는 지 여부에 따라 선형휘귀식이 적합한지, 로지스틱 회귀식이 적합한지 판단 가능
 
 #### 3.2 Skewness(왜도)
 [왜도](https://ko.wikipedia.org/wiki/%EB%B9%84%EB%8C%80%EC%B9%AD%EB%8F%84)<br>
 데이터의 비대칭성을 나타냄<br>
 
 -> 값이 **0**에 가까울 수록 잔차가 **정규분포**되어있음을 나타냄<br>
= 평균값과 중앙값이 같음
 
 #### 3.3 Kurtosis(첨도)
 [첨도](https://ko.wikipedia.org/wiki/%EC%B2%A8%EB%8F%84)<br>
 확률분포의 뾰족함을 나타냄 = 관측치들이 집중적으로 몰려있는 정도<br>
 
 -> 값이 **3**에 가까우면 **정규분포**되어있음을 나타냄<br>
 = 아웃라이어의 영향을 피해 회귀식이 잘 정의되어있음을 나타냄
 
 #### 3.4 Durbin-Watson
 [Durbin-watson](https://en.wikipedia.org/wiki/Durbin%E2%80%93Watson_statistic)<br>
 잔차의 자기상관을 측정함<br>
 -> 값이 **2** =자기상관이 없음을 뜻함
 
 #### 3.5 Jarque-Bera = Omnibus와 비슷
 [Jarque-Bera](https://en.wikipedia.org/wiki/Jarque%E2%80%93Bera_test)
 
 
 #### 3.6 Condition Number
 [Condition Number](https://en.wikipedia.org/wiki/Condition_number)<br>
 입력값의 변화에, 출력값이 얼마나 영향을 받는지를 나타냄<br>
 = 내부 오류에 의해 외부 오류가 얼마나 영향을 받는지를 나타내며,<br>
   [다중공선성](https://ko.wikipedia.org/wiki/%EB%8B%A4%EC%A4%91%EA%B3%B5%EC%84%A0%EC%84%B1)의 진단으로도 쓰임
 -> 값이 **30** 아래여야 함.
 
 
  ### 4. 그 외
  
  #### 4.1 정규분포 & "선형회귀" 와 "로지스틱 회귀"
  - 선형회귀: 종속변수와 독립변수사이에 **선형관계**가 필요<br>
    -> 종속변수의 **가우스분포(정규분포)** 가정
    
  - 로지스틱 회귀: 데이터를 **곡선**에 맞춤<br>
    -> 종속변수의 **이항분포**를 가정
  
  > - 로짓변환: 곡선으로 맞춤 = Odds에 로그를 취하는 것<br>
  > - Odds: "비" =  실패에 비해 성공확률  log(P/1-P)<br>
  > - Odds Ratio : "비의 비율"  -> 비에 지수함수를 취한 것
 
 
 
 
 
