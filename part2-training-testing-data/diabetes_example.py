import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, linear_model
from sklearn import mean_squared_error, r2square

#load the dataset

x, y = datasets.load_diabetes(return_x_y=True)
x = x[:,np.newaxis, 2] #makes it seperate
# print(x)
# print(y)

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)


model = linear_model.LinearRegression().fit(xtrain, ytrain)

