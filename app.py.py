#!/usr/bin/env python
# coding: utf-8

import time
import pandas as pd

#!pip install imbalanced-learn
$ pip install imblearn

import imbalanced-learn.imblearn
from imblearn.over_sampling import RandomOverSampler

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.svm import SVC
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import StackingClassifier


df= pd.read_csv(r"C:\Users\chels\Desktop\creditcard.csv")
 
# seperate data for analysis
legit=df[df.Class==0]
fraud=df[df.Class==1]
legit_data=legit.sample(n=492)
df2=pd.concat([legit_data,fraud], axis=0)
X=df2.drop(columns='Class',axis=1)
Y=df2['Class']
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split 
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=42)


#!pip install xgboost
import xgboost as xgb

lr= LogisticRegression(solver='lbfgs', max_iter=1000)
svm = SVC(gamma = 'auto', kernel = 'linear', decision_function_shape='ovo')
xg = xgb.XGBClassifier(objective= 'binary:logistic', n_estimators = 10, seed= 123)

estimators= [('svm', svm), ('logreg', lr)]
 
stack = StackingClassifier(estimators=estimators, final_estimator=xg)
stack.fit(X_train,Y_train)

#pred= stack.predict(X_test)

b_type = ["fraud","legit"]



import streamlit as st

st.title('Interactive Text Input Example')
st.write('enter transactions details')

time= st.number_input(label='time',step=1.,format="%.2f")

v1 = st.number_input(label='transaction1',step=1.,format="%.2f")
v2 = st.number_input(label='transaction2',step=1.,format="%.2f")
v3 = st.number_input(label='transaction3',step=1.,format="%.2f")
v4 = st.number_input(label='transaction4',step=1.,format="%.2f")
v5 = st.number_input(label='transaction5',step=1.,format="%.2f")
v6 = st.number_input(label='transaction6',step=1.,format="%.2f")
v7 = st.number_input(label='transaction7',step=1.,format="%.2f")
v8 = st.number_input(label='transaction8',step=1.,format="%.2f")
v9 = st.number_input(label='transaction9',step=1.,format="%.2f")
v10 = st.number_input(label='transaction10',step=1.,format="%.2f")
v11 = st.number_input(label='transaction11',step=1.,format="%.2f")
v12 = st.number_input(label='transaction12',step=1.,format="%.2f")
v13 = st.number_input(label='transaction13',step=1.,format="%.2f")
v14 = st.number_input(label='transaction14',step=1.,format="%.2f")
v15 = st.number_input(label='transaction15',step=1.,format="%.2f")
v16 = st.number_input(label='transaction16',step=1.,format="%.2f")
v17 = st.number_input(label='transaction17',step=1.,format="%.2f")
v18 = st.number_input(label='transaction18',step=1.,format="%.2f")
v19 = st.number_input(label='transaction19',step=1.,format="%.2f")
v20 = st.number_input(label='transaction20',step=1.,format="%.2f")
v21 = st.number_input(label='transaction21',step=1.,format="%.2f")
v22 = st.number_input(label='transaction22',step=1.,format="%.2f")
v23= st.number_input(label='transaction23',step=1.,format="%.2f")
v24 = st.number_input(label='transaction24',step=1.,format="%.2f")
v25 = st.number_input(label='transaction25',step=1.,format="%.2f")
v26 = st.number_input(label='transaction26',step=1.,format="%.2f")
v27 = st.number_input(label='transaction27',step=1.,format="%.2f")
v28= st.number_input(label='transaction28',step=1.,format="%.2f")
amt= st.number_input(label='amount',step=1.,format="%.2f")

data = {'Time': time, 'v1':v1, 'v1':v1, 'v1':v1, 'v1':v1,'v1':v1,'v1':v1,'v1':v1,'v1':v1,'v1':v1,'v1':v1,'v1':v1,'v1':v1,'v1':v1,'v1':v1,'v1':v1,'v1':v1,'v1':v1,
        'v1':v1,'v1':v1,'v1':v1, 'v1':v1,'v1':v1,'v1':v1,'v1':v1,'v1':v1,'v1':v1,'v1':v1,'v1':v1,'amt':amt}  
  
tester = pd.DataFrame(data)
pred = stack.predict(tester)
if pred== 1:
  st.write('FRAUD')
else:
  st.write('LEGIT')

  
