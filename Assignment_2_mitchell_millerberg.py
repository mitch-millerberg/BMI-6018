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
print("Modified List =",list_1)
"""
 .c Coerce all elements in the list to floats using list comprehension
"""
#convert list_1 using map function
float_list_1 = list(map(float,list_1))
print("float_list_1 = ",float_list_1) 

"""
 .d Coerce the list to a set
"""
set_list=set(list_1)
print("list_1 = ",list_1)
print("converted into a set =",set_list)

""" 
 .e Using a method, append int 10 to the set
"""
# Appending the integer 10 to the list
list_1.append(10)
print("updated list_1", list_1)
"""
 .f Using a method, pop an item from the set
"""
popped_item = list_1.pop()
print("popped item",popped_item) #what item was popped out of the list?
print("updated list:", list_1)
"""
 .g Using a length counting function, count the number of items in the set
"""
count = len(list_1)
print("The number of item in list_1 is ",count)
"""

 .h Check if the number of items in the set is the same as the 
    number of items in the list
"""
# Check if the lengths are the same
if len(list_1) == len(set_list):
    print("The number of items in the list and the set are the same.")
else:
    print("The number of items in the list and the set are different.")
"""
 
 .i Coerce the set to a list and use the "+" operator combine the list to the list from 1.a
"""
list_2 = list(set_list) #coerce the set into list format

combined_list = list_1 + list_2 # combined lists with "+"

print("this is the combined list ", combined_list)

"""
 .j Coerce 1.i to a set
"""
combined_set_list=set(combined_list)
print("combined set list",combined_set_list)

"""

 .k Count the number of elements in the 1.j
"""
count = len(combined_set_list)
print("count of combined set list",count)

"""
Problem 2: Dictionary woes

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
2.a Combine the three sample dictionaries (given above) into a nested dictionary 
(nested in programming means joined),
 named two_a, ensure the key names are the same as the dictionary names.
"""
two_a = {
    "two_patient_dictionary_kinoko": {
        "name": "Kinoko",
        "year": 2021
    },
    "two_patient_dictionary_dango": {
        "name": "Dango",
        "year": 2019
    },
    "two_patient_dictionary_mochi": {
        "name": "Mochi",
        "year": 2020
    }
}
""" 
 
 .b Using keys, retrieve the Dango's name from 2.a
"""
# Accessing Dango's name
dango_name = two_a["two_patient_dictionary_dango"]["name"]
print(dango_name)

"""
 .c Using keys, update the value of Mochi's year to 2018. This should not be a variable
    and should simply update 2.a.
"""
two_a["two_patient_dictionary_mochi"]["year"] = 2018
"""
 .d Manually create a dictionary that has a single level and contains each patient
    as the key and the year as the value. Set Mochi's year to 2019.'
"""
patient_years = {
    "Kinoko": 2021,
    "Dango": 2019,
    "Mochi": 2019  # Updated Mochi's year to 2019
}
"""
 .e Coerce the keys of 2.d into a list
"""
# Coerce the keys into a list
patient_keys = list(patient_years.keys())
# List of patient names (keys)
patient_keys = ["Kinoko", "Dango", "Mochi"]

"""
 .f Coerce the values of 2.d into a list
"""
# Coerce the values into a list
years_list = list(patient_years.values())

# Output the results
print("Patient Year Dictionary:", patient_years)
print("Years List:", years_list)

"""
 .g Use the zip function to combine 2.e and 2.f into a dictionary again
"""
# Use zip to combine keys and years into a dictionary
combined_dict = dict(zip(patient_keys, years_list))

# Print the resulting dictionary
print("combined dictionary", combined_dict)
"""
Problem 3: Set combinations
"""
three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}
"""
Given the predefined sets above and using set methods
3.a Is set E a subset of set A
"""
#Yes, set E is a subset of set A ( E ⊆ A E⊆A).
"""
 .b Is set E a strict subset of set A
"""
 #Yes, set E is a strict subset of set A ( E ⊂ A E⊂A).

