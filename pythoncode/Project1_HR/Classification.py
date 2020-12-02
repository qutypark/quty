

# 0. import library 
import numpy as np
import pandas as pd

from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

import matplotlib.pyplot as plt
%matplotlib inline 
import seaborn as sns
plt.style.use("ggplot")

pd.set_option("display.max_columns",None)

# 0. read dataset 
# data: GAB and assessment data of in-house company /  GAB data of candidates

# 0.1 standard data = GAB and assessment data of in-house company
train=pd.read_excel("C:/local",encoding="cp932")
# Lable: categorial (Ordinal)=  H/M/L
# Explanatory variable:numerical(Continuous)= score of each GAB 

# 0.2 apply data; GAB data of candidates
test=pd.read_csv("C:/local",encoding="cp932")

# 1. check dataset
# null data 
for i,n in enumerate(train.isnull().sum()):
    if n>0:print(i)
    elif n==0:pass
# check datatype
for i,a in enumerate(train.dtypes):
    if a=="object":
        print(train.iloc[:,i].value_counts())

# 2．data cleansing 
# leave only necessary varibable
b=[0,1]+list(range(10,train.shape[1]))
train= train.iloc[:,b]
#Label Encoding: convert Ordinal data to numerical
train["V57"]=train["V57"].map(lambda x: 0 if x=="C" else 1 if x=="B" else 2) 
train["label"]=train["label"].map(lambda x: 0 if x=="LP" else 1 if x=="M" else 2) 


# 3．EDA
# as result, Explanatory variable are weak to explain label data

# 3．1 correlation
# as result, there is no correlation above 0.5


#exclude categorical data
train["ID"]=pd.Categorical(train.ID)
traincorr=train.corr()
mask=np.array(traincorr)
mask[np.tril_indices_from(mask)]=False

# for heatmap 
fig,ax=plt.subplots()
fig.set_size_inches(50,40)
sns.heatmap(traincorr, mask=mask, vmax=.9, square=True, annot=True)


# 3．2  KMeans cluster with PCA
#PCA -> extract main value of cluster and make it visible via 2d Plot
#compare [lable with PCA] vs [new cluster with PCA] -> check whether current data is good or not


from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# 1) normalize
# exclude categorical data and label
train1=train.iloc[:,2:]
train_max = train1.max().max()
train_min = train1.min().min()

train_nm = (train1- train_min) / (train_max - train_min)
xn=train_nm.values

# 2)calculate PCA, parameter: n_components
# there is difference between each of parameter but,,for 2d graph -> PCA n_components=2 

# 2.1) parameter: n_components="mle"
pca = PCA(n_components="mle")
principalComponents = pca.fit_transform(xn)

# n_components="mle" 
principalDf = pd.DataFrame(data = principalComponents)
kmeansmle=KMeans(n_clusters=3).fit(principalDf)

# n_components="mle" [new cluster with PCA]
principalDf["c3"]=kmeansmle.labels_

# 2.2)oaraneter: n_components=2 for 2D
pca2 = PCA(n_components=2,svd_solver="randomized")
principalComponents2 = pca2.fit_transform(xn)
# n_components=2 
principalDf2 = pd.DataFrame(data = principalComponents2)
kmeans2=KMeans(n_clusters=3).fit(principalDf2)

# n_components=2,[new cluster with PCA]
principalDf2["c3"]=kmeans2.labels_

# 2.3) n_components="mle" vs n_components=2 2D
print("n_components=mle",pca.explained_variance_ratio_)
print("n_components=2",pca2.explained_variance_ratio_)

display("n_components=mle",principalDf["c3"].value_counts())
display("n_components=2",principalDf2["c3"].value_counts())

# 3) make dataframe with label and PCA = [label with PCA]
finalDf2 = pd.concat([principalDf2, train[["label"]]], axis = 1)

# 4) [label with PCA] vs [new cluster PCA]
# as result, each of 2d graph are non idendical 
# furthermore, distance of each cluster are too close to be classified -> hard to make classification

