import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
import xlrd
df=pd.read_excel('C:\\Users\\anurag\\Downloads\\titanic.xls')
df.drop(['name','body'],1,inplace=True)
df.fillna(0,inplace=True)

columns=df.columns.values
for column in columns :
    if df[column].dtype !=np.int64 and df[column].dtype !=np.float64:
        #print(column)
        dfset=set(df[column])
        dic={}
        x=0
        for i in dfset:
            dic[i]=x
            x=x+1
        j=0
        for i in df[column]:
            df.at[j,column]=dic[i]
            j=j+1

print(df.head())


df.drop(['sex','boat'], 1, inplace=True)
X = np.array(df.drop(['survived'], 1).astype(float))
X = preprocessing.scale(X)
y = np.array(df['survived'])

clf = KMeans(n_clusters=2)
clf.fit(X)
correct = 0
j=0

for i in X:
   #print(clf.predict([i]),' ',[y[j]])
   if [y[j]] == clf.predict([i]):
       correct=correct+1
       
   j=j+1 
     
print(correct/len(X))