# I'm switching to "#" commentating to mark out the questions because I think it's easier and looks 
# cleaner than usings """. If I am using spyder instead of jupyter to do my homework will that be a problem?
#I am able to uploading my code to my github repo. I just want to know if not using Jupyter notebooks  will be a 
# problem later on in this class?k

#.c Create a set that is the intersection of set A and set B
# Intersection using the intersection() method
intersection_set = three_setA.intersection(three_setB)
print("intersection_set", intersection_set)

#.d Create a set that is the union of sets C, D and E
# Using the union() method
union_set = three_setC.union(three_setD, three_setE)
print("Union using union(X) method:", union_set)

#.e add 9 to the set
union_set.add(9)

# Print the result
print("union_set_with_9", union_set)
#.f Using == compare this set to the list in one_a. aka "list_1"

list_1_set = set(list_1)
is_equal = union_set == list_1_set

print(is_equal) 

"""
.g Explain why they are not the same. What would you need to change if you
    #wanted this to be True?
    
list_1 = [0,1,2,3,4,5,6,7,8,9]
union_set{1, 2, 3, 4, 5, 6, 7, 8, 9}

The data types between the two are different.
list_1 is a list, while union_set is a set. In Python, lists and sets are fundamentally different types, and they cannot be equal to each other. Another reason why they are different is because the content is different.
The contents of list_1 include the integer 0, which is not present in union_set. 
Making Them Equal
To make the comparison return True, I would need to ensure that both data structures contain the same elements and are of the same type.
convert list_1 to a set and remove 0 from list_1.   

"""
 
"""
Problem 4: Changing variable types

For each step you will modify a variable, then append the type of the variable
to a list. Do not recreate the list variable, it should be a running list of 
types.
"""
"""
#4.a Create a variable of type int with the value of 8
"""
var_a = 8  # Integer
"""

# .b Create an empty list 
"""
type_list = []  # [] make an Empty list

"""
# .c Using type(), add the type of 4.a to this list
"""
type_list.append(type(var_a))  # Append type of var_a (int)
"""
"""
# .d Add 0.39 to 4.c
"""
"""
var_d = 0.39  # Float

"""
# .e append the type of 0.39 to the list
"""
type_list.append(type(var_d))  # Append type of var_d (float)
"""

# .f exponentiate to the -10, ie: 4.d^-10,(hint: there might be an artihmetic operator to do so) round it to no 
# decimal places, and append to list.
"""
result_f = round(var_d ** -10)  # Exponentiate to -10 and round
#  

type_list.append(type(result_f))  # Append type of result_f (int)

"""
#In Python, the operation ** is the exponentiation operator. 
#It raises the number on the left to the power of the number on the right.
# .g append the type to the list
"""
print(type_list)
 
 
#Problem 5: More variable type changes
#Continue from where you left off in Problem 4.

# 5.a Manually create a dictionary where the values are items in the "type_list" 
# and the keys should be their index in the list. Print the dictionary.
type_dict ={index: str(type_item) for index, type_item in enumerate(type_list)}
print("type dictionary: ",type_dict)

#  .b Add 300 and coerce it into a string
var_b = str(300)
#  .c append the type to the list
type_list.append(type(var_b))

#  .d slice the string up to the 2nd element
sliced_string = var_b[:2]
print("sliced",sliced_string)
#  .e append the type to the list
type_list.append(type((sliced_string)))
print("sliced",sliced_string)            
#  .f use list comprehension to convert this into a new list of integers
int_list = [int(char) for char in sliced_string] 

#  .g append the type to the list
type_list.append(type(int_list))
#  .h append the type of three_setA to the list
three_setA = {1, 2, 3}  # Example set
type_list.append(type(three_setA))  # Append type of three_setA (set)
print(type_list) 