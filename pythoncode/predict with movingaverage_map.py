#―――――――――――――――A. predict path of ship with move average――――――――――――――――――――――――――――
#―――――――――――――――B. make label efficieny with water speed and rotaion―――――――――――――――――――――――
#―――――――――――――――R. visulization of A B――――――――――――――――――――――――――――――――――――――



# ------0. import libraries-----------
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

# ------A1. read data from local; location data of ship-----------
path_glob = os.path.join('c:/users/localpath/') 
xlsx_paths = sorted(glob.glob(path_glob))     

A = len(xlsx_paths)                 
lsDFA = [None]*A                    # make empty dataframe

for i,xpath in enumerate(xlsx_paths):
    xlsx=pd.read_csv(xpath,encoding="cp932")
    lsDFA[i]=xlsx

# def function: duplication
def duplicate(testList, n):
    return testList*n
# view　option
pd.set_option('display.max_colwidth', 100) # 一列に表示できる文字数を増やす
pd.set_option('display.max_columns', None) # 常に全ての列（カラム）を表示するpandasオプション

# def fuction: convert string to numeric for lotitude, langtitude 
def convert(tude):
    multiplier = 1 if tude[-1] in ['N', 'E'] else -1
    return multiplier * sum(float(x) / 60 ** n for n, x in enumerate(tude[:-1].split('-')))

# for example using one file from all files 
imo49=lsDFA[0].copy()

# -----A2. Data Cleansing-----


# -----A2.1 convert longtitude and latitude-----

lat49=[]
lon49=[]
for i in range(imo49.shape[0]):
    a=np.array(lsDFA[0].iloc[:,7])
    b=convert(a[i])
    lan49.append(b)
for i in range(imo49.shape[0]):
    a=np.array(lsDFA[0].iloc[:,8])
    b=convert(a[i])
    lon49.append(b)
imo49["Latitude"]=lat49
imo49["Longitude"]=lon49

imo49.drop(columns=['Latitude(緯度)', 'Longitude(経度)'],axis=1,inplace=True)

# -----A2.2 feature engineering 1.new feauture= move distance-----　
from geopy.distance import geodesic

imo49distance=[0]
for i in range(1,imo49.shape[0]):
    a=(imo49.Latitude[i-1],imo49.Longitude[i-1])
    b=(imo49.Latitude[i],imo49.Longitude[i])
    c=geodesic(a,b).miles
    imo49distance.append(c)
imo49["Distance"]=imo49distance

# -----A2.2 feature engineering 2.new feauture= bearing-----　

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
imo49["bearing"]=imo49bearing

# -----A2.3 replace nan data and make datetime span consistent with median -----

imo49_1=imo49.copy()

imo49_1["Course"].fillna(imo49_1.Course.median(),inplace=True)
imo49_1["Heading"].fillna(imo49_1.Heading.median(),inplace=True)
imo49_1['Lasttime(UTC+09:00)']= pd.to_datetime(imo49_1['Lasttime(UTC+09:00)'])
imo49_1.drop(columns="UTC",axis=1,inplace=True)

imo49_1float=imo49_1.iloc[:,[7,8,9,11,12,13]]
imo49_3=imo49_1.groupby([pd.Grouper(key='Lasttime(UTC+09:00)', freq='1D')])[['Course', 'Heading', 'Speed（船速）', 'Latitude',
       'Longitude','Distance',"bearing"]].median()


# -----B1.read data from local: waterspeed and rotaion of ship-----

path_globw= os.path.join('c:/user/localpath*.csv') 
csv_pathw= sorted(glob.glob(path_globw))      

W = len(csv_pathw)                  # 
lsDFW= [None]*W                    # make empty dataframe for save data

for i,cpath in enumerate(csv_pathw):
    df = pd.read_csv(cpath,engine='python')         
    lsDFW[i] = df 

# -----B2.data cleansing-----

c=lsDFW[1].columns
c=c.drop("�ｻｿTimestamp")
for i in range(W):
    lsDFW[i]['�ｻｿTimestamp']= pd.to_datetime(lsDFW[i]['�ｻｿTimestamp'])
