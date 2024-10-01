# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:17:09 2024

@author: mitch
2.Write the a python program that, given an input list of any level of complexity/nestedness,
will return the inner most list plus 1. This is to be done with recursion. 
Note: the input will contain only integers or lists. 

"""
"""
    Recursively finds the depth of the innermost list in a nested list structure.
    
    Args:
        input_list (list): The input list which may contain integers or other lists.
        
    Returns:
        int: The depth of the innermost list plus one.
 """

def innermost_list_length_plus_one(nested_list):
    # Base case: if the input is not a list, return 1
    if not isinstance(nested_list, list):
        return 1
    
    # Recursive case: if it's a list, check each element
    max_length = 0
    for element in nested_list:
        # Recursively call the function on each element
        current_length = innermost_list_length_plus_one(element)
        max_length = max(max_length, current_length)
    
    # Return the maximum length found plus one
    return max_length + 1

# Example 
input_list = [1,11, [2,3,[[ [3]]]],3,2, [[2,3,4]],5,2]
result = innermost_list_length_plus_one(input_list)
print(f"The length of the innermost list plus one is: {result}")