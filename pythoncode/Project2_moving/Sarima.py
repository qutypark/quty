# 0. ---------------------import library---------------------
import numpy as np
import pandas as pd

from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

import matplotlib
import matplotlib.pyplot as plt
import japanize_matplotlib
# https://yolo.love/matplotlib/japanese/

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

# def duplication function 
def duplicate(testList, n):
    return testList*n

# 목적1: 선박 경로 예측 -> 예측 대상: 위도, 경도(Latitude, Longitude)
# 목적2: 선박 운전 효율지표 생성
# 목적3: 현 경로/예측 경로 가시화 및, 효율 지표 가시화 
#       데이터1: 선박위치데이터
#       데이터2: 선박기기데이터
#       예측1: 시계열 이동평균으로, 위도/경도 예측
#       예측2: 혹은 [distance, bearing]를 예측 후, 위도/경도를 계산 * 결과적으로 배제

#*주의* 데이터 셋 타임라인 1달 ->  시계열 예측의 어려움이 예상됨

# ----------------목적1.0 read data-------------------------------------------------------
#데이터1: 선박위치데이터
path_glob = os.path.join("localpath") 
xlsx_paths = sorted(glob.glob(path_glob))      
A = len(xlsx_paths)                 
lsDFA = [None]*A                    #save data as dataframe

for i,xpath in enumerate(xlsx_paths):
    xlsx=pd.read_csv(xpath,encoding="cp932")
    lsDFA[i]=xlsx

imo49=lsDFA[0].copy()

# ---------------목적1.1. data cleansing-------------------------------------
# latitude,longitude->정수화（from DMS to [Decimal Degree]）
def convert(tude):
    multiplier = 1 if tude[-1] in ['N', 'E'] else -1
    return multiplier * sum(float(x) / 60 ** n for n, x in enumerate(tude[:-1].split('-')))

lan49=[]
lon49=[]
for i in range(imo49.shape[0]):
    a=np.array(lsDFA[0].iloc[:,7])
    b=convert(a[i])
    lan49.append(b)
for i in range(imo49.shape[0]):
    a=np.array(lsDFA[0].iloc[:,8])
    b=convert(a[i])
    lon49.append(b)
imo49["Latitude"]=lan49
imo49["Longitude"]=lon49
imo49.drop(columns=['Latitude(緯度)', 'Longitude(経度)'],axis=1,inplace=True)

# ----------------목적1.2. Feature Engineering-------------------
# 예측2 distance 를 계산

from geopy.distance import geodesic
imo49distance=[0]
for i in range(1,imo49.shape[0]):
    a=(imo49.Latitude[i-1],imo49.Longitude[i-1])
    b=(imo49.Latitude[i],imo49.Longitude[i])
    c=geodesic(a,b).miles
    imo49distance.append(c)

# distance변수 추가
imo49["Distance"]=imo49distance

# 예측2 bearing 를 계산
import math
imo49bearing=[0]
for i in range(1,imo49.shape[0]):
    lat0=imo49.Latitude[i-1]
    lat1=imo49.Latitude[i]
    lon0=imo49.Longitude[i-1]
    lon1=imo49.Latitude[i]
    tc=math.atan2(math.sin(lon1-lon0)*math.cos(lat1),
                  math.cos(lat0)*math.sin(lat1)-math.sin(lat0)*math.cos(lat1)*math.cos(lon1-lon0))
    
    imo49bearing.append(tc)

# bearing변수 추가
imo49["bearing"]=imo49bearing

# --------------------------목적1.3.data 완성----------------------------
# ------it is not necessary to see skewdness----------------------------

imo49_1=imo49.copy()

#결손치 제거 /  필요한 변수만 남기기
imo49_1["Course"].fillna(imo49_1.Course.median(),inplace=True)
imo49_1["Heading"].fillna(imo49_1.Heading.median(),inplace=True)
imo49_1['Lasttime(UTC+09:00)']= pd.to_datetime(imo49_1['Lasttime(UTC+09:00)'])
imo49_1.drop(columns="UTC",axis=1,inplace=True)

# imo49_1float=imo49_1.iloc[:,[7,8,9,11,12,13]]
#시계열 이동평균 예측을 위해, 시간빈도 조정: 빈도=1day with median
imo49_3=imo49_1.groupby([pd.Grouper(key='Lasttime(UTC+09:00)', freq='1D')])[['Course', 'Heading', 'Speed（船速）', 'Latitude',
       'Longitude','Distance',"bearing"]].median()

# # --------------------------목적1.5  EDA--------------------------

