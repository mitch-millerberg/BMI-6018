# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:18:29 2024

@author: mitch

Write a python program that, given an input list, will filter the input above a user defined threshold. 
This is to be done with a standard function.
That is, given a list [1,2,3,4,5,6,7,8,9], and an argument (6), it should return [1,2,3,4,5,6]

  Filters the input list to include only elements less than or equal to the given threshold.

  Parameters:
  input_list (list): The list of numbers to be filtered.
  threshold (int or float): The threshold value.

  Returns:
  list: A new list containing elements from input_list that are less than or equal to threshold.
"""

def filter_above_threshold(input_list, threshold):
    return [x for x in input_list if x <= threshold]

# Example 
if __name__ == "__main__":
    
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Define the input list and threshold
    threshold = 6

    # Call the function and print the result
    filtered_list = filter_above_threshold(input_list, threshold)
    print("Filtered List:", filtered_list)
    