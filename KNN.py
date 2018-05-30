import numpy as np
import pandas as pd
from sklearn import preprocessing,cross_validation,neighbors,svm

df=pd.read_csv('C:\\Users\\anurag\\Desktop\\breast-cancer.txt')

df.drop(['id'],1,inplace=True)

df.replace('?',-99999,inplace=True)

X=np.array(df.drop(['class'],1))
y=np.array(df['class'])

X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=.2)

cf=neighbors.KNeighborsClassifier()

cf.fit(X_train,y_train)
accuracy=cf.score(X_test,y_test)
print(accuracy)

sample=np.array([3,8,3,8,8,8,3,8,8])
sample=sample.reshape(1,-1)
x=cf.predict(sample)
print(x)
