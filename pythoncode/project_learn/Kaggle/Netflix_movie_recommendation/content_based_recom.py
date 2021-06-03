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
df = pd.read_csv("../input/netflix-shows/netflix_titles.csv"")

# ---- <data cleansing> ----
# we need columns below. 
# [type, title, cast, country, rating, listed_in, description]

# delete unnecessary columns
df1 = df.copy()
df1.drop(columns=['show_id','date_added','release_year','director'],axis=1, inplace=True)

# handle with null data
df1.isnull().sum()

dfv1 = df1.copy()
ncol=['cast','country','rating']
values = {'cast': 'nodata', 'country': 'nodata', 'rating': 'nodata'}
dfv1.fillna(value=values,inplace=True)

# ------ < NLP and cosine similarity > ------
# A. convert to numerical 
# A.1. TF-IDF :  listed_in
# what is TF-IDF:  https://en.wikipedia.org/wiki/Tf–idf

# A.2. one-hot-encoding with TF: description, cast, country
# A.3. categorical: type, rating

# B. get cosine similarity
# B.1 TF-IDF(listed_in) & one-hot(country) & categorical
# B.2 TF-IDF(description) & one-hot(country) & categorical
# B.3 one-hot encoding & categorical

# A.1 TF-IDF 
# listed_in

# exclude word 'Movies', 'TV' because we have type field 
# generage new columns for tf-idf
exclude_wd = set(['movies','tv','&'])
f = lambda x: ' '.join(w for w in x.split() if not w in exclude_wd)
# generate new column 'genre'
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

# tf-idf: how important the word is to a document(per each title)
# it doesn't recognize '-' as word, so 'sci-fi' would be splited into 'sci' and 'fi'
# each index would be the order of titles
from sklearn.feature_extraction.text import TfidfVectorizer
tfidfv_g = TfidfVectorizer().fit(arr_g)
tfidfv_g_r = tfidfv_g.transform(arr_g).toarray() # get tf-idf
# get each word list
tfidfv_g_v = sorted(tfidfv_g.vocabulary_.items(), key=lambda x: x[1]) 
voc_gt = []
for i in tfidfv_g_v:
    voc_gt.append(i[0])
# get dataframe with tf-idf
tfidfv_g_df = pd.DataFrame(tfidfv_g_r , columns = voc_gt)
# tfidfv_g_df = tfidfv_g_df.reindex(sorted(tfidfv_g_df.columns), axis=1)
print('tf-idf')
display(tfidfv_g_df.head(5))

# A.2. one-hot-encoding with TF: description, cast, country
# 1) description
# too many description so extract only NOUN(NN)
# but too many time spent

import nltk
arr_d = dfv1['description']

voc_d = []
for text in arr_d:
    term = nltk.word_tokenize(text)
    qu = nltk.pos_tag(term)
    for e in qu:
        if e[1]=='NN':
            voc_d.append(e[0])
            
voc_ds=list(set(voc_d))

# tf
voc_d_count = []
for i in range(len(arr_d)): 
    voc_d_count.append([])
    d = arr_d[i]
    for j in range(len(voc_ds)):
        t = voc_ds[j]        
        voc_d_count[-1].append(tf(t, d))

tf_d = pd.DataFrame(voc_d_count, columns = voc_ds)
print('term count')
display(tf_d.head(5))
               
# 2) cast ; too many cast so catch only first cast
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
                 
# 3) country; catch only first country
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
                         
# B. get cosine similarity 
# drop unnecessary column
dfv2 =dfv1.drop(columns=['cast','country','duration','listed_in','description','genre'],axis=1)

# B.1 TF-IDF(listed_in) & one-hot(country) & categorical(type,rating) (without cast)
# B.2 TF-IDF(description) & one-hot(country) & categorical
# B.3 one-hot encoding & categorical

# listed_in = tfidfv_g_df / description = tfidfv_d_df
# one-hot(country) = tf_ct / one-hot(cast) = tf_c
# categorical = dfv1['type'] , dfv1['rating'] 
                 
# B.1 TF-IDF(listed_in) & one-hot(country) & categorical (without cast)
result_B1 = pd.concat([dfv2, tfidfv_g_df, tf_ct], join='outer', axis=1)
display(result_B1.head(5))                 
                 
def recommend_genre(title):
    if title in list(result_B1['title']):
        mov=result_B1[result_B1['title']==title]
        dfn= result_B1[result_B1['title']!=title]
        new_df = dfn.copy()
        new_df.loc[1, 'cos'] = 'ok' #to avoid pandas copywarning
        n0 = new_df.shape[0]
        n1 = new_df.shape[1]
        t = np.array(mov.iloc[0,np.r_[0,2:n1-1]])
        for i in range(n0):
            c = cos_sim(np.array(new_df.iloc[i,np.r_[0,2:n1-1]]),t)
            new_df.loc[i+1, 'cos'] = c

        sort = new_df.sort_values('cos',ascending=False)
        title_5 = sort.head(5)
        return title_5[['title','cos']]
    else: return ('cannont find title you want')

# for example = print 5 movies similar to movie called '3%'
recommend_genre('3%')

# B.2 one-hot TF(description, country) & categorical(type, rating) (without cast)
# because columns are duplicated with word of description, rename column of dfv2
dfv3=dfv2.rename(columns={'title': 'mov_title','type':'tvmovtype','rating': 'aged_type'})
result_B2 = pd.concat([dfv3,tf_d, tf_ct], join='inner', axis=1)
display(result_B2.head(5))
                 
# it would take time because of over 5000 words so quit
def recommend_description(title):
    if title in list(result_B2['mov_title']):
        mov=result_B2[result_B2['mov_title']==title]
        dfn= result_B2[result_B2['mov_title']!=title]
        new_df = dfn.copy()
        new_df.loc[1, 'cos'] = 'ok' # to avoid pandas copywarning
        n0 = new_df.shape[0]
        n1 = new_df.shape[1]
        t = np.array(mov.iloc[0,np.r_[0,2:n1-1]])
        for i in range(n0):
            c = cos_sim(np.array(new_df.iloc[i,np.r_[0,2:n1-1]]),t)
            new_df.loc[i+1, 'cos'] = c

        sort = new_df.sort_values('cos',ascending=False)
        title_5 = sort.iloc[:5,:]
        return title_5[['mov_title','cos']]
    else: return ('cannont find title you want')
# for example = print 5 movies similar to movie called '3%'
recommend_description('3%')
                 
# B.3 one-hot encoding & categorical
# one-hot encoding = cast, country
# categorical=type, rating
result_B3 = pd.concat([dfv2, tf_c, tf_ct], join='outer', axis=1)
display(result_B3.head(5))
                 
# it would take time 
def recommend_cast_country(title):
    if title in list(result_B3['title']):
        mov=result_B3[result_B3['title']==title]
        dfn= result_B3[result_B3['title']!=title]
        new_df = dfn.copy()
        new_df.loc[1, 'cos'] = 'ok' # to avoid pandas copywarning
        n0 = new_df.shape[0]
        n1 = new_df.shape[1]
        t = np.array(mov.iloc[0,np.r_[0,2:n1-1]])
        for i in range(n0):
            c = cos_sim(np.array(new_df.iloc[i,np.r_[0,2:n1-1]]),t)
            new_df.loc[i+1, 'cos'] = c

        sort = new_df.sort_values('cos',ascending=False)
        title_5 = sort.iloc[:5,:]
        return title_5[['title','cos']]
    else: return ('cannont find title you want')
# for example = print 5 movies similar to movie called '3%'
recommend_cast_country('3%')
                 
# # Option
# # tf-idf for manually for description 
# voc_d=[]
# for text in arr_d:
#     term = nltk.word_tokenize(text)
#     qu = nltk.pos_tag(term)
#     for e in qu:
#         if e[1]=='NN':
#             voc_d.append(e[0])
            
# voc_ds=list(set(voc_d))
# N = len(arr_d) 

# def idf(t):
#     df = 0
#     for doc in arr_d:
#         df += t in doc
#     return log(N/(df + 1))

# tf_d = []
# for i in range(N): 
#     tf_d.append([])
#     d = arr_d[i]
#     for j in range(len(voc_ds)):
#         t = voc_ds[j]        
#         tf_d [-1].append(tf(t, d))
# tf_Df= pd.DataFrame(tf_d, columns = voc_ds)

# idf_d = []
# for j in range(len(voc_ds)):
#     t = voc_ds[j]
#     idf_d.append(idf(t))

# idf_Df = pd.DataFrame(idf_d , index = voc_ds, columns = ["IDF"])

# #td_idf
# for i in range(tf_Df.shape[0]):
#     idf = idf_Df.iloc[0,:].values[0]
#     tf_Df.iloc[:,i]=tf_Df.iloc[:,i]*idf                 
                 
                 
