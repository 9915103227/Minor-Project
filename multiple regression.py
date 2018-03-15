import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv('finalData.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,9].values
'''from sklearn.preprocessing import LabelEncoder
x_le=LabelEncoder()
#x_le.fit(x[:,3])
x[:,3]=x_le.fit_transform(x[:,3])
from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(categorical_features=[3])
x=ohe.fit_transform(x).toarray()'''
#avoid dummy trap
#x=x[:,1:]
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)
#import statsmodels.formula.api as sm
#x=np.append(arr=np.ones((50,1)),values=x,axis=1)
#x_opt=x[:,[0,1,2,3,4,5]]
#lr=sm.OLS(endog=y,exog=x_opt).fit()
#lr.summary()'''
