# 0. ---------------------import library---------------------
import numpy as np
import pandas as pd

from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

import matplotlib
import matplotlib.pyplot as plt
import japanize_matplotlib
# to display hiragana,katakata,kanji 

%matplotlib inline 
import seaborn as sns
plt.style.use("ggplot")

import os
import openpyxl

import collections, csv
from os.path  import basename

import glob                        

import itertools
from itertools import chain, repeat
from itertools import cycle, islice

# 목적1: 선박 경로 예측 -> 예측 대상: 위도, 경도(Latitude, Longitude)
# 목적2: 선박 운전 효율지표 생성
# 목적3: 현 경로/예측 경로 가시화 및, 효율 지표 가시화 
#       데이터1: 선박위치데이터 =df1
#       데이터2: 선박기기데이터 =df2
#       데이터3: 데이터1 + 데이터2 = df3
#       예측1: 시계열 이동평균으로, 위도/경도 예측
#       예측2: 혹은 [distance, bearing]를 예측 후, 위도/경도를 계산 * 결과적으로 배제

#*주의* 데이터 셋 타임라인 1달 ->  시계열 예측의 어려움이 예상됨

# ----------------목적1.0 read data-------------------------------------------------------
#데이터1: 선박위치데이터

df1=pd.read_csv("localpath",encoding="cp932")

# ---------------목적1.1. data cleansing-------------------------------------
# latitude,longitude->정수화（from DMS to [Decimal Degree]）
def convert(tude):
    multiplier = 1 if tude[-1] in ['N', 'E'] else -1
    return multiplier * sum(float(x) / 60 ** n for n, x in enumerate(tude[:-1].split('-')))

lan=[]
lon=[]
for i in range(df1.shape[0]):
    a=np.array(lsDFA[0].iloc[:,7])
    b=convert(a[i])
    lan.append(b)
for i in range(df1.shape[0]):
    a=np.array(lsDFA[0].iloc[:,8])
    b=convert(a[i])
    lon.append(b)
df1["Latitude"]=lan
df1["Longitude"]=lon
df1.drop(columns=['Latitude(緯度)', 'Longitude(経度)'],axis=1,inplace=True)

# ----------------목적1.2. Feature Engineering-------------------
# 예측2 distance 를 계산

from geopy.distance import geodesic
df1distance=[0]
for i in range(1,df1.shape[0]):
    a=(df1.Latitude[i-1],df1.Longitude[i-1])
    b=(df1.Latitude[i],df1.Longitude[i])
    c=geodesic(a,b).miles
    df1distance.append(c)

# distance변수 추가
df1["Distance"]=df1distance

# 예측2 bearing 를 계산
import math
df1bearing=[0]
for i in range(1,df1.shape[0]):
    lat0=df1.Latitude[i-1]
    lat1=df1.Latitude[i]
    lon0=df1.Longitude[i-1]
    lon1=df1.Latitude[i]
    tc=math.atan2(math.sin(lon1-lon0)*math.cos(lat1),
                  math.cos(lat0)*math.sin(lat1)-math.sin(lat0)*math.cos(lat1)*math.cos(lon1-lon0))
    
    df1bearing.append(tc)

# bearing변수 추가
df1["bearing"]=df1bearing

# --------------------------목적1.3.data 완성----------------------------
# ------it is not necessary to see skewdness----------------------------

df1_1=df1.copy()

#중앙값으로 결손치 제거  /  필요한 변수만 남기기
df1_1["Course"].fillna(df1_1.Course.median(),inplace=True)
df1_1["Heading"].fillna(df1_1.Heading.median(),inplace=True)
df1_1['Lasttime(UTC+09:00)']= pd.to_datetime(df1_1['Lasttime(UTC+09:00)'])
df1_1.drop(columns="UTC",axis=1,inplace=True)

#시계열 이동평균 예측을 위해, 시간빈도 조정: 빈도=1day with median
#완성된 데이터1 = df1_3
df1_3=df1_1.groupby([pd.Grouper(key='Lasttime(UTC+09:00)', freq='1D')])[['Course', 'Heading', 'Speed（船速）', 'Latitude',
       'Longitude','Distance',"bearing"]].median()



# # --------------------------목적1.5  EDA--------------------------

# 먼저 위도경도 가시화 
# 시간빈도 조정 전: before manipulate datetime span with median
df1_1.plot(x='Longitude', y='Latitude',style='o')  
plt.title('before manipulate time')  
plt.xlabel('Latitude')  
plt.ylabel('Longitude')  
plt.show()
# 시간빈도 조정 후:  after manipulate datetime span with median
df1_3.plot(x='Longitude', y='Latitude',style='o')  
plt.title('after manipulate time')  
plt.xlabel('Longitude')  
plt.ylabel('Latitude')  
plt.show()

