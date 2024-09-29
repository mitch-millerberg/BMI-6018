# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 15:46:04 2024

@author: mitch

while_inner_plus.py
Write a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. This is to be done with a while loop. Note: the input will contain only integers or lists. 
As an example:
"""
#input_list = [1,2,3,4,[5,6,7,[8,9]]]

#your_py_program.py input_list

#will produce:

#[9,10]

#That is [8, 9] (the inner most list) plus 1 -> [9, 10]

def find_innermost_plus_one(input_list):
    # Start with the input list
    current_list = input_list
    
    # move into the innermost list
    while isinstance(current_list, list) and current_list:
        current_list = current_list[-1]  # Move to the last element

    # current_list is the innermost integer
    # the result by adding 1 to the innermost value
    result = [current_list + 0, current_list + 1]
    
    return result

# Example usage
input_list = [3, 48, 23, 89, [67, 45, 78, [31, 32]]]
output = find_innermost_plus_one(input_list)
print(output)  # Output will be [32, 33]`