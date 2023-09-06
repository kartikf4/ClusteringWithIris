# -*- coding: utf-8 -*-
"""clusteringwithiris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HJx36szXxkfmry5AjmQ02qUlxXcguojS
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
# %matplotlib inline

df = pd.read_csv('/iris.csv')

df.head()

df.tail()

df.describe()

plt.scatter(df['petal.length'],df['petal.width'])
plt.xlabel('petal_length')
plt.ylabel('petal_width')



km =KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['petal.length','petal.width']])
y_predicted

df['cluster']=y_predicted
df.head()
df.tail()

km.cluster_centers_

df1=df[df.cluster==0]
df2=df[df.cluster==1]
df3=df[df.cluster==2]

plt.scatter(df1['petal.length'],df1['petal.width'],color= 'red')
plt.scatter(df2['petal.length'],df2['petal.width'],color= 'green')
plt.scatter(df3['petal.length'],df3['petal.width'],color= 'black')
plt.xlabel('petal.length')
plt.ylabel('petal.width')

plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.scatter(df1['petal.length'],df1['petal.width'],color= 'red')
plt.scatter(df2['petal.length'],df2['petal.width'],color= 'green')
plt.scatter(df3['petal.length'],df3['petal.width'],color= 'black')
plt.xlabel('petal.length')
plt.ylabel('petal.width')

SSE=[]
k_rnge = (1,10)
for k in k_rnge :
  km = KMeans(n_clusters=k)
  km.fit(df[['petal.length','petal.width']])
  SSE.append(km.inertia_)

SSE

plt.xlabel('k')
plt.ylabel('sse')
plt.plot(k_rnge,SSE)

scaler =MinMaxScaler()
scaler.fit(df[['petal.length']])
df['petal.length']=scaler.transform(df[['petal.length']])

scaler.fit(df[['petal.width']])
df['petal.width']=scaler.transform(df[['petal.width']])


df.head()

plt.scatter(df['petal.length'],df['petal.width'])
plt.xlabel('petal_length')
plt.ylabel('petal_width')

km =KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['petal.length','petal.width']])
y_predicted

df['cluster']=y_predicted
df.head()
df.tail()

km.cluster_centers_

df1=df[df.cluster==0]
df2=df[df.cluster==1]
df3=df[df.cluster==2]

plt.scatter(df1['petal.length'],df1['petal.width'],color= 'red')
plt.scatter(df2['petal.length'],df2['petal.width'],color= 'green')
plt.scatter(df3['petal.length'],df3['petal.width'],color= 'black')
plt.xlabel('petal.length')
plt.ylabel('petal.width')

plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.scatter(df1['petal.length'],df1['petal.width'],color= 'red')
plt.scatter(df2['petal.length'],df2['petal.width'],color= 'green')
plt.scatter(df3['petal.length'],df3['petal.width'],color= 'black')
plt.xlabel('petal.length')
plt.ylabel('petal.width')

SSE=[]
k_rnge = (1,10)
for k in k_rnge :
  km = KMeans(n_clusters=k)
  km.fit(df[['petal.length','petal.width']])
  SSE.append(km.inertia_)

SSE

plt.xlabel('k')
plt.ylabel('sse')
plt.plot(k_rnge,SSE)