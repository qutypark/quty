# calculate matching score for content-based filtering
# cosine similarity 

# <import library>
import numpy as np
import pandas as pd

from math import log
import re

import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# for cosine similarity
from numpy import dot
from numpy.linalg import norm
def cos_sim(A, B):
       return dot(A, B)/(norm(A)*norm(B))

pd.set_option("display.max_columns",None)

# <read dataset>
df = pd.read_csv("/data/netflix_titles.csv")

# <data cleansing>
# we need columns below. 
# [type, title, director, cast, country, rating, listed_in, description]

# delete unnecessary columns
df1 = df.copy()
df1.drop(columns=['show_id','date_added','release_year'],axis=1, inplace=True)

# handle with null data
df1.isnull().sum()

# ver1. include columns which has null data
dfv1 = df1.copy()
ncol=['director','cast','country','rating']
values = {'director': 'nodata', 'cast': 'nodata', 'country': 'nodata', 'rating': 'nodata'}
dfv1.fillna(value=values,inplace=True)

# ver2. exclude columns which has null data
dfv2 = df1.dropna(axis=1)

# ------ < ver1; with null data > ------
# A. convert to numerical 
# A.1. TF-IDF :  listed_in, description
# what is TF-IDF:  https://en.wikipedia.org/wiki/Tf–idf

# A.2. one-hot-encoding: cast, country
# A.3. categorical: type, rating

# B. get cosine similarity
# B.1 TF-IDF(listed_in) & one-hot(country) & categorical
# B.2 TF-IDF(description) & one-hot(country) & categorical
# B.3 one-hot encoding & categorical

# A.1. TF-IDF 
# 1) listed_in

# exclude word 'Movies', 'TV' because we have type field 
# generage new columns for tf-idf
exclude_wd = set(['movies','tv','&'])
f = lambda x: ' '.join(w for w in x.split() if not w in exclude_wd)
dfv1['genre'] = dfv1['listed_in'].str.lower().replace(',','',regex=True)
dfv1['genre'] = dfv1['genre'].apply(f)

# count per term of genre
# each index would be the order of titles
def tf(t, d):
    return d.count(t)
arr_g = dfv1['genre']
voc_g = sorted(list(set(w for i in arr_g for w in i.split())))

voc_g_count = []
for i in range(len(arr_g)): 
    voc_g_count.append([])
    d = arr_g[i]
    for j in range(len(voc_g)):
        t = voc_g[j]        
        voc_g_count[-1].append(tf(t, d))

tf_g = pd.DataFrame(voc_g_count, columns = voc_g)
print('term count')
display(tf_g.head(5))

# tf-idf: to know how important the word is to a document(per each title)
# it doesn't recognize '-' as word, so 'sci-fi' would be splited into 'sci' and 'fi'
# each index would be the order of titles
from sklearn.feature_extraction.text import TfidfVectorizer

tfidfv_g = TfidfVectorizer().fit(arr_g)
tfidfv_g_r = tfidfv_g.transform(arr_g).toarray()
voc_gt= list(tfidfv_g.vocabulary_.keys()) 
tfidfv_g_df = pd.DataFrame(tfidfv_g_r , columns = voc_gt)
tfidfv_g_df = tfidfv_g_df.reindex(sorted(tfidfv_g_df.columns), axis=1)
print('tf-idf')
display(tfidfv_g_df.head(5))

# # A.1. TF-IDF 
# # 2) description
arr_d = dfv1['description']

tfidfv_g = TfidfVectorizer().fit(arr_d)
tfidfv_d_r = tfidfv_d.transform(arr_d).toarray()
voc_dt= list(tfidfv_d.vocabulary_.keys()) 
tfidfv_d_df = pd.DataFrame(tfidfv_d_r , columns = voc_dt)

print('tf-idf')
display(tfidfv_d_df.head(5))

# A.2. one-hot-encoding: cast, country
# 1) cast ; too many cast so catch only first cast
first_cast = []
for i in dfv1['cast']:
    a = i.split(',')[0]
    first_cast.append(a)
    
voc_cast=list(set(first_cast))
arr_c = dfv1['cast']

voc_c_count = []
for i in range(len(arr_c)): 
    voc_c_count.append([])
    d = arr_c[i]
    for j in range(len(voc_cast)):
        t = voc_cast[j]        
        voc_c_count[-1].append(tf(t, d))

tf_c = pd.DataFrame(voc_c_count, columns = voc_cast)
print("first cast count")
display(tf_c.head())

# 2) country; catch only first cast
first_cnt = []
for i in dfv1['country']:
    a = i.split(',')[0]
    first_cnt.append(a)

voc_cnt=list(set(first_cnt))
arr_ct = dfv1['country']

voc_ct = []
for i in range(len(arr_ct)): 
    voc_ct.append([])
    d = arr_ct[i]
    for j in range(len(voc_cnt)):
        t = voc_cnt[j]        
        voc_ct[-1].append(tf(t, d))

tf_ct = pd.DataFrame(voc_ct, columns = voc_cnt)
print('first country count')
display(tf_ct.head())

# A.3. categorical: type, rating

#  type: Movie = 0 / TV Show = 1 (nominal)
dfv1['type'] = dfv1['type'].apply(lambda x: 0 if x=='Movie' else 1)

# rating: more audlt, get higher number (ordinary)
dfv1['rating'] = dfv1['rating'].apply(lambda x: 0 if x=='UR' or x=='nodata' or x=='NR'
                                      else 1 if x=='TV-Y' else 2 if x=='TV-Y7'
                                     else 3 if x=='TV-Y7-FV' else 4 if x=='G' or x=='TV-G'
                                     else 5 if x=='PG' or x=='TV-PG' else 6 if x=='TV-14' or x=='PG-13'
                                     else 7 if x=='R' else 8 if x=='TV-MA' or x=='NC-17' else 9)
        
