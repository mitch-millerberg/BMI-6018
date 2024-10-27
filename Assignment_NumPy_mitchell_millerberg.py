# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:18:43 2024

@author: mitch
1. Import numpy as np and print the version number.
2. Create a 1D array of numbers from 0 to 9.
3. Import a dataset with numbers and texts keeping the text intact in python numpy. 
Use the iris dataset available from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
4. Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset. 
Use the iris dataset available from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.dataLinks 
to an as a .csv file. Use this file for analisis 
5. From the array a, replace all values greater than 30 to 30 and less than 10 to 10.

 

"""
import numpy as np
#import requests
import pandas as pd

print("the version of numpy is ",np.__version__)


array = np.arange(10)
print(array)


# moved the import "requests" to import list for cleaner look
# URL of the Iris dataset
Iris_data = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Import the dataset while keeping text intact
# Define column names for the dataset
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
Iris_data = pd.read_csv(Iris_data, header=None, names=column_names)
print(Iris_data)

# Find the position of the first occurrence of a value greater than 1.0 in petal width (4th column) 
#I added headers to my data table so this number will be one more than if I hadnt added the headers. 
first_occurrence = np.where(Iris_data['petal_width'] > 1.0)[0][0]
print("The position of the first occurrence of a value greater than 1.0 in petal width is:", first_occurrence)

# From the array, replace all values greater than 30 to 30 and less than 10 to 10
#x = np.array([5, 15, 25, 35, 45])

np.random.seed(100)
a = np.random.uniform(1,50, 20)
a[(a > 30)] = 30
a[(a < 10)] = 10
print(a)
print("Modified array:", a)














