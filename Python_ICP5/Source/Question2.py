"""
Create Multiple Regression for the “wine quality” dataset.
In this data set “quality” is the target label.
Evaluate the model using RMSE and R2 score.
https://umkc.box.com/s/ohp4ys6b1gv1qa8wxh7infnzw13vjeso
**You need to delete the null values in the data set
**You need to find the top 3 most correlated features to the target label(quality)
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


# Loading the data using pandas library
wine_data = pd.read_csv('winequality-red.csv')

# Deleting the null values
nulls = pd.DataFrame(wine_data.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print("Null values:", nulls, '\n')

# Finding correlated features with the target class
numeric_features = wine_data.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print("\n Correlated Features: ", corr['quality'].sort_values(ascending=False)[1:4], '\n')

# Dropping the columns which have less correlation with the target class
data = wine_data.drop(columns=['residual sugar', 'free sulfur dioxide', 'pH'], axis=1)
print(data.columns)

# Splitting the data
x = data.drop('quality', axis=1)
y = data['quality']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=200)

# Creation of regression model and training the model
model = LinearRegression().fit(x_train, y_train)

# predicting the target
predict = model.predict(x_test)

# Evaluation of model using metrics
MSE = mean_squared_error(y_test, predict)
r2_score = r2_score(y_test, predict)
print("\nMean squared error is", MSE)
print("\nR2 score is ", r2_score)