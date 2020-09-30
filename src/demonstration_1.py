"""
Define a function that transforms a given string into a new string where the
original string was split into strings of a specified size.

For example:
If the input string was this:

"supercalifragilisticexpialidocious"

and the specified size was 3, then the return string would be:

"sup erc ali fra gil ist ice xpi ali doc iou s"

The assumptions we are making about our input are the following:

- The input string's length is always greater than zero.
- The string has no spaces.
- The specified size is always a positive integer.
"""

# declaring the function with name and parameters 
def split_in_parts(string, part_length):
    
    # create variable for a new list of split strings 
    return_list = []
    print("return list", return_list)

    # define the sub strings that will be injected into the list 
    substring = ""

    # use loop to iterate over the passed in string 
    for letter in string:
        print(letter)
        # if the length of the string is less than part_length:
        if len(substring) < part_length:
            # add the letter to the substring
            substring = substring + letter 
        # otherwise, add the substring to the returned list
        else:
            return_list.append(substring) 
            # then reset the substring to empty 
            substring = ""
            # add the next letter in the iteration
            substring = substring + letter
    
        # handling the remainder of the string 
        if len(substring) > 0:
            return_list.append(substring)

        # rejoin to a space delimited list?
        return_string = " ".join(return_list)

        # return the list
        return return_list
    
# calling the function
split_in_parts("supercalifragilisticexpialidocious", 3)

# more efficient approach
for i in range(0, len(string) + 1, 3): # for (int i = 0; i < len(string) + 1; i += 3)
    print(string[i: (i + 3)])