#time series가 additive vs multiplicative인지 확인
# 1) Latitude -> Seasonal이 일정한 형태 = additive
df1_Lat=df1_3['Latitude']
decomposition_a = sm.tsa.seasonal_decompose(df1_Lat, model="additive")
decomposition_a.plot()

decomposition_m = sm.tsa.seasonal_decompose(df1_Lat, model="multiplicative")
decomposition_m.title="multiplicative"
decomposition_m.plot()

# 2) Longitude -> Seasonal이 일정한 형태 = additive
df1_Long=df1_3['Longitude']
decomposition_a = sm.tsa.seasonal_decompose(df1_Long, model="additive")
decomposition_a.plot()

decomposition_m = sm.tsa.seasonal_decompose(df1_Long, model="multiplicative")
decomposition_m.title="multiplicative"
decomposition_m.plot()

# 3) distance -> Seasonal이 일정한 형태 = additive
df1_dis=df1_3['Distance']
decomposition_a = sm.tsa.seasonal_decompose(df1_dis, model="additive")
decomposition_a.plot()

decomposition_m = sm.tsa.seasonal_decompose(df1_dis, model="multiplicative")
decomposition_m.title="multiplicative"
decomposition_m.plot()

# 3) bearing -> multiplocative가 적용되지 않음 / Seasonal이 일정한 형태 = additive 
df1_be=df1_3['bearing']
decomposition_a = sm.tsa.seasonal_decompose(df1_be, model="additive")
decomposition_a.plot()

decomposition_m = sm.tsa.seasonal_decompose(df1_be, model="multiplicative")
decomposition_m.title="multiplicative"
decomposition_m.plot()

