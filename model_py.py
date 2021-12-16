# importing files and dataset
# import pdb
# pdb.set_trace()
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_excel('data.xlsx')

# pdb.set_trace()

X = data.drop(['Overall','bins'], axis=1)
y = data['Overall'].values
data_column_names = X.columns

# # Scaling the input features
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# X_scaled = pd.DataFrame(X_scaled, columns = data_column_names)

# Divide the data into training and testing samples

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

# Using Linear Regression




def regressionAnalysis(test):
    regressor = LinearRegression()
    regressor.fit(X_train,y_train)
    y_pred = regressor.predict((test))
    return y_pred


def grade(y_pred):
    if (y_pred >=70 and y_pred <= 100):
        grade = 'A'
    elif (y_pred >=60 and y_pred <= 69):
        grade = 'B'
    elif (y_pred >=50 and y_pred <= 59):
        grade = 'C'
    elif (y_pred >=49 and y_pred <= 49):
        grade = 'D'
    else:
        grade = 'E'
    
    return grade
