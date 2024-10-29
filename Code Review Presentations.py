# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 22:48:27 2024
code review 
Oct 28th 
	Assignment: Complex Data Types, Question 1e - 1h	 Mitchell Millerberg
    
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

@author: mitch

#Start 


"""
#Problem 1: Lists, Sets and Coersion
"""

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