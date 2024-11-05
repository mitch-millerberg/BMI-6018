# -*- coding: utf-8 -*-
"""
Created on 21:03:24 2024

@author: mitch
Pandas Assignment 2

Question 1 (15 Points)
Compute the euclidean distance between series (points) p and q, without using a packaged formula.
Input
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

Question 2 (15 Points)
Change the order of columns of a dataframe. Interchange columns 'a' and 'c'.
Input
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

Question 3 (15 Points)
Change the order of columns of a dataframe. Create a generic function to interchange two columns, without
hardcoding column names.
Input
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

Question 4 (15 Points)
Format or suppress scientific notations in a pandas dataframe. Suppress scientific notations like ‘e-03’ in df and
print upto 4 numbers after decimal.
Input
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
df
#> random
#> 0 3.474280e-03
#> 1 3.951517e-05
#> 2 7.469702e-02
#> 3 5.541282e-28
Desired Output
#> random
#> 0 0.0035
#> 1 0.0000
#> 2 0.0747
#> 3 0.0000

Question 5 (15 Points)
Create a new column that contains the row number of nearest column by euclidean distance. Create a new column
such that, each row contains the row number of nearest row-record by euclidean distance.
Input
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1),
columns=list('pqrs'), index=list('abcdefghij'))
df
# p q r s
# a 57 77 13 62
# b 68 5 92 24
# c 74 40 18 37
# d 80 17 39 60
# e 93 48 85 33
# f 69 55 8 11
# g 39 23 88 53
# h 63 28 25 61
# i 18 4 73 7
# j 79 12 45 34
Desired Output
df
# p q r s nearest_row dist
# a 57 77 13 62 i 116.0
# b 68 5 92 24 a 114.0
# c 74 40 18 37 i 91.0
# d 80 17 39 60 i 89.0
# e 93 48 85 33 i 92.0
# f 69 55 8 11 g 100.0
# g 39 23 88 53 f 100.0
# h 63 28 25 61 i 88.0
# i 18 4 73 7 a 116.0
# j 79 12 45 34 a 81.0

Question 6 (15 Points)
Correlation is a statistical technique that shows how two variables are related. Pandas dataframe.corr() method is
used for creating the correlation matrix. It is used to find the pairwise correlation of all columns in the dataframe.
Any na values are automatically excluded. For any non-numeric data type columns in the dataframe it is ignored.
Input
data = {'A': [45, 37, 0, 42, 50],
'B': [38, 31, 1, 26, 90],
'C': [10, 15, -10, 17, 100],
'D': [60, 99, 15, 23, 56],
'E': [76, 98, -0.03, 78, 90]
}

"""
import pandas as pd
import math
import numpy as np

#Question 1
# Define the Series
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# Compute the euclidean distance between series (points) p and q, without using a packaged formula.  
#Step-by-step computation of Euclidean distance
def euclidean_distance(series1, series2):
    # Ensure both series have the same length
    if len(series1) != len(series2):
        raise ValueError("Both series must be of the same length.")
    
    # Calculate the squared differences
    squared_differences = [(series1[i] - series2[i]) ** 2 for i in range(len(series1))]
    
    # Sum the squared differences
    sum_of_squares = sum(squared_differences)
    
    # Take the square root of the sum to get the Euclidean distance
    distance = math.sqrt(sum_of_squares)
    
    return distance


# Calculate and print the Euclidean distance
distance = euclidean_distance(p, q)
print("Euclidean Distance:", distance)

#Question 2
# Create the DataFrame
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Interchange columns 'a' and 'c'
df[['a', 'c']] = df[['c', 'a']]

# Display the modified DataFrame
print("\nDataFrame after interchanging columns 'a' and 'c':")
print(df)

#Question 3
# Create a DataFrame with values from 0 to 19 reshaped into 4 rows and 5 columns
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

# Set display options to suppress scientific notation and format floats
pd.options.display.float_format = '{:.4f}'.format

# Print the DataFrame
print(df)

#other examplse that i found while doing this problem and want to keep them in the code.
# sample DataFrame with scientific notation
data = {
    'A': [1.234567e-03, 2.345678e-04, 3.456789e-05],
    'B': [4.567890e+02, 5.678901e+03, 6.789012e+04]
}
df = pd.DataFrame(data)

# Method 1: Using round() to format numbers
df_rounded = df.round(4)

# Method 2: Using apply() to format as strings with specified decimal places
df_formatted = df.apply(lambda x: x.map('{:.4f}'.format))

# Method 3: Set global option to suppress scientific notation
pd.set_option('display.float_format', lambda x: '%.4f' % x)

# Print the DataFrame with rounded values
print("DataFrame with rounded values:")
print(df_rounded)

# Print the DataFrame with formatted strings
print("\nDataFrame with formatted strings:")
print(df_formatted)

# Resetting the display option to default if needed
pd.reset_option('display.float_format')

#Question 4
# set the DataFrame with values from 0 to 19, reshaped into 4 rows and 5 columns
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

# Set the display option to suppress scientific notation and format floats
pd.options.display.float_format = '{:.4f}'.format

# Print the DataFrame
print(df)

#Question5 
#A DataFrame f is created with random integers between 1 and 100, reshaped into 10 rows and 4 columns.

from scipy.spatial import distance

# Create the initial DataFrame with random integers
f = pd.DataFrame(np.random.randint(1, 100, 40).reshape(10, -1),
                  columns=list('pqrs'), index=list('abcdefghij'))

# Function to find the nearest row based on Euclidean distance
def find_nearest_row(df):
    nearest_rows = []
    distances = []
    
    for i in range(len(df)):
        # Calculate the Euclidean distances from the current row to all other rows
        dists = distance.cdist([df.iloc[i]], df, 'euclidean')[0]
        # Get the index of the nearest row (excluding itself)
        nearest_index = np.argmin(np.where(np.arange(len(df)) == i, np.inf, dists))
        # Append the nearest row's index and distance
        nearest_rows.append(df.index[nearest_index])
        distances.append(dists[nearest_index])
    
    return nearest_rows, distances

# Apply the function to find nearest rows and distances
f['nearest_row'], f['dist'] = find_nearest_row(f)

# Display the updated DataFrame
print(f)


#Question6
# Input data
data2 = {
    'A': [45, 37, 0, 42, 50],
    'B': [38, 31, 1, 26, 90],
    'C': [10, 15, -10, 17, 100],
    'D': [60, 99, 15, 23, 56],
    'E': [76, 98, -0.03, 78, 90]
}

# Create DataFrame
df = pd.DataFrame(data2)

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)
