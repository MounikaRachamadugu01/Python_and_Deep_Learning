"""
find the correlation between ‘survived’(target column) and ‘sex’ column for the Titanic use case in class.
Do you think we should keep this feature?

"""

# importing pandas library for data analysis in python
import pandas as pd
# read the data using pandas and store in a variable
train_data = pd.read_csv('train.csv')
# preproccesing the data
train_data['Sex'] = train_data['Sex'].replace( {'female': 1, 'male': 0} )
# finding the correlation
Correlation = train_data['Survived'].corr(train_data['Sex'])
print("\n Correlation score between Survived and Sex Fields in the csv file:", Correlation)