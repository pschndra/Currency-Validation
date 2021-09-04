# -*- coding: utf-8 -*-
"""banknoteAuth.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12KZDMqDpsdnIfip3LStrRTawENx-Zljr
"""

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

df = pd.read_csv('/home/hunter/Free/projects/BankNote_Authentication.csv')

df

x= df.iloc[:,:-1]
y= df.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state = 0)

"""SVM"""

from sklearn.svm import SVC
csvm= SVC(kernel='linear')  
csvm.fit(x_train,y_train)

y_pred_svm=csvm.predict(x_test)
scnf=accuracy_score(y_test,y_pred_svm)
scnf

"""Applying decision tree classifier and checking the accuracy of classifier

"""

from sklearn.tree import DecisionTreeClassifier
dcf = DecisionTreeClassifier(criterion = "gini", 
            random_state = 100,max_depth=3, min_samples_leaf=5)
dcf.fit(x_train,y_train)

y_pred_dt=dcf.predict(x_test)
dcnf=accuracy_score(y_test,y_pred_dt)
dcnf

"""Applying the Random Forest classifier and checking the accurary"""

from sklearn.ensemble import RandomForestClassifier
cf = RandomForestClassifier()
cf.fit(x_train,y_train)

y_pred = cf.predict(x_test)

cnf = accuracy_score(y_test,y_pred)
cnf

import pickle
pickel_out = open("cf.pkl" , "wb")
pickle.dump(cf,pickel_out)
pickel_out.close()
