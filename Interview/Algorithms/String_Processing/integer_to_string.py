"""
You are given some integer as input, (i.e. ... -3, -2, -1, 0, 1, 2, 3 ...)
Convert the integer you are given to a string. Do not make use
of the built-in "str" function.
Examples:
    Input: 123
    Output: "123"
    Input: -123
    Output: "-123"
"""
# a = 123
# a = print(type(a))  # class int
# a = str(123)  # builtin python function
# a = print(type(a))  # class string


def int_to_str(input_int):
    if input_int < 0:  # if input is negative number
        is_negative = True
        input_int *= -1  # converts to positive integer, # input_int = input_int * 10
    else:
        is_negative = False

    output_str = []
    while input_int > 0:
        # ord('a') = 97, ord('0') = 48, ord('1') = 49, chr(ord('0')) = '0', chr(ord('1')) = '1', chr(ord('10')) = ':',
        # so will just go from 0 till 9
        output_str.append(chr(ord('0') + input_int % 10))
        # print(input_int % 10) # return 3 2 1
        input_int //= 10  # input_int = input_int // 10

    # a = ['3', '2', '1'], now they are in reverse order and in list not just in string
    output_str = output_str[::-1]  # reverse the list
    # ''.join(a) = '123'
    # '-'.join(a) = '1-2-3'
    output_str = ''.join(output_str)
    # print(output_str)  # return 123
    if is_negative:  # to take care of negative numbers
        return '-' + output_str
    else:  # if not negative
        return output_str


print(int_to_str(123))  # return 123
print(int_to_str(-123))  # return -123

# input_int = 123
# print(type(input_int)) # return <class 'int'>

# output_str = int_to_str(input_int)
# print(type(output_str)) # return <class 'str'>
