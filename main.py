import pandas as pd
from joblib import load
import streamlit as st
import pandas as pd
import numpy as np

model = load('Final Model.joblib')

# test = pd.read_csv('test.csv')
# test.drop('Name',axis=1,inplace=True)
# sex = pd.get_dummies(test['Sex'],drop_first=True,dtype='int')
# Embarked = pd.get_dummies(test['Embarked'],drop_first=True,dtype='int')
# test = pd.concat([test,sex,Embarked],axis=1)
# test.drop(['Sex','Ticket','Embarked'],axis=1,inplace=True)
# test['Age'].fillna(np.mean(test['Age']),inplace=True)
# test.drop('Cabin',axis=1,inplace=True)
# test.drop('PassengerId',axis=1,inplace=True)
#
# print(test[test['Parch']>5])


st.title('Welcome to the Titanic Survived Prediction Model')
st.subheader('Enter the following Info to predict whether that person survived or not (0 for No,1 for Yes)')

Pclass = st.radio('Enter the Pclass:',('1','2','3'))
if Pclass=='1':
    Pclass=1
elif Pclass=='2':
    Pclass=2
else:
    Pclass=3


age = st.number_input('Enter age:')
SibSP = st.number_input('Enter number of Siblings:')
Parch = st.number_input('Enter parch: ')
Fare = st.number_input('Enter the Fare:')
male = st.radio("Select Gender: ",('Male','Female'))
if male=='Male':
    male = 1
else:
    male = 0

Q_class = st.radio('Select Q_class: ',('0','1'))
if Q_class=='1':
    Q_class=1
else:
    Q_class=0

S_class = st.radio("Select S_class: ",('0','1'))
if S_class=='1':
    S_class=1
else:
    S_class=0

if (st.button('Predict')):
    arr = np.array([[Pclass,age,SibSP,Parch,Fare,male,Q_class,S_class]])

    pred = model.predict(arr)
    if pred[0]==0:
        st.error(f'Not Survived')
    else:
        st.success(f'Survived')