"""
You are given some numeric string as input. Convert the string you are
given to an integer. Do not make use of the built-in "int" function.
Example:
    "123" -> 123
    "-12332" -> -12332
    "554" -> 554
x = "123"
print(int(x)) # built-in function
"""


def str_to_int(input_str):
    output_int = 0
    if input_str[0] == '-':  # checking the first character of input_str is negative or not
        start_idx = 1  # so it will go to index 1 position if the input is negative
        is_negative = True
    else:
        start_idx = 0
        is_negative = False
    # print(10**2 * 1 + 10**1 * 2 + 10**0 * 3) # returns 123
    for i in range(start_idx, len(input_str)):
        place = 10**(len(input_str) - (i + 1))
        # print(place) # return 100 10 1
        # ord('a') = 97, ord('0') = 48, ord('1') = 49, chr(ord('0')) = '0', chr(ord('1')) = '1', chr(ord('10')) = ':',
        # so will just go from 0 till 9. ord('1')-ord('0')=1, 49-48=1
        digit = ord(input_str[i]) - ord('0')
        # print(place, digit)  # return 100 1, 10 2, 1 3
        output_int += place * digit
        # print(output_int) # return 100 120 123
    if is_negative:  # to take care of negative number
        return -1 * output_int
    else:
        return output_int


s = "123"
x = str_to_int(s)
print(type(s))  # class 'str'

s2 = "123"
print(str_to_int(s2))  # return 123

s1 = "-123"
print(str_to_int(s1))  # return -123
