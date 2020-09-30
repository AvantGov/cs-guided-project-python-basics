"""
Write a function that takes in a two-dimensional list (a list that contains
lists) and returns a new list which contains only the lists from the original
which:

1. were not empty
2. have items that are all of the same type

You can assume that the lists inside the list will only contain integers or
strings. Also, for this challenge, we are assuming that empty arrays are not
homogenous. Also, the resultant lists should be in the same order as the
original list and none of the values should be changed.

**Example:**

Given `[[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]`, your function should
return `[[1, 5, 4], ['b']]`.
"""
def filter_homogenous(arrays):
    # Your code here
    # iterate through the outer list
    new_list = []
    for outer_item in arrays:
        for inner_item in outer_item:
            # iterate through the inner list, check the values
            if (inner_item.isinstance(outer_item)):
                new_list.append(inner_item)
    
    return new_list
    
#  solution 1
def filter_homogenous(arrays):
    new_list = []
    for array in arrays:
        if len(array) > 0:
            for i in range(len(array) - 1):
                if int(array[i]) is True:

# not complete

# solution 2
def filter_homogenous(array):
    newArray = []
    for array in arrays:
        count = 0
        for i in range(len(array)):
            if type(array[i]) != type(array[i + 1]):
                break
            newArray.append(array)
    print(newArray)


#  definite solution
def filter_homogenous(arrays):
    newArray = []
    for array in arrays:
        # checks if array is empty 
        if len(array) == 0
            continue
        
        # checks if the array has length
        if len(array) == 1
            newArray.append(array)
            continue

        # set a flag outside of the loop 
        is_homo = True 
        
        # checks for homogenity 
        for i in range(len(array) - 1):
            if type(array[i]) != type(array[i + 1]):
                is_homo = False
        
        # only appends if the item is different
        if is_homo:
            newArray.append(array)