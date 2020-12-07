"""
URLify: Write a method to replace all spaces in a string with '%20'. You may
assume that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string. (Note: If
implementing in Java, please use character array so that you can perform this
operation in place.)
"""
input_test_str = "Mr. Akshay Lavhagale"


def urlify(input_str):
    url = ""
    for i in range(len(input_str)):
        if input_str[i] == " ":  # if index i of input string is equal to empty space
            url += "%20"
        else:
            url += input_str[i]
    return url


print(urlify(input_test_str)) # return Mr.%20Akshay%20Lavhagale
