# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:14:24 2024

@author: mitch

Question 7
Jack has been prescribed 5 medications, write a variable named "Medication",
and store in it the number of medications he has. Print the type of the variable 
''Medication". Submit your code either here as a text entry, or on your GitHub page
in a new repository and past the link here. We encourage you to use GitHub. 
Don't forget to add comments to your code.
"""

Medication = 5

#print the type of the variable Medication
print(type(Medication))

"""
Explanation:
The variable Medication is assigned the integer value 5, which represents the number 
of medications Jack has been prescribed.

The print(type(Medication)) statement outputs the type of the variable, 
which in this case will be <class 'int'>, indicating that Medication is an integer.

"""

"""
Question 8
Susan has a weight of 60 kilograms and a height of 1.58 meters. 
Write Code to Calculate and Print Susan’s Body Mass Index as float. 
Note: Body Mass Index is a person’s weight in kilograms divided by the square of height 
in meters.
Reference: https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.htmlLinks 

Submit your code either here as a text entry, or on your GitHub page in a new 
repository and past the link here. We encourage you to use GitHub. 
Don't forget to add comments to your code.

"""
# This code caclualtes Susans's Body Mass Index
# Given Susan's weight and height
weight = 60  # in kilograms
height = 1.58  # in meters

# Calculate Body Mass Index (BMI)
bmi = weight / (height ** 2)

# Print the BMI as a float
print(bmi)