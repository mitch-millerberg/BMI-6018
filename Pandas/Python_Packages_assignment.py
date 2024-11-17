# -*- coding: utf-8 -*-
"""
@author: mitch
Created on Thu Nov 14 20:47:28 2024
In this assignment you will experiment on your own. You will demonstrate the use a python library of your choice 
by reading its documentation.

Seaborn

You submission include the following:
1) An introduction to the library and its sources as comments. (10 Points)
    
For this assignment, I chose to work with the Seaborn Python library package.
Seaborn is a data visualization library that builds upon the foundation of Matplotlib, another popular Python library.
I explore the potential of various data visualization techniques, including scatter plots, line plots, bar plots, and heat maps.
   
 Scatter Plots: for visualizing the relationship between two variables.
    Line Plots: for illustrating trends over time.
    Bar Plots: for comparing quantities across different categories.
    Heatmaps: for representing matrix-like data and correlations.
    
2)Advantages, limitations of using the library also provided as comments (10 Points)
Advantages:
    The library supports a wide range of plot types.
    Seaborn integrates with Pandas data structures, easier workflow to visualize data directly from DataFrames.
    Seaborn's default themes and color palettes are visually appealing graphics.
    Seaborn's syntax is concise and expressive, allowing users to quickly create custom plots. 

limitations:
    Seaborn is not as customizable as Matplotlib
    Matplotlib allows for fine-tuning every aspect of a plot, which can be essential for creating publication-quality figures or adhering to specific style guidelines.
    When dealing with very large datasets, Seaborn can experience performance issues. 
    Seaborn's automation can slow down and use lots of memory, especially for many or complex plots.
  
    
3)Code to demonstrate calling the library, and use an example dataset to run the library. (30 Points) 
    

    
    now write a py. segment of code that use the library Seaborn to visulize the dataset diabetes_130_us_hospitals_for_years_1999_2008 
    
    Here are some datasets you can use if you don’t have one:
https://archive.ics.uci.edu/ml/datasets/Breast+CancerLinks to an external site.
https://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospitals+for+years+1999-2008Links to an external site.
https://archive.ics.uci.edu/ml/datasets/ArrhythmiaLinks to an external site.

"""
#import data 
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
diabetes_130_us_hospitals_for_years_1999_2008 = fetch_ucirepo(id=296) 
  
# data (as pandas dataframes) 
X = diabetes_130_us_hospitals_for_years_1999_2008.data.features 
y = diabetes_130_us_hospitals_for_years_1999_2008.data.targets 
  
# metadata 
print(diabetes_130_us_hospitals_for_years_1999_2008.metadata) 
  
# variable information 
print(diabetes_130_us_hospitals_for_years_1999_2008.variables) 

#only the column headers
print(X.head(0))

# seaborn library for data visulation 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from ucimlrepo import fetch_ucirepo

# Combine features and targets into a single dataframe
df = pd.concat([X, y], axis=1)

# Set the style for seaborn plots
sns.set_style("whitegrid")
# Why I used "whitegrid" as an argument passed to the set_style() function. 
# It specifies a particular style for the plots.
# It sets the background color of the plot to white.
# It adds light grey gridlines to the plot.

# Now lets explore diffrent types of plots that Seaborn can do.... 

# Correlation heatmap for numerical variables
plt.figure(figsize=(12, 10))
numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
sns.heatmap(df[numerical_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f') #The correlation matrix shows the pairwise correlation coefficients between the variables, indicating how closely related they are.
plt.title('Correlation Heatmap of Numerical Variables')
plt.tight_layout()
plt.show()

# Pairplot for key variables
key_vars = ['time_in_hospital', 'num_lab_procedures', 'num_medications', 'number_diagnoses', 'readmitted']
sns.pairplot(df[key_vars], hue='readmitted', palette='viridis') #This line uses Seaborn's pairplot function to create a grid of scatter plots for each pair of the specified variables in key_vars.
plt.suptitle('Pairplot of Key Variables', y=1.02)
plt.show()

# Box plot of 'time_in_hospital' by 'readmitted'
plt.figure3(figsize=(10, 6))
sns.boxplot(x='readmitted', y='time_in_hospital', data=df)
plt.title('Time in Hospital by Readmission Status')
plt.show()
# creates a pairplot to visually explore relationships between several key variables related to hospital data, while also differentiating patients based on whether they were readmitted. 
# This type of visualization is particularly useful in exploratory data analysis (EDA) as it provides insights into potential correlations and distributions among multiple variables simultaneously. Problem is that is take awhile to load.

# Scatter plot with regression line for 'num_lab_procedures' vs 'num_medications'
plt.figure(figsize=(10, 6))
sns.regplot(x='num_lab_procedures', y='num_medications', data=df, scatter_kws={'alpha':0.3}) # This argument customizes the appearance of the scatter points. Here, alpha controls the transparency of the points; an alpha value of 0.3 makes them semi-transparent, which can help when there are many overlapping points.
plt.title('Relationship between Number of Lab Procedures and Medications')
plt.show()
# This plot generates a scatter plot with a regression line illustrating how the number of lab procedures correlates with the number of medications prescribed. 

# Violin plot of 'num_medications' by 'diabetesMed'
plt.figure(figsize=(10, 6))
sns.violinplot(x='diabetesMed', y='num_medications', data=df)
plt.title('Number of Medications by Diabetes Medication Status') #This line sets the title of the plot to "Number of Medications by Diabetes Medication Status". 
plt.show()
# This plot creates a violin plot to compare the distribution of medication counts across different diabetes medication statuses, while also ensuring that the plot is displayed at an optimal size for analysis.

# Bar plot of average 'number_diagnoses' by 'age' group
plt.figure(figsize=(12, 6))
df.groupby('age')['number_diagnoses'].mean().plot(kind='bar') # This part groups the DataFrame df by the 'age' column. It means that all rows with the same age will be considered together.
plt.title('Average Number of Diagnoses by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Number of Diagnoses')
plt.xticks(rotation=45)
plt.show()
# This Plot is a bar chart that visualizes the average number of diagnoses across different age groups in a dataset. 

# Create a count plot for the 'race' column
plt.subplot(2, 2, 2)
sns.countplot(x='race', data=df)
plt.title('Distribution of Race')
plt.xticks(rotation=45)

# Create a box plot for 'time_in_hospital' by 'gender'
plt.subplot(2, 2, 3)
sns.boxplot(x='gender', y='time_in_hospital', data=df)
plt.title('Time in Hospital by Gender')

# Create a histogram for 'num_lab_procedures'
plt.subplot(2, 2, 4)
sns.histplot(df['num_lab_procedures'], kde=True) # This function is part of Seaborn, a statistical data visualization library built on top of Matplotlib. It creates a histogram of the specified data.
plt.title('Distribution of Number of Lab Procedures')
# This code creates a subplot in a 2x2 grid and generates a histogram for the 'num_lab_procedures' column from a DataFrame called df
