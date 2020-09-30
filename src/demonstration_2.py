"""
You have been asked to implement a line numbering feature in a text editor that
you are working on.

Write a function that takes a list of strings and returns a new list that
contains each line prepended by the correct number.

The numbering starts at 1 and the format should be `line_number: string`. Make
sure to put a colon and space in between the `line_number` and `string` value.

Examples:
number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
"""

def number(lines):
    #  define a new list
    # for loop for letter  
        # look at what iteration we're on 
        # format a string with iteration and letter
        # append to a new list

# solution 1 (with .append())
def numer(lines):
    if( len( lines ) < 1 ): return []
    new_array = []
    for count, line in enumerate(lines):
        new_line = "%s :%s" % (count +1, line) #
        new_array.append(new_line)
    return new_array

#  solution 2 (with enumerate)
def number(lines):
    new_lines = []
    # enumerate takes in an iterable (list) and returns a list of iterables (items)
    for count, line in enumerate(lines):
        new_lines.insert(count, f"{count + 1}: {line}")
    
    return new_lines