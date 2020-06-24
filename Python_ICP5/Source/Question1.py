"""
Delete all the outlier data for the Garage Area field (for the same data set in the use case from Python Lesson5: House Prices).
* for this task you need to plot Gaurage Area field and Sale Price in scatter plot, then check which numbers are anomalies.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Loading the data using pandas library
train_data = pd.read_csv('train.csv')

data = pd.read_csv('train.csv', sep=',', usecols=(62, 80))
x = data['GarageArea']
y = data['SalePrice']

# Data size and graph before deleting out liners
print('Data size before deleting outliers', data.shape)
plt.scatter(x, y, alpha=.75, color='b')
plt.title("Scatter Plot before deleting outliers")
plt.xlabel("GarageArea")
plt.ylabel("SalesPrice")
plt.show()

# Finding the outliers using Z-score
# Data points with Z-score greater than three are considered as outliers
data = data[data['GarageArea'] > 200]
z = np.abs(stats.zscore(data))
modified_data = data[(z < 3).all(axis=1)]
x = modified_data['GarageArea']
y = modified_data['SalePrice']

# Data size and graph after deleting out liners
print('Data size after deleting outliers : ', modified_data.shape)
plt.scatter(x, y, alpha=.75, color='g')
plt.title("Scatter Plot after deleting outliers")
plt.xlabel("GarageArea")
plt.ylabel("SalesPrice")
plt.show()