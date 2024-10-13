
"""

#%% the humble print statement

1.a
Using the print() function only, get the wrong_add_function to print out where
it is making a mistake, given the expected output for ex, "we are making an error 
in the loop", which you would put near the loop. 
Structure the print() statement to show what the expected output ought to be
via f-strings: ie "The correct answer is supposed to be: [...]".
"""
def wrong_add_function(a, b):
    result = 0
    for i in range(a):
        result += i  # Mistake: should be result += b
        print(f"We are making an error in the loop. The correct answer is supposed to be: {a + b}")
    return result

# Example Print statement
print(wrong_add_function(2, 5))  # This will show an error message for wrong addition

"""
1.b
Then, changing as little as possible, modify the function, using the same 
general structure to output the correct answer. Call this new function 
correct_add_function() 
"""
def correct_add_function(a, b):
    result = a + b  # Correctly adds a and b
    print(f"The correct answer is: {result}")
    return result

# Example Print statement
print(correct_add_function(3, 5))  # This shows the correct addition result

""" 
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [6,9,12]

   whereas the expected correct answer is, [2,3,4]

   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''
   arg1_index=0
   while arg1_index < len(arg1):
      arg_2_sum = 0
      for arg2_elements in arg2:
         arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
      arg1[arg1_index]=arg_2_sum  
      arg1_index+=1
   return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

wrong_add_function(arg1, arg2)

#%% try, except
'''
2.a
Update the numeric section of the function with your changes from 1 for both 
2.b and 2.c
"""
def wrong_add_function(arg1, arg2):
    '''
    The function takes in two lists of integers or strings, 
    and then adds all of arg2 to each item of arg1.
    
    If the lists are integers, it adds them.
    If the lists are strings, it concatenates them.
    '''
    # numeric section
    if all(isinstance(i, int) for i in arg1) and all(isinstance(i, int) for i in arg2):
        for idx in range(len(arg1)):
            arg1[idx] = arg1[idx] + sum(arg2)
        return arg1

    # string section
    elif all(isinstance(i, str) for i in arg1) and all(isinstance(i, str) for i in arg2):
        for idx in range(len(arg1)):
            arg1[idx] = arg1[idx] + ''.join(arg2)
        return arg1

"""

2.b
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
returns an error message to the user, in case users give invalid inputs,
(for example an input of ["5","2", 5])
: "Your input argument [1 or 2] at element [n]
is not of the expected type. Please change this and rerun. Name this function 
exception_add_function()
"""
def exception_add_function(arg1, arg2):
    try:
        if not all(isinstance(i, int) for i in arg1):
            raise TypeError(f"Your input argument 1 at element contains a non-integer. Please change this and rerun.")
        if not all(isinstance(i, int) for i in arg2):
            raise TypeError(f"Your input argument 2 at element contains a non-integer. Please change this and rerun.")
        
        # numeric section of wrong_add_function
        result = [x + sum(arg2) for x in arg1]
        return result
    except TypeError as e:
        print(e)

# Test with invalid input
arg1 = [1, '2', 3]
arg2 = [1, 1, 1]
exception_add_function(arg1, arg2)  # This should raise a TypeError

"""
2.c
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
gets it to process via the string section. IE, do not, outside the function,
change the values of arg_str_1 or arg_str_2. Name this function 
correction_add_function(), i.e you will not be updating the wrong_add_function,
you will simply handle the error of wrong inputs in a seperate function, you want
the wrong_add_function to output its current result you are only bolstering the 
function for edge cases .
'''
"""
def correction_add_function(arg1, arg2):
    try:
        # Try calling wrong_add_function directly
        return wrong_add_function(arg1, arg2)
    except TypeError:
        # Handle the error: convert all items to strings if there's a mix of types
        print("Converting all inputs to strings to handle mixed types.")
        arg1 = [str(x) for x in arg1]
        arg2 = [str(x) for x in arg2]
        return wrong_add_function(arg1, arg2)

# Example with mixed types in the string section
arg_str_1 = ['1', '2', '3']
arg_str_2 = ['1', '1', 1]  # One invalid type (integer in the string list)
print(correction_add_function(arg_str_1, arg_str_2))  

"""
def wrong_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [4,5,6]
   
   If the lists are lists of strings, concatenate them
   Example:
      > wrong_add_function(['1','2','3'],['1','1','1'])
      > ['1111','2111','3111']
   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''
   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
               arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1
arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]

wrong_add_function(arg_str_1,arg_str_2)
"""