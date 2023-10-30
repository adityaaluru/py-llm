import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
np.random.seed(2)

polynomialDimension = 4
print("*****Creating model with degree of '",polynomialDimension,"'")

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x
# y = np.random.normal(150, 40, 100)
# y0 = np.random.normal(0,0,100)
# x0 = np.random.normal(0,0,100)
# print(x)
# plt.scatter(x, y0)
# plt.scatter(x0, y)

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = np.poly1d(np.polyfit(train_x, train_y, polynomialDimension))
myline = np.linspace(0, 6, 100)

score1 = r2_score(train_y, mymodel(train_x))
print("Model score with training data:",score1)
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))

score2 = r2_score(test_y, mymodel(test_x))
print("Model score with test data:",score2)

print("Predicted value for input '5' is ",mymodel(5))

plt.show()