fig = plt.figure(figsize = (16,8))

ax= fig.add_subplot(1,2,1)
ax.set_xlabel('PC1', fontsize = 15)
ax.set_ylabel('PC2', fontsize = 15)
ax.set_title('2 PCA with HML', fontsize = 20)

ax1= fig.add_subplot(1,2,2)
ax1.set_xlabel('PC1', fontsize = 15)
ax1.set_ylabel('PC2', fontsize = 15)
ax1.set_title('2 PCA with kmeans', fontsize = 20)

#[label with PCA]=2 PCA with HML
targets =finalDf2.label.unique()
colors = ['b', 'g', 'r']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf2['label'] == target
    ax.scatter(finalDf2.loc[indicesToKeep, 0]
               , finalDf2.loc[indicesToKeep, 1]
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()

#[new cluster PCA]=2 PCA with kmeans
targets1 =finalDf2.c3.unique()
colors1 = ['b', 'g', 'r']
for target, color in zip(targets1,colors1):
    indicesToKeep = finalDf2['c3'] == target
    ax1.scatter(finalDf2.loc[indicesToKeep, 0]
               , finalDf2.loc[indicesToKeep, 1]
               , c = color
               , s = 50)
ax1.legend(targets1)
ax1.grid()

plt.show

#  4．Feature Engineering


# 4.1 ordinary least squares(OLS) -> Backward elimination for min AIC 

Names=[]
AIC=[]
Drop=[]
Features=[]
train1=train.drop(columns=["ID"],axis=1)
for i in train1.columns[1:]:
    if len(Drop)==0:
        names="+".join(train1.columns[1:])
        model=smf.ols(formula="label~"+names,data=train1)
        result=model.fit()
        Drop.append(i)
        Names.append(names)
        Features.append(train1.columns.values)
        AIC.append(result.aic)
    elif len(Drop)>0:
        traind=train1.drop(columns=Drop,axis=1)
        names="+".join(traind.columns[1:])
        model=smf.ols(formula="label~"+names,data=traind)
        result=model.fit()
        Drop.append(i)
        Names.append(names)
        Features.append(traind.columns.values)
        AIC.append(result.aic)
backAICdf=pd.DataFrame({"features":Features,"Name":Names,"AIC":AIC})
minAIC=backAICdf[backAICdf["AIC"]==min(backAICdf["AIC"])]

# 4.1 build regression model(OLS) with min AIC  
# *caution*adjusted coefficient of determination is low(0.044 )
trainf=train1.loc[:,minAIC.features.values[0]]
modelf=smf.ols(formula="label~"+minAIC.Name.values[0],data=trainf)
resultf=modelf.fit()
display("OLS with minAIC",resultf.summary())

# 4.2 Exponential function -> can check change from 1 increase
# hyp: ( type I error) Pv < 0.05 
est=np.exp(resultf.params)
estp=100*(est-1).round(2)
Pv=resultf.pvalues
Namef=est.index.values
df_MS_=pd.DataFrame({"Name":Namef,"est":est,"estp":estp,"Pv":Pv})

df_MS_=df_MS_.iloc[1:,:]
df_MS_0=df_MS_[df_MS_.Pv<0.05]
display("result summary",df_MS_0)

# 4.3 result data with feature engineering
cr=["label"]+list(df_MS_0.Name.values)
trainResult=trainf.loc[:,cr]


# 5.Classification: result data with feature engineering

# 5.1 split train set, test set
x=trainResult.drop(columns=["label"])
y=trainResult.label
#Standard Scale
from sklearn.preprocessing import StandardScaler
sc= StandardScaler()
X_scaled= sc.fit_transform(x)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,test_size=0.3)

# 5.2 ML: because dataset is too small, there is high risk of overfitting -> ensemble library should be needed
#RandomForest
from sklearn.ensemble import RandomForestClassifier
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, y_train)
Y_predRF = random_forest.predict(X_test)
acc_random_forest = round(random_forest.score(X_train, y_train) * 100, 2)

