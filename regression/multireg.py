# Develop model to correlate a value based on independent variables
# In this example CO2 emission is predicted based on car's volume and weight

import pandas as pd
from sklearn import linear_model
import sklearn

df = pd.read_csv(".\data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X.values,y.values) ## THIS line is modified from the given example
print("Coefficient:",regr.coef_)

print("Score: ",regr.score(X.values,y.values))
print(regr.get_params())

predictedCO2 = regr.predict([[2300, 1300]])
print("Predicted value for Weight as 2300 and volume as 1300",predictedCO2)

predictedCO2 = regr.predict([[3300, 1300]])
print("Predicted value for Weight as 3300 and volume as 1300",predictedCO2)