for i in range(W):
    lsDFW[i]=lsDFW[i].groupby([pd.Grouper(key='�ｻｿTimestamp', freq='1D')])[c].median()    

# -----B2.data cleansing-----

cydf= lsDFW[1]                 
for i in range(2,W):
    cydf = cydf.append(lsDFW[i]) 
cydf.columns=c
cydf1=cydf[["<CH1>  Longitudinal water speed","<TAFB>  ACTUAL ACTUATOR POSITION"]]


# -----A,B2.data cleansing ; concat 2dataframe -----

imo49_4=imo49_3.copy()
imo49_4=imo49_4.rename(index={"Lasttime(UTC+09:00)":"time"})
cydf1=cydf1.rename(index={"�ｻｿTimestamp":"time"})
AISCy=pd.concat([imo49_4,cydf1],axis=1) 
AISCy['eff']=(AISCy["Speed"] > AISCy['<CH1>  Longitudinal water speed']).astype("int")

#label efficiency
AISCyeff1=AISCy[AISCy["eff"]==1]
AISCyeff0=AISCy[AISCy["eff"]==0] 


# -----A3.moveing average -----

# first, make plot of move path
# before manipulate datetime span with median
imo49_1.plot(x='Longitude', y='Latitude',style='o')  
plt.title('Latitude & Longitude')  
plt.xlabel('Latitude')  
plt.ylabel('Longitude')  
plt.show()
# after manipulate datetime span with median
imo49_3.plot(x='Longitude', y='Latitude',style='o')  
plt.title('Latitude & Longitude')  
plt.xlabel('Longitude')  
plt.ylabel('Latitude')  
plt.show()
# example
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

# use ARIMA to calculate move average of path with timedata
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

#choose parameter to calculate moving average of latitude / longtitude data  

#-----way A3.1. calculate latitude and logngitude by of its own moveing average -----
#-----in result:  way A3.1 will gonna be chosen,, but let's see!

