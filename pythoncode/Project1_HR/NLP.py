﻿# imort library

import numpy as np
import pandas as pd
import re

from scipy import stats
import statsmodels.api as smz
import statsmodels.formula.api as smf

from sklearn import preprocessing 

import matplotlib.pyplot as plt


%matplotlib inline 
import seaborn as sns
plt.style.use("ggplot")
pd.set_option("display.max_columns",None)

#------------------ 0. read data ----------------------
# purpose: analyze words of cv document from applicants who passed final interview

df=pd.read_csv("C:/localpath.csv",encoding="cp932",dtype="str")

#------------------ 1. data cleansing  ----------------------
# get unique list to drop the variances which is not meaningful(has less than 1 unique data)
uni=df.nunique()
uni01=uni[uni<=1].index.values.tolist()
df01New=df.drop(columns=uni01)

#------------------ 2. Feature Engineering  ----------------------

# 1) label encoding for categorical data 
# Pass・Fail・etc・Nan -> to numeric

df01New=df01New.fillna("")

# since expression pass or fail is located in between character  '【' -> split it
# only for PassFail on inverview process
df01New=df01New.fillna("")
for i in ['PF_sc1', 'PF_lib1', 'PF_sc2', 'PF_lib2', 'PF_scL','PF_libL']:
    df01New[i]=df01New[i].apply(lambda x:"N" if x=="" else x.split('【')[0])

# only for PassFail on inverview process and test
for i in ['test','PF_sc1', 'PF_lib1', 'PF_sc2', 'PF_lib2', 'PF_scL','PF_libL']:
    df01New[i]=df01New[i].map(lambda x: 2 if x=="pass " else 1 if x=="resign" else 0) 


# 2) integrate pass/fail column  because each pass/fail result is separated by major of applicant
def PF_1(row): # for first interview
    if row['PF_sc1']==2 or row['PF_lib1']==2:
        return(2)
    if row['PF_sc1']==1 or row['PF_lib1']==1:
        return(1)
    if row['PF_sc1']==0 or row['PF_lib1']==0:
        return(0)
def PF_2(row): # for second interview
    if row['PF_sc2']==2 or row['PF_lib2']==2:
        return(2)
    if row['PF_sc2']==1 or row['PF_lib2']==1:
        return(1)
    if row['PF_sc2']==0 or row['PF_lib2']==0:
        return(0)
def PF_L(row): # for last(final) interview
    if row['PF_scL']==2 or row['PF_libL']==2:
        return(2)
    if row['PF_scL']==1 or row['PF_libL']==1:
        return(1)
    if row['PF_scL']==0 or row['PF_libL']==0:
        return(0)   

df01New["PF_1"] = df01New.apply (lambda row: PF_1(row), axis=1)  # for first interview
df01New["PF_2"] = df01New.apply (lambda row: PF_2(row), axis=1)  # for second interview
df01New["PF_L"] = df01New.apply (lambda row: PF_L(row), axis=1)  # for last(final) interview

# drop old columns
df01New=df01New.drop(columns=['PF_sc1', 'PF_lib1', 'PF_sc2', 'PF_lib2', 'PF_scL','PF_libL'])

#------------------ 3. NLP  ----------------------

#import library for japanese
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *


# specified condition for nlp
# filter mark such as .,
char_filters = [UnicodeNormalizeCharFilter(),
                RegexReplaceCharFilter('<.*?>', '')]
# mainly keep language which is Noun(= "名詞" in japanese) 
token_filters = [POSKeepFilter(['名詞']),
                 LowerCaseFilter(),
                 ExtractAttributeFilter('surface')]
a = Analyzer(char_filters=char_filters, token_filters=token_filters)

# split data by result of final(last) interview
copyp=df01New[df01New["PF_L"]==2].reset_index() # pass
copyn=df01New[df01New["PF_L"]==1].reset_index() # resign
copyf=df01New[df01New["PF_L"]==0].reset_index() # fail

# pass = result of final(last) interview
resultp=[]
for i in range(copyp.shape[0]):
    for x in a.analyze(copyp['value'][i]):
        resultp.append(x)
# resign = result of final(last) interview
resultn=[]
for i in range(copyn.shape[0]):
     for x in a.analyze(copyn["value"][i]):
        resultn.append(x)
# fail = result of final(last) interview
resultf=[]
for i in range(copyf.shape[0]):
    for x in a.analyze(copyf["value"][i]):
        resultf.append(x)

# make dictionary
from collections import Counter

word_dictP=dict(Counter(resultp))
word_dictN=dict(Counter(resultn))
word_dictF=dict(Counter(resultf))

# convert Dictionary to dataframe for word count

# pass
textP= pd.Series(word_dictP, name='textcount')
textP.index.name="value"
textP= textP.reset_index()

# resign
textN= pd.Series(word_dictN, name='textcount')
textN.index.name="value"
textN= textN.reset_index()

# fail
textF= pd.Series(word_dictF, name='textcount')
textF.index.name="value"
textF= textF.reset_index()

#check word count used by applicants who passed last(final) interview
textP.sort_values(by=['textcount'],ascending=False)

#------------------ 4. word cloud  ----------------------

# import library
from wordcloud import WordCloud, STOPWORDS

wc = WordCloud(background_color="white",width=500,height=500, max_words=10,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(word_dictP)
plt.imshow(wc)
from PIL import Image

