# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:03:32 2024

@author: mitch
In this assignment you will experiment on your own. Using a health dataset of your choice.
Write code to demonstrate the following Pandas functions:

Melt
Pivot
Aggregation
Iteration
Groupby

The data set that I choose to use is Heart Disease from the UC Irvine repo
https://archive.ics.uci.edu/dataset/45/heart+disease

Dataset Information
Additional Information

This database contains 76 attributes, but all published experiments refer to using a subset of 14 of them.  In particular, the Cleveland database is the only one that has been used by ML researchers to date.  The "goal" field refers to the presence of heart disease in the patient.  It is integer valued from 0 (no presence) to 4. Experiments with the Cleveland database have concentrated on simply attempting to distinguish presence (values 1,2,3,4) from absence (value 0).  
   
The names and social security numbers of the patients were recently removed from the database, replaced with dummy values.

One file has been "processed", that one containing the Cleveland database.  All four unprocessed files also exist in this directory.

To see Test Costs (donated by Peter Turney), please see the folder "Costs" 

Cite:
Janosi, A., Steinbrunn, W., Pfisterer, M., & Detrano, R. (1989). Heart Disease [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C52P4X.


"""
# Data Fetching: Importing necessary libraries and fetching the heart disease dataset from the UCI Machine Learning Repository.
#Using the following dataset health dataset
import pandas as pd
from ucimlrepo import fetch_ucirepo 

  
# fetch dataset 
heart_disease = fetch_ucirepo(id=45) 
  
# data (as pandas dataframes) 
X = heart_disease.data.features 
y = heart_disease.data.targets 
  
# metadata 
print(heart_disease.metadata) 
# variable information 
print(heart_disease.variables) 
"""
Write code to demonstrate the following Pandas functions:

**Melt**: The `pd.melt()` function reshapes the features DataFrame from wide to long format, creating a new DataFrame with each feature as a row.

**Pivot**: The `pivot()` function is used to revert the melted DataFrame back to its original wide format, using the 'index' as identifiers.

**Aggregation**: The code performs an aggregation to calculate the mean value for each feature using `groupby()` and `agg()`.

**Iteration**: It iterates through the rows of the melted DataFrame, printing out each feature's index and value.

**Groupby**: Groups by feature name and counts occurrences, producing a summary of how many times each feature appears in the dataset.

"""

# Melt
# Melting the features DataFrame to long format
melted_df = pd.melt(X.reset_index(), id_vars=['index'], var_name='Feature', value_name='Value')
print("\nMelted DataFrame:")
print(melted_df)


# Pivot
# Pivoting the melted DataFrame back to wide format
pivoted_df = melted_df.pivot(index='index', columns='Feature', values='Value').reset_index()
print("\nPivoted DataFrame:")
print(pivoted_df)

# Aggregation
# Example aggregation to find average value of a feature by index
agg_df = melted_df.groupby('Feature').agg({'Value': 'mean'}).reset_index()
print("\nAggregated DataFrame (Average Value by Feature):")
print(agg_df)

# Iteration
# Iterating over rows in the melted DataFrame
print("\nIterating over rows:")
for index, row in melted_df.iterrows():
    print(f"Index {row['index']} has Feature {row['Feature']} with Value {row['Value']}.")
    
# Groupby
# Grouping by feature and counting number of occurrences of each feature value
grouped_df = melted_df.groupby('Feature').size().reset_index(name='Count')
print("\nGrouped DataFrame (Count of Each Feature):")
print(grouped_df)
  
