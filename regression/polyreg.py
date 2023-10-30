import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from sklearn.metrics import r2_score

# Show input data
## X-axis
# hourOfDay = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# ## Y-axis
# speedAtToll = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# plt.scatter(hourOfDay, speedAtToll)

# Example of a bad fit data

hourOfDay = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
speedAtToll = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
plt.scatter(hourOfDay, speedAtToll)

# Generate and show the model prediction for some range
## Create a 3 dimensional polynomial to fit the data. Try changing this to 5.
mymodel = np.poly1d(np.polyfit(hourOfDay, speedAtToll, 3))
myline = np.linspace(1, 22, 100) # This function creates 100 points for the range 1-22 ,to be used a x-axis points to plot the model
plt.plot(myline, mymodel(myline))

# Coefficient of determination
r = r2_score(speedAtToll, mymodel(hourOfDay))
print("Coefficient of determination:",r)
if(r>0.90):
    print("GO AHEAD with prediction!")
else:
    print("NOT READY for prediction!")

# Predict the value

predictedSpeedAtToll = mymodel(17)
print("Predicted car speed at toll at 17:00 -",predictedSpeedAtToll)

# Show plots
plt.show()