# # --------------------------목적1.6  위도경도예측 with 이동평균--------------------------
#전반적으로 [additive] 한 시계열 데이터
# ①시계열이동평균 = SARIMA(Seasonal Autoregressive Integrated Moving Average)
# 예측1: 시계열 이동평균으로, 위도/경도 예측
# 파라메터: Trend Parameter　pdq  0,1 (빈도 1day)/ Seasonal Parameter pdqm (s=12)

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(df1_3.iloc[:,6],
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

#latitude and longtitude
#파라메터 선택1: 위의 결과에서 정보손실지표 AIC가 낮은 파라메터 선택
#파라메터 선택2: P값과의 조정

#latitude 예측 파라메터
df1_Lat=df1_3["Latitude"]
mod_Lat= sm.tsa.statespace.SARIMAX(df1_Lat,
                                order=(0, 1, 1),
                                seasonal_order=(1, 1, 0, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results_Lat = mod_Lat.fit()
print(results_Lat.summary().tables[1])

#longitude 예측 파라메터
df1_Long=df1_3["Longitude"]
mod_Long= sm.tsa.statespace.SARIMAX(df1_Long,
                                order=(0, 1, 0),
                                seasonal_order=(1, 1, 0, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results_Long = mod_Long.fit()
print(results_Long.summary().tables[1])

# # # predict in 10days of lat&longtitude 10일 후 예측
pred_uc_Lat = results_Lat.forecast(10)
pred_ci_Lat= pred_uc_Lat.conf_int()
pred_Lat=pred_uc_Lat.predicted_mean

pred_uc_Long = results_Long.forecast(steps=10)
pred_ci_Long= pred_uc_Long.conf_int()
pred_Long=pred_uc_Long.predicted_mean

df1_L=df1_3[["Latitude","Longitude"]]
pred_Long_Lat=pd.concat([pred_Lat,pred_Long],axis=1, sort=False)
pred_Long_Lat.columns=["pred_lat","pred_long"]

objs=[df1_L,pred_Long_Lat]

#목적1의 완성된 데이터
df_resultL=pd.concat(objs)

# 가시화 for mapping make plot
BBox = ((df1_1.Longitude.min(),   df1_1.Longitude.max(),      
         df1_1.Latitude.min(), df1_1.Latitude.max()))
BBox_P=((df_resultL["pred_long"].min(),df_resultL["pred_long"].max(),      
        df_resultL["pred_lat"].min(),df_resultL["pred_lat"].max()))

BBox_N = ((BBox_P[0], BBox[1], BBox[2], BBox_P[3]))

# download backgroud map
ruh_m= plt.imread("map.png")
ruh_p= plt.imread("map_predict.png")

fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(df1_3.Longitude, df1_3.Latitude, zorder=1, alpha= 1, c='b', s=50)
ax.scatter(df_resultL.pred_long, df_resultL.pred_lat, zorder=1, alpha= 1, c='r', s=50)
ax.set_xlim(BBox_N[0],BBox_N[1])
ax.set_ylim(BBox_N[2],BBox_N[3])
ax.imshow(ruh_p, zorder=0, extent = BBox_N, aspect= 'equal')


# -----------------------------목적2.0 read data---------------------------
#데이터2 선박기기데이터
df2= pd.read_csv("localpath",engine='python')  

# # --------------------------목적2.1 data cleansing---------------------------
#데이터1 과의 시간빈도 조정: 빈도=1day with median
c=df2.columns
df2=df2.groupby([pd.Grouper(key='Timestamp', freq='1D')])[c]].median()
#지표생성에 필요한 변수만 남기기
df2_1=df2[["v1","v2"]]

# # --------------------------목적2.2  Feature Engineering--------------------------
#데이터1(위치데이터(*현 경로)) & 데이터2(기기데이터 )concat
#for concat ->  manipulate index
df1_4=df1_3.copy()
df1_4=df1_4.rename(index={"Lasttime(UTC+09:00)":"time"})
df2_1=df2_1.rename(index={"Timestamp":"time"})

df3=pd.concat([df1_4,df2_1],axis=1)
#운전 지표 생성
df3['eff']=(df3["V0"] > df3["V2"]).astype("int")

df3eff1=df3[df3["eff"]==1]
df3eff0=df3[df3["eff"]==0]

# ------------------목적3: 현 경로/예측 경로 가시화 및, 효율 지표 가시화 -------------------
# -------------------목적3.0 import library----------------------------------------

import chart_studio.plotly as py
from plotly.graph_objs import *
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
import plotly.tools as tlsM
from IPython.display import HTML,IFrame

# -------------------목적3.1 필요한 데이터 준비----------------------------------------
# 데이터 1:현 경로/예측 경로 = df_resultL
# 데이터 2:효율지표 
#       효율이 좋음: df3eff1
#   효율이 좋지 않음: df3eff0

#---------------목적3.1.1 for static map----------------------- 
# download backgroud map
ruh_m= plt.imread("c:/users/localpath/map.png")
ruh_p= plt.imread("c:/users/localpath/map_predict.png")

# for mapping make plot
BBox = ((df1_1.Longitude.min(),   df1_1.Longitude.max(),      
         df1_1.Latitude.min(), df1_1.Latitude.max()))
BBox_P=((df_resultL["pred_long"].min(),df_resultL["pred_long"].max(),      
        df_resultL["pred_lat"].min(),df_resultL["pred_lat"].max()))


BBox_N = ((BBox_P[0], BBox[1], BBox[2], BBox_P[3]))


fig, ax = plt.subplots(figsize = (8,7))
ax.plot(df1_3.Longitude, df1_3.Latitude,'-o',c='b',label="present")
ax.plot(df3eff1["Longitude"], df3eff1["Latitude"],'o',c='g',label="efficiency")
ax.plot(df_resultL.pred_long, df_resultL.pred_lat,'-o',c="r",label="future")

ax.legend()
ax.set_title('efficeiency')
ax.set_xlim(BBox_P[0],BBox[1])
ax.set_ylim(BBox[2],BBox_P[3])
ax.imshow(ruh_p, zorder=0, extent = BBox_N,aspect= 'equal')

#---------------목적3.1.2 for dynamic plot with plotly----------------------- 
fig =go.Figure()
fig.add_trace(go.Scattermapbox(lat=list(df3.Latitude),lon=list(df3.Longitude),
                               mode="markers+lines", marker=go.scattermapbox.Marker(
            size=5
        ),subplot='mapbox',name="present",hovertemplate =df3.index))
fig.add_trace(go.Scattermapbox(lat=list(df3.pred_lat),lon=list(df3.pred_long), 
                         mode="markers+lines", marker=go.scattermapbox.Marker(
            size=5
        ),subplot='mapbox',name="prediction",hovertemplate =df3.index))
fig.add_trace(go.Scattermapbox(lat=list(df3eff1.Latitude),lon=list(df3eff1.Longitude),
                         mode="markers", marker=go.scattermapbox.Marker(
            size=5
        ),subplot='mapbox',name="eff",hovertemplate =df3eff1.index))


fig.update_layout(
    autosize=True,
    hovermode='x',
    mapbox=dict(
        style='open-street-map',
        domain={'x': [0, 1], 'y': [0, 1]},
        bearing=0,
        center=dict(
            lat=20,
            lon=61
        ),
        pitch=0,
        zoom=2
        
    )
)
fig.show()


