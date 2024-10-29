# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:01:04 2024

@author: mitch
T:quiz Libraries and Numpy

quesitons
4. In 100 words or fewer, explain what a boolean mask is and how it is used in numpy/pandas.  Provide code as appropriate.
6. Given the following np.array(), what will be the result of the slicing operation listed below?
7. Let us create an np vector as:
x = np.array ([[1,2,3,4,5,6],[7,8,9,10,11,12])

And then we do following x[1,::2].

What is that :: operator doing?

What would it output?
"""
import numpy as np
#import requests
import pandas as pd

#6 Given the following np.array(), what will be the result of the slicing operation listed below?
x = np.array([[1,2,3],[4,5,6]])
x[1,::1]
print(x[1, ::1])

#7 Let us create an np vector as:

y = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])

# Slicing the second row (index 1) to get every second element starting from index 0
result = y[1, ::2]

#What is that :: operator doing?
#It subsets for the 1th x dim, then produces EVERY OTHER value in that vectors elements.

# Printing the result
print(result)


#Question 4 
### Usage in NumPy
arr = np.array([1, 2, 3, 4])
mask = arr > 2  # Creates a boolean mask
maskresult = arr[mask]  # Selects elements where mask is True
print(maskresult)  

### Usage in Pandas
mask_df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})
print(mask_df)#priview data table
mask = mask_df['B'] > 30
filtered_dfd = mask_df[mask]  # Selects rows where mask is True
print(filtered_dfd)