#latitude and longtitude
mod_Lat= sm.tsa.statespace.SARIMAX(imo49_Lat,
                                order=(0, 1, 1),
                                seasonal_order=(1, 1, 0, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results_Lat = mod_Lat.fit()
# print(results_Lat.summary().tables[1])

mod_Long= sm.tsa.statespace.SARIMAX(imo49_Long,
                                order=(0, 1, 0),
                                seasonal_order=(1, 1, 0, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results_Long = mod_Long.fit()
# print(results_Long.summary().tables[1])

# predict in 10days of lat&longtitude
pred_uc_Lat = results_Lat.get_forecast(steps=10)
pred_ci_Lat= pred_uc_Lat.conf_int()
pred_Lat=pred_uc_Lat.predicted_mean

pred_uc_Long = results_Long.get_forecast(steps=10)
pred_ci_Long= pred_uc_Long.conf_int()
pred_Long=pred_uc_Long.predicted_mean
             
# make dataframe of present data and predict data of latitude and longtitude
pred_Long_Lat=pd.concat([pred_Lat,pred_Long],axis=1, sort=False)
pred_Long_Lat.columns=["pred_lat","pred_long"]

objs=[imo49_L,pred_Long_Lat]
df_resultL=pd.concat(objs)

#-----way A3.2. calculate latitude and logngitude prediction from heading, course, bearing, speed, distance -----
#-----in result:  way A3.1 will gonna be chosen,, but let's see!


#except for latitude and longtitude -> will be used for longtitude and latitude
mod_heading= sm.tsa.statespace.SARIMAX(imo49_3.iloc[:,1],
                                order=(1, 1, 0),
                                seasonal_order=(1, 1, 0, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results_heading = mod_heading.fit()
# print(results_heading.summary().tables[1])

mod_course= sm.tsa.statespace.SARIMAX(imo49_3.iloc[:,0],
                                order=(1, 0, 1),
                                seasonal_order=(1, 1, 0, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results_course = mod_course.fit()
# print(results_course.summary().tables[1])

mod_speed= sm.tsa.statespace.SARIMAX(imo49_3.iloc[:,2],
                                order=(0, 0, 0),
                                seasonal_order=(1, 1, 0, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results_speed = mod_speed.fit()
# print(results_speed.summary().tables[1])

mod_dis= sm.tsa.statespace.SARIMAX(imo49_3.iloc[:,5],
                                order=(0, 0, 1),
                                seasonal_order=(1, 1, 0, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results_dis = mod_dis.fit()
# print(results_dis.summary().tables[1])

mod_bearing= sm.tsa.statespace.SARIMAX(imo49_3.iloc[:,6],
                                order=(1, 1, 0),
                                seasonal_order=(0, 1, 0, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results_bearing = mod_bearing.fit()
# print(results_bearing.summary().tables[1])

#predict heading, course, speed,distant, bearing
pred_uc_heading = results_heading.get_forecast(steps=10)
pred_ci_heading= pred_uc_heading.conf_int()
pred_heading=pred_uc_heading.predicted_mean

pred_uc_course = results_course.get_forecast(steps=10)
pred_ci_course= pred_uc_course.conf_int()
pred_course=pred_uc_course.predicted_mean

pred_uc_speed = results_speed.get_forecast(steps=10)
pred_ci_speed= pred_uc_speed.conf_int()
pred_speed=pred_uc_speed.predicted_mean

pred_uc_dis = results_dis.get_forecast(steps=10)
pred_ci_dis= pred_uc_dis.conf_int()
pred_dis=pred_uc_dis.predicted_mean

pred_uc_bearing = results_bearing.get_forecast(steps=10)
pred_ci_bearing= pred_uc_bearing.conf_int()
pred_bearing=pred_uc_bearing.predicted_mean

pred4=pd.concat([pred_course,pred_heading,pred_speed,pred_dis,pred_bearing],axis=1, sort=False)
pred4.columns=["pred_course","pred_heading","pred_speed","pred_dis","pred_bearing"]

#---calculate latitude&longtitude prediction with prediction of speed,distance,heading, bearing
import math

d=imo49_3.Distance[30]
lat1=math.radians(imo49_3.Latitude[30])
lon1=math.radians(imo49_3.Longitude[30])
tc=imo49_3.bearing[30]
pi=math.pi

lat2=math.asin(math.sin(lat1)*math.cos(d/3958)+math.cos(lat1)*math.sin(d/3958)*math.cos(tc))
lon2=lon1+math.atan2((math.sin(tc)*math.sin(d/3958)*math.cos(lat1)),
                     (math.cos(d/3958)-math.sin(lat1)*math.sin(lat2)))

lat3= math.degrees(lat2)
lon3= math.degrees(lon2)

lat=[lat3]
lon=[lon3]
for i in range(9):
    d=pred4.pred_dis[i]
    tc=pred4.pred_bearing[i]
    lat1=math.radians(lat[i])
    lon1=math.radians(lon[i])
    pi=math.pi   
    
    a=math.asin(math.sin(lat1)*math.cos(d/3958)+math.cos(lat1)*math.sin(d/3958)*math.cos(tc))
    b=lon1+math.atan2((math.sin(tc)*math.sin(d/3958)*math.cos(lat1)),
                           (math.cos(d/3958)-math.sin(lat1)*math.sin(a)))
    
    a1=math.degrees(a)
    b1=math.degrees(b)
    lat.append(a1)
    lon.append(b1)

#---------------R1. plotting map-----------------------

#---------------R1.1 for static map----------------------- 
# download backgroud map
ruh_m= plt.imread("C:/Users/1181767/Desktop/map.png")
ruh_p= plt.imread("C:/Users/1181767/Desktop/map_predict.png")

# for mapping make plot
BBox = ((imo49_1.Longitude.min(),   imo49_1.Longitude.max(),      
         imo49_1.Latitude.min(), imo49_1.Latitude.max()))
BBox_P=((df_resultL["pred_long"].min(),df_resultL["pred_long"].max(),      
        df_resultL["pred_lat"].min(),df_resultL["pred_lat"].max()))

# BBox_P2=((pred4.pred_lon.min(),pred4.pred_lon.max(),      
#        pred4.pred_lat.min(),pred4.pred_lat.max()))

BBox_N = ((BBox_P[0], BBox[1], BBox[2], BBox_P[3]))


fig, ax = plt.subplots(figsize = (8,7))
ax.plot(imo49_3.Longitude, imo49_3.Latitude,'-o',c='b',label="present")
ax.plot(AISCyeff1["Longitude"], AISCyeff1["Latitude"],'o',c='g',label="efficiency")
ax.plot(df_resultL.pred_long, df_resultL.pred_lat,'-o',c="r",label="future")
# ax.scatter(df_resultL.pred_long, df_resultL.pred_lat, zorder=1, alpha= 1, c='r', s=50)
# ax.scatter(imo49_3.Longitude, imo49_3.Latitude, zorder=2, alpha= 1, c='b',s=50)
# ax.scatter(AISCyeff1["Longitude"], AISCyeff1["Latitude"], zorder=2, alpha= 1, c='g',s=50)
ax.legend()
ax.set_title('efficeiency')
ax.set_xlim(BBox_P[0],BBox[1])
ax.set_ylim(BBox[2],BBox_P[3])
ax.imshow(ruh_p, zorder=0, extent = BBox_N,aspect= 'equal')


#---------------R1.2 for dynamic map----------------------- 

import chart_studio.plotly as py
from plotly.graph_objs import *
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
import plotly.tools as tlsM
from IPython.display import HTML,IFrame

fig =go.Figure()
fig.add_trace(go.Scattermapbox(lat=list(imo49_3.Latitude),lon=list(imo49_3.Longitude), 
                               mode="markers+lines", marker=go.scattermapbox.Marker(
            size=5
        ),subplot='mapbox',name="現状"))
fig.add_trace(go.Scattermapbox(lat=list(df_resultL.pred_lat),lon=list(df_resultL.pred_long), 
                         mode="markers+lines", marker=go.scattermapbox.Marker(
            size=5
        ),subplot='mapbox',name="予測値"))
fig.add_trace(go.Scattermapbox(lat=list(AISCyeff1.Latitude),lon=list(AISCyeff1.Longitude), 
                         mode="markers", marker=go.scattermapbox.Marker(
            size=5
        ),subplot='mapbox',name="燃費"))


fig.update_layout(
    autosize=True,
    hovermode='closest',
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
# fig.update_layout(yaxis=dict(range=[11.958866666666667, 43.329345210459884]))
# fig.update_layout(xaxis=dict(range=[10.306791038154024, 61.47988333333333]))

# pio.renderers.default = 'browser'
# pio.show(fig)
fig.show()


#---------------R1.3 for dynamic map with datetime pointer (with hovertemplate = index(datetime)) ----------------------- 


fig =go.Figure()
fig.add_trace(go.Scattermapbox(lat=list(df_resultL.Latitude),lon=list(df_resultL.Longitude),
                               mode="markers+lines", marker=go.scattermapbox.Marker(
            size=5
        ),subplot='mapbox',name="現状",hovertemplate =df_resultL.index))
fig.add_trace(go.Scattermapbox(lat=list(df_resultL.pred_lat),lon=list(df_resultL.pred_long), 
                         mode="markers+lines", marker=go.scattermapbox.Marker(
            size=5
        ),subplot='mapbox',name="予測値",hovertemplate =df_resultL.index))
fig.add_trace(go.Scattermapbox(lat=list(AISCyeff1.Latitude),lon=list(AISCyeff1.Longitude),
                         mode="markers", marker=go.scattermapbox.Marker(
            size=5
        ),subplot='mapbox',name="燃費",hovertemplate =AISCyeff1.index))


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
# fig.update_layout(yaxis=dict(range=[11.958866666666667, 43.329345210459884]))
# fig.update_layout(xaxis=dict(range=[10.306791038154024, 61.47988333333333]))

# pio.renderers.default = 'browser'
# pio.show(fig)
fig.show()
