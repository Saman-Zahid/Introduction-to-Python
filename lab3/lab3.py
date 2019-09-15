#part 1
from sklearn import datasets
import pandas as pd

#load data set
boston = datasets.load_boston()
#creating a dataframe using pandas 
df_boston = pd.DataFrame(boston.data,columns=boston.feature_names)
np.array(df_boston.columns)
#print(boston.data)
#print description
#print(boston.DESCR)

x = boston.data
print(df_boston.head())
print(df_boston['CRIM'])

#part 2
import numpy as np
from numpy.linalg import inv 

class OLS:
    
    def __init__(self, dataFrame, response):
        self.columnNames = np.insert(dataFrame.columns, 0, 'INT')
        
        self.X = dataFrame.as_matrix()
        self.Y = response
        
        
        #add intercept in martix
        intercept =  np.ones(shape=self.Y.shape)[..., None]
        self.X = np.concatenate((intercept, self.X), 1)
        
        
        #calculate cofficient
        self.coeffs = inv(self.X.transpose().dot(self.X)).dot(self.X.transpose()).dot(self.Y)
        
        #y_hat calculate
        self.yhat = self.X.dot(self.coeffs)
        
        #residual
        self.residual = self.Y - self.yhat
        
        #MSE
        self.mse = np.mean(self.Y - self.yhat)
        
    def get_beta(self):
        results = pd.DataFrame({'coefficients':self.coeffs}, index=self.columnNames)
        return results.round(2)
    
    def get_yhat(self):
        return self.yhat
    
    def get_residual(self):
        return self.residual
    
    def get_rmse(self):
        return self.mse
    
#adding a intercept by creating a one's
#intercept = np.ones((df_boston.shape[0],), dtype=np.int)
#df_boston = df_boston.insert(0,"intercept",intercept)
#print(df_boston.head())

obj = OLS(df_boston,boston.target)
obj.get_beta()

X = boston.data
y = boston.target
int = np.ones(shape=y.shape)[..., None]
y.shape[0]
a = np.ones([y.shape[0]], dtype=np.int)
X = np.concatenate((int, X), 1)



inv(X)

coeffs = inv(X.transpose().dot(X)).dot(X.transpose()).dot(y)
df_boston.as_matrix()



a = np.array([1,2,4])
col = np.array(["a"])

df = pd.DataFrame(a,columns=col)

df.insert(loc=0, column='A', value=np.array([4,5,6]))
df
del df['A']


