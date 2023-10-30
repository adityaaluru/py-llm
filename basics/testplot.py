
import matplotlib.pyplot as plt
import numpy as np

#xpoints = np.array([1, 2, 6, 8])
#ypoints = np.array([3, 8, 1, 10])

#plt.plot(xpoints, ypoints)
#plt.plot(xpoints, ypoints, 'o')
#plt.plot(ypoints, marker = '*')
#plt.show()

### Normal distribution into 1000 durations
# x = np.random.normal(5.0, 1.0, 100000)
# plt.hist(x,1000)
# plt.show()


### Uniform distribution and histogram plot
# x = np.random.uniform(0.0, 5.0, 2000)
# plt.hist(x,5)
# plt.show()

### Scatter distribution plot
x = np.random.normal(5.0, 4.0, 1000)
y = np.random.normal(10.0, 5.0, 1000)
plt.scatter(x, y)
plt.show()