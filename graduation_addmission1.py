import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from sklearn import linear_model
import seaborn as sns

data= pd.read_csv(r"C:\Users\HP\.spyder-py3\graduation addmission\Admission_Predict_Ver1.1.csv")

data.info()

data.head()

data.describe()

data.isnull().any() #check if there a missing values or not

sns.heatmap(data.corr(), cmap="YlGnBu", annot = True) # show the most correlated variable to our target variable
plt.show()

#As we can see from the heatmap, the  CGPA is the most correlated 
#variable with the Chance of Admit. so we decided to perform simple 
#linear regression using CGPA  as our input  variable.

#Rename the columns
data.columns=['id','GRE','TOFEL','UniversityRating','SOP','LOR','CGPA','Research','p']
data

#Dropping unwanted column
data = data.drop('id',axis='columns')
data =data.drop('GRE',axis='columns')
data =data.drop('TOFEL',axis='columns')
data =data.drop('UniversityRating',axis='columns')
data =data.drop('SOP',axis='columns')
data =data.drop('LOR',axis='columns')
data =data.drop('Research',axis='columns')
data.head()

#visualize the data
plt.scatter(data['CGPA'],data['p'])
plt.xlabel('GPA')
plt.ylabel('Chance of Admit')
plt.show()

X = data.iloc[:,:-1].values  #independent variable array
y = data.iloc[:,1].values  #dependent variable vector

#split the data for trainig and testing 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=1/3,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()#modeling 
regressor.fit(X_train,y_train)#train model

print("coefficients : ",regressor.coef_) #slop
print("Intercept : ",regressor.intercept_)

y_pred = regressor.predict(X_test) #test model
y_pred

# visualizing fit 
plt.figure(figsize=(8,4))
plt.scatter(X_train, y_train, color='red') # plotting the observation line
plt.plot(X_train, regressor.predict(X_train), color='blue') 
plt.xlabel('GPA')
plt.ylabel('Chance of Admit')

#evaluation metrics for comparison
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import math
import statsmodels.api as sm
print("Mean squares (MSE): %.3f"%mean_squared_error(y_test, y_pred))
print("Root Mean Square Error: %.3f"%math.sqrt(mean_squared_error(y_test, y_pred)))
print("Mean absolute error: %.3f"%mean_absolute_error(y_test, y_pred))
X_addC = sm.add_constant(X)
result = sm.OLS(y, X_addC).fit()
print("R-Square Error: %.3f"%result.rsquared)

#checking the accurecy
accuracy = regressor.score(X_test, y_test)
print("accuracy : ", accuracy*100, "%")


