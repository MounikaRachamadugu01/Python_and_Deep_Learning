"""
Implement Naïve Bayes method using scikit-learn library
Use dataset available in https://umkc.box.com/s/ea6wn1cidukan67t02j60nmp1ljln3kd
Use train_test_split to create training and testing part
Evaluate the model on testing part using score and classification_report(y_true, y_pred)

"""

# importing libraries to python
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import pandas as pd

# reading the csv file data using pandas library
glass_data = pd.read_csv("glass.csv")

# preprocessing the data
X = glass_data.drop('Type', axis=1)
Y = glass_data['Type']

# splitting data into training data and testing data
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.2, random_state=0)

# creating and Training the classifier from sklearn library
gb = GaussianNB()
gb.fit(X_train, Y_train)

# Prediction
Y_pred = gb.predict(X_test)

# Display Scores
print("\n Gaussian Naive Bayes Accuracy Score:", metrics.accuracy_score(Y_test, Y_pred))
print("\n Classification Report: \n", metrics.classification_report(Y_test, Y_pred))