#AdaBoost
from sklearn.ensemble import AdaBoostClassifier
AdaBoost =  AdaBoostClassifier(n_estimators=100)
AdaBoost.fit(X_train, y_train)
Y_predAda = AdaBoost.predict(X_test)
acc_AdaBoost = round(AdaBoost.score(X_train, y_train) * 100, 2)

#GBM
from sklearn.ensemble import GradientBoostingClassifier
GBM = GradientBoostingClassifier(n_estimators=100)
GBM.fit(X_train, y_train)
Y_predGBM = GBM.predict(X_test)
acc_GBM=round(GBM.score(X_train, y_train)*100, 2)

#compare accuracy

from sklearn.metrics import accuracy_score

models = pd.DataFrame({'Model': ['RandomForest', 'AdaBoost', 'GBM'],
    'Score': [acc_random_forest, acc_AdaBoost, acc_GBM]})
models.sort_values(by='Score', ascending=False)


# 5.1 Classification;with Euclidiean 

#candidate assessment(future)= short distance with in-house company assess  
#representative value =median <- escape from outlier effect because of small dataset

def smallest(num1, num2, num3):
    if (num1 < num2) and (num1 < num3):
        return num1
    elif (num2 < num1) and (num2 < num3):
        return num2
    else:
        return num3

# 5.1.1 median of in-house company data

#ols result
feature=list(df_MS_0.Name.values)

th=trainResult[trainResult.label==2]
tm=trainResult[trainResult.label==1]
tl=trainResult[trainResult.label==0]

th_med=np.array(th[feature].median()) 
tm_med=np.array(tm[feature].median()) 
tl_med=np.array(tl[feature].median())

# 5.1.2 
es=test[feature]


#5.1.3 calssification with euclidean 
es_th=[]
es_tm=[]
es_tl=[]
es_label=[]

for i in range(es.shape[0]):
    h=np.linalg.norm(np.array(es.iloc[i,:])-th_med)
    m=np.linalg.norm(np.array(es.iloc[i,:])-tm_med)
    l=np.linalg.norm(np.array(es.iloc[i,:])-tl_med)
    if smallest(h,m,l)==h:
        lab="H"
    elif smallest(h,m,l)==m:
        lab="M"
    elif smallest(h,m,l)==l:
        lab="L"
    else: lab="X"
    es_th.append(h)
    es_tm.append(m) 
    es_tl.append(l) 
    es_label.append(lab)
    
eshml=pd.DataFrame({"h":es_th,"m":es_tm,"l":es_tl,"label":es_label})

# complete candidate data
testR=pd.concat([test1["ID"],es,eshml],axis=1)
display(testR.head())

# 6. make chart
# 6.1 radar chart
labels=feature
#Threshold: ols result and median of highperformance data 

th= pd.DataFrame({"val":th_med},index=feature)
tr1=np.concatenate((th.values,[th.values[0]]))

#compare data : candidate data 
testR0=testR[testR["ID"]==0]
val=testR0[feature].values[0]
testR0m=pd.DataFrame({"val":val},index=feature)
es0=np.concatenate((testR0m.values,[testR0m.values[0]]))

# create backgroud radar chart
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
angles=np.concatenate((angles,[angles[0]]))

fig=plt.figure()
ax= fig.add_subplot(111, polar=True)
fig.set_size_inches(6,6)
ax.set_title("radar")


# radar chart of Threshold(in-house company data)  
ax.plot(angles, tr1, 'o-', linewidth=1,label="HP",color="b")
ax.set_thetagrids(angles * 180/np.pi, labels)

# candidate  radar chart 
ax.plot(angles,es0, 'o-', linewidth=1,label="candidate",color="green")
ax.fill(angles,es0,"green",alpha=0.25)
ax.set_thetagrids(angles * 180/np.pi, labels)
ax.grid(True)
plt.legend(loc="upper right",bbox_to_anchor=(0.1,0.1))



