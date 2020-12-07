# Given a string, develop an algorithm to return the first occurring uppercase letter. We require both an iterative and recursive solution to this problem.

def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):  # we will loop through each character of string
        # if character in input_str is uppercase, isupper() is python function
        if input_str[i].isupper():
            return input_str[i]  # return that character
    return "No uppercase character found"


def find_uppercase_recursive(input_str, index=0):  # initially index set to 0
    if input_str[index].isupper():  # base condition
        return input_str[index]
    if index == len(input_str) - 1:
        return "No uppercase character found"
    return find_uppercase_recursive(input_str, index + 1)

# For instance, for the strings:


str_1 = "lucidProgramming"
str_2 = "LucidProgramming"
str_3 = "lucidprogramming"

# The algorithm should return "P", "L", and output a message indicating no such capital letter found, respectively for the above strings.

print(find_uppercase_iterative(str_1))
print(find_uppercase_iterative(str_2))
print(find_uppercase_iterative(str_3))

print(find_uppercase_recursive(str_1))
print(find_uppercase_recursive(str_2))
print(find_uppercase_recursive(str_3))
