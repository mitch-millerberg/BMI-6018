# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:14:24 2024

@author: mitch
"""
"""
Question 1 (Booleans)
boolean True + boolean True - boolean False = ?

Here's how the expression evaluates step-by-step:
boolean True is 1
boolean True is 1
boolean False is 0
"""
Q1_result = True + True - False
print(Q1_result)

"""
 Question 2 (Booleans 2)

"""
logical_tracker = True

# First operation
logical_tracker = logical_tracker & logical_tracker

# Second operation
logical_tracker = logical_tracker | (logical_tracker - logical_tracker)

# Final value
print(logical_tracker)  # This will output: True

"""
Question 5 (Strings)
what is the output for the following?
string = "E. Coli"

string[2]=
"""
Q_5 = "E. Coli"
print(Q_5[2])
# the result is the " " space between the "." and the "C"
"""
Question 6 (Strings 2)
# Correct the typo
"""
string = "I Bove python"
# Correct the typo
corrected_string = string[:2] + "L" + string[3:]
print(corrected_string)

"""
 Question 9 (Operators 2)
"""
# String concatenation
str1 = "Mitchell "
str2 = "Millerberg"
result = str1 + str2
print("String concatenation:", result)  # Output: my Full name

# Integer addition
a = 5
b = 3
result = a + b
print("Integer addition:", result)  # Output: 8

"""
Question 10 (String 3)

"""
Q10_result = "7" + "3"
print(Q10_result)  # Output: "73"

Q10_result_int = int("7") + int("3")
print(Q10_result_int)  # Output: 10

"""
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