# 먼저 위도경도 가시화 
# 시간빈도 조정 전: before manipulate datetime span with median
imo49_1.plot(x='Longitude', y='Latitude',style='o')  
plt.title('before manipulate time')  
plt.xlabel('Latitude')  
plt.ylabel('Longitude')  
plt.show()
# 시간빈도 조정 후:  after manipulate datetime span with median
imo49_3.plot(x='Longitude', y='Latitude',style='o')  
plt.title('after manipulate time')  
plt.xlabel('Longitude')  
plt.ylabel('Latitude')  
plt.show()

#time series가 additive vs multiplicative인지 확인
# 1) Latitude -> Seasonal이 일정한 형태 = additive
imo49_Lat=imo49_3['Latitude']
decomposition_a = sm.tsa.seasonal_decompose(imo49_Lat, model="additive")
decomposition_a.plot()

decomposition_m = sm.tsa.seasonal_decompose(imo49_Lat, model="multiplicative")
decomposition_m.title="multiplicative"
decomposition_m.plot()

# 2) Longitude -> Seasonal이 일정한 형태 = additive
imo49_Long=imo49_3['Longitude']
decomposition_a = sm.tsa.seasonal_decompose(imo49_Long, model="additive")
decomposition_a.plot()

decomposition_m = sm.tsa.seasonal_decompose(imo49_Long, model="multiplicative")
decomposition_m.title="multiplicative"
decomposition_m.plot()

# 3) distance -> Seasonal이 일정한 형태 = additive
imo49_dis=imo49_3['Distance']
decomposition_a = sm.tsa.seasonal_decompose(imo49_dis, model="additive")
decomposition_a.plot()

decomposition_m = sm.tsa.seasonal_decompose(imo49_dis, model="multiplicative")
decomposition_m.title="multiplicative"
decomposition_m.plot()

# 3) bearing -> multiplocative가 적용되지 않음 / Seasonal이 일정한 형태 = additive 
imo49_be=imo49_3['bearing']
decomposition_a = sm.tsa.seasonal_decompose(imo49_be, model="additive")
decomposition_a.plot()

decomposition_m = sm.tsa.seasonal_decompose(imo49_be, model="multiplicative")
decomposition_m.title="multiplicative"
decomposition_m.plot()

