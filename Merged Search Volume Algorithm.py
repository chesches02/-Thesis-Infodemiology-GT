import pandas
import matplotlib.pyplot as plt 
import numpy as np  
import scipy

print(scipy.__version__)

mydataset = {
    'first': ["yes", "No", "Maybe"]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()