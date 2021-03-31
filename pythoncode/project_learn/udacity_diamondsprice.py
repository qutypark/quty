#-----------------------------import library------------------------------
import numpy as np
import pandas as pd

from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

import os
import sys

import matplotlib.pyplot as plt
%matplotlib inline 
import seaborn as sns
plt.style.use("ggplot")

#-----------------------------read dataset------------------------------
df = pd.read_csv("/diamonds.csv")

#-----------------------------preparation------------------------------
# color D is valuable, J is yellow(relatively low value)
# label encoding : make orinal data to numerical
df1 = df.copy()
df1["color_ord"]=df1["color"].map(lambda x: 6 if x=="D" else 5 if x=="E" else 4 if x=="F"
                             else 3 if x=="G" else 2 if x=="H" else 1 if x=="I" else 0)
#only numerical variable
dfN = df1[["carat","cut_ord","clarity_ord","color_ord","price"]]

#-----------------------------EDA------------------------------
#1 correlation
corr=dfN.corr()
mask=np.array(corr)
mask[np.tril_indices_from(mask)]=False

fig,ax=plt.subplots()
fig.set_size_inches(10,5)
sns.heatmap(corr, mask=mask, vmax=.9, square=True, annot=True)

# there is no collineraity
#  carat has high correlration with price


# scatter plot
fig = plt.figure(figsize=(16,10))
ax1= fig.add_subplot(1,4,1)
ax1.scatter(dfN.carat,dfN.price)
ax1.set_title("carat and price")
ax1.set_xlabel("carat")
ax1.set_ylabel("price")

ax2= fig.add_subplot(1,4,2)
ax2.scatter(dfN.cut_ord,dfN.price)
ax2.set_title("cut_ord and price")
ax2.set_xlabel("cut_ord")


ax3= fig.add_subplot(1,4,3)
ax3.scatter(dfN.clarity_ord,dfN.price)
ax3.set_title("clarity_ord and price")
ax3.set_xlabel("clarity_ord")


ax4= fig.add_subplot(1,4,4)
ax4.scatter(dfN.color_ord,dfN.price)
ax4.set_title("color_ord and price")
ax4.set_xlabel("color_ord")


plt.show()

# maybe better to to linear regression only with carat
# but this time, with all predictive variance


# make model of linear regression with OLS 

#OLS for all (carat, cut_ord, clarity_ord)
names="+".join(dfN.columns[:-1])
model=smf.ols(formula="price~"+names,data=dfN)
result=model.fit()

display(result.summary())

# Omnibus,Skewness and kurtosis is way higher than 0 (residual is not normally distributed)
# Durbin-Watson is near to 2: risk of autocorrelation is low
# So it would be better to do Logistic Regression than Linear, but Y value is continuous so it has to be linear 

# but this time only focused on R-Squared
# linear regression model 
# f(x) = -0.6734 + 8727*carat + 161*cut_ord + 494*clartiy_ord + 303*color_ord


#-------------------apply model-----------------------

#-------------------read_data without price(label) -----------------------
dfP = pd.read_csv("/new-diamonds.csv")

dfP1 = dfP.copy()
# label encoding
dfP1["color_ord"]=dfP1["color"].map(lambda x: 6 if x=="D" else 5 if x=="E" else 4 if x=="F"
                             else 3 if x=="G" else 2 if x=="H" else 1 if x=="I" else 0)
#only numerical data
dfPN = dfP1[["carat","cut_ord","clarity_ord","color_ord"]]

predicted_price = [None]*dfPN.shape[0]
for i in range(dfPN.shape[0]):
    predicted_price[i]= -0.6734 + (8727*dfPN["carat"][i])+(161*dfPN["cut_ord"][i])+(494*dfPN["clarity_ord"][i])+(303*dfPN["color_ord"][i]) 
    
dfPN["Prdicted_Price"] = predicted_price
dfPN["recommend_bid"] = dfPN["Prdicted_Price"]/100*70


# option : Sklearn.linear_model LinearRegression

X = dfN.drop(columns="price")
y = dfN.price
#StandardScaler
from sklearn.preprocessing import StandardScaler
sc= StandardScaler()
X_scaled= sc.fit_transform(X)
#train-test split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,test_size=0.3)

#-------------Linear Regression --------------------------
from sklearn.linear_model import LinearRegression
linearmodle = LinearRegression().fit(X,y)

r_sq = linearmodle.score(X,y)
print(r_sq,linearmodle.intercept_,linearmodle.coef_)

# which is similar to results of OLS estimator 