# # --------------------------목적1.6  위도경도예측 with 이동평균--------------------------
#전반적으로 [additive] 한 시계열 데이터
# ①시계열이동평균 = SARIMA(Seasonal Autoregressive Integrated Moving Average)
# 예측1: 시계열 이동평균으로, 위도/경도 예측
# 파라메터: Trend Parameter　pdq  0,1 (빈도 1day)/ Seasonal Parameter pdqm (s=12)
# 
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(imo49_3.iloc[:,6],
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

#latitude and longtitude
#파라메터 선택1: 정보손실지표 AIC가 낮은 파라메터 선택
#파라메터 선택2: P값과의 조정
imo49_Lat=imo49_3["Latitude"]
mod_Lat= sm.tsa.statespace.SARIMAX(imo49_Lat,
                                order=(0, 1, 1),
                                seasonal_order=(1, 1, 0, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results_Lat = mod_Lat.fit()
print(results_Lat.summary().tables[1])

imo49_Long=imo49_3["Longitude"]
mod_Long= sm.tsa.statespace.SARIMAX(imo49_Long,
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

imo49_L=imo49_3[["Latitude","Longitude"]]
pred_Long_Lat=pd.concat([pred_Lat,pred_Long],axis=1, sort=False)
pred_Long_Lat.columns=["pred_lat","pred_long"]

objs=[imo49_L,pred_Long_Lat]
#목적1의 완성된 데이터
df_resultL=pd.concat(objs)

# 가시화 for mapping make plot
BBox = ((imo49_1.Longitude.min(),   imo49_1.Longitude.max(),      
         imo49_1.Latitude.min(), imo49_1.Latitude.max()))
BBox_P=((df_resultL["pred_long"].min(),df_resultL["pred_long"].max(),      
        df_resultL["pred_lat"].min(),df_resultL["pred_lat"].max()))

# BBox_P2=((pred4.pred_lon.min(),pred4.pred_lon.max(),      
#        pred4.pred_lat.min(),pred4.pred_lat.max()))

BBox_N = ((BBox_P[0], BBox[1], BBox[2], BBox_P[3]))
# download backgroud map
ruh_m= plt.imread("map.png")
ruh_p= plt.imread("map_predict.png")

fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(imo49_3.Longitude, imo49_3.Latitude, zorder=1, alpha= 1, c='b', s=50)
ax.scatter(df_resultL.pred_long, df_resultL.pred_lat, zorder=1, alpha= 1, c='r', s=50)
ax.set_title('')
ax.set_xlim(BBox_N[0],BBox_N[1])
ax.set_ylim(BBox_N[2],BBox_N[3])
ax.imshow(ruh_p, zorder=0, extent = BBox_N, aspect= 'equal')


# -----------------------------목적2.0 read data---------------------------
#데이터2 선박기기데이터
path_globw= os.path.join("C:/user/local") # C140のxlsxファイル読み込み
csv_pathw= sorted(glob.glob(path_globw))      

W = len(csv_pathw)                 
lsDFW= [None]*W                    # save data to dataframe

for i,cpath in enumerate(csv_pathw):
    df = pd.read_csv(cpath,engine='python')  
    lsDFW[i] = df                 
    
# # --------------------------목적2.1 data cleansing---------------------------
#데이터1 과의 시간빈도 조정: 빈도=1day with median
c=lsDFW[1].columns
c=c.drop("Timestamp")
for i in range(W):
    lsDFW[i]['Timestamp']= pd.to_datetime(lsDFW[i]['Timestamp'])
for i in range(W):
    lsDFW[i]=lsDFW[i].groupby([pd.Grouper(key='Timestamp', freq='1D')])[c].median()
#지표생성에 필요한 변수만 남기기
cydf= lsDFW[1]                 
for i in range(2,W):
    cydf = cydf.append(lsDFW[i]) 
cydf.columns=c
cydf1=cydf[["v1","v2"]]
# # --------------------------목적2.2  Feature Engineering--------------------------
#데이터1(위치데이터(*현 경로)) & 데이터2(기기데이터 )concat
imo49_4=imo49_3.copy()
imo49_4=imo49_4.rename(index={"Lasttime(UTC+09:00)":"time"})
cydf1=cydf1.rename(index={"Timestamp":"time"})

AISCy=pd.concat([imo49_4,cydf1],axis=1)
#운전 지표 생성
AISCy['eff']=(AISCy["V0"] > AISCy["V2"]).astype("int")

AISCyeff1=AISCy[AISCy["eff"]==1]
AISCyeff0=AISCy[AISCy["eff"]==0]

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
#       효율이 좋음: AISCyeff1
#   효율이 좋지 않음: AISCyeff0

#---------------목적3.1.1 for static map----------------------- 
# download backgroud map
ruh_m= plt.imread("c:/users/localpath/map.png")
ruh_p= plt.imread("c:/users/localpath/map_predict.png")

# for mapping make plot
BBox = ((imo49_1.Longitude.min(),   imo49_1.Longitude.max(),      
         imo49_1.Latitude.min(), imo49_1.Latitude.max()))
BBox_P=((df_resultL["pred_long"].min(),df_resultL["pred_long"].max(),      
        df_resultL["pred_lat"].min(),df_resultL["pred_lat"].max()))


BBox_N = ((BBox_P[0], BBox[1], BBox[2], BBox_P[3]))


fig, ax = plt.subplots(figsize = (8,7))
ax.plot(imo49_3.Longitude, imo49_3.Latitude,'-o',c='b',label="present")
ax.plot(AISCyeff1["Longitude"], AISCyeff1["Latitude"],'o',c='g',label="efficiency")
ax.plot(df_resultL.pred_long, df_resultL.pred_lat,'-o',c="r",label="future")

ax.legend()
ax.set_title('efficeiency')
ax.set_xlim(BBox_P[0],BBox[1])
ax.set_ylim(BBox[2],BBox_P[3])
ax.imshow(ruh_p, zorder=0, extent = BBox_N,aspect= 'equal')

#---------------목적3.1.2 for dynamic plot with plotly----------------------- 
fig =go.Figure()
fig.add_trace(go.Scattermapbox(lat=list(b.Latitude),lon=list(b.Longitude),
                               mode="markers+lines", marker=go.scattermapbox.Marker(
            size=5
        ),subplot='mapbox',name="present",hovertemplate =b.index))
fig.add_trace(go.Scattermapbox(lat=list(a.pred_lat),lon=list(b.pred_long), 
                         mode="markers+lines", marker=go.scattermapbox.Marker(
            size=5
        ),subplot='mapbox',name="prediction",hovertemplate =b.index))
fig.add_trace(go.Scattermapbox(lat=list(AISCyeff1.Latitude),lon=list(AISCyeff1.Longitude),
                         mode="markers", marker=go.scattermapbox.Marker(
            size=5
        ),subplot='mapbox',name="eff",hovertemplate =AISCyeff1.index))


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


