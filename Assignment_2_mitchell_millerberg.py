# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 23:21:59 2024

@author: mitch

Assignment: Complex Data Types

"""
"""BMI 6018 Fall 2022 

Instructions: For this assignment, please return all answers as variables in your
.py file. You will quickly note that you will need to find answers outside the
class lectures. This is not an accident! You will need to become professionally
comfortable with looking things up via the python docs and google. 

Ensure that all variables are labelled according to the example. IE the answer
to problem 1 part c should be labelled one_c. While all questions are answerable
with a single line of code, you are free to use helper variables so long as they
are helpfully/informatively named. 

I should be able to open your .py file and run it without errors. I will **not** be 
debugging your code for you. If your file does not run, it will **not** be graded. 
If you are unsure if your file will run, open up a chpc terminal and test it there.

For this assignment, please only use base python files types. That is: there 
should be no import calls in your file save my use of sys at the end.

Example Problem

0.a Create a list of strings
0.b Using a str method, capitalize one of the elements in the list using a slice
0.c Coerce one character of the list to display as a hex

zero_a = ['first','second','third','fourth','fifth']
zero_b = zero_a[1].upper()
zero_c = hex(ord(zero_a[1][1]))

#Problem 1: Lists, Sets and Coersion

1.a Create a list of integers no fewer than 10 items from 0 to 9.
 .b Add 3 to the 5th indexed element
 .c Coerce all elements in the list to floats using list comprehension
 .d Coerce the list to a set
 .e Using a method, append int 10 to the set
 .f Using a method, pop an item from the set
 .g Using a length counting function, count the number of items in the set
 .h Check if the number of items in the set is the same as the 
    number of items in the list
 .i Coerce the set to a list and use the "+" operator combine the list to the list from 1.a
 .j Coerce 1.i to a set
 .k Count the number of elements in the 1.j



Problem 2: Dictionary woes

2.a Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), named 
    two_a, ensure the key names are the same as the dictionary names.
 .b Using keys, retrieve the Dango's name from 2.a
 .c Using keys, update the value of Mochi's year to 2018. This should not be a variable
    and should simply update 2.a.
 .d Manually create a dictionary that has a single level and contains each patient
    as the key and the year as the value. Set Mochi's year to 2019.'
 .e Coerce the keys of 2.d into a list
 .f Coerce the values of 2.d into a list
 .g Use the zip function to combine 2.e and 2.f into a dictionary again


two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}



Problem 3: Set combinations

Given the predefined sets below and using set methods
3.a Is set E a subset of set A
 .b Is set E a strict subset of set A
 .c Create a set that is the intersection of set A and set B
 .d Create a set that is the union of sets C, D and E
 .e add 9 to the set
 .f Using == compare this set to the list in one_a
 .g Explain why they are not the same. What would you need to change if you
    wanted this to be True?
 

three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}



Problem 4: Changing variable types

For each step you will modify a variable, then append the type of the variable
to a list. Do not recreate the list variable, it should be a running list of 
types.

4.a Create a variable of type int with the value of 8
 .b Create an empty list 
 .c Using type(), add the type of 4.a to this list
 .d Add 0.39 to 4.c
 .e append the type of 0.39 to the list
 .f exponentiate to the -10, ie: 4.d^-10,(hint: there might be an artihmetic operator to do so) round it to no 
    decimal places, and append to list.
 .g append the type to the list
 
 
Problem 5: More variable type changes

Continue from where you left off in Problem 4.

5.a Manually create a dictionary where the values are items in the list from where we left in 
    problem 4, and the keys should be their index in the list. Print the dictionary.
 .b Add 300 and coerce it into a string
 .c append the type to the list
 .d slice the string up to the 2nd element
 .e append the type to the list
 .f use list comprehension to convert this into a new list of integers
 .g append the type to the list
 .h append the type of three_setA to the list
"""

#Start your assignment here

"""
#Problem 1: Lists, Sets and Coersion

1.a Create a list of integers no fewer than 10 items from 0 to 9.
"""
list_1 = [0,1,2,3,4,5,6,7,8,9]
"""
 .b Add 3 to the 5th indexed element
 """
list_1[5]+=3
print("Modified List:",list_1)
"""
 .c Coerce all elements in the list to floats using list comprehension
"""

"""
 .d Coerce the list to a set
 .e Using a method, append int 10 to the set
 .f Using a method, pop an item from the set
 .g Using a length counting function, count the number of items in the set
 .h Check if the number of items in the set is the same as the 
    number of items in the list
 .i Coerce the set to a list and use the "+" operator combine the list to the list from 1.a
 .j Coerce 1.i to a set
 .k Count the number of elements in the 1.j
 """
