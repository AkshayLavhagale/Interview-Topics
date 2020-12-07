"""
String Compression: Implement a method to perform basic string compression
using the counts of repeated characters. For example, the string aabcccccaaa
would become a2b1c5a3. If the"compressed" string would not become smaller than
the original string, your method should return the original string. You can
assume the string has only uppercase and lowercase letters (a-z).
"""


def string_compression(input_str):
    compressed_str = ""
    count = 1
    # in this loop we are checking the character we are on and next character are equal or not
    for i in range(len(input_str) - 1):
        if input_str[i] == input_str[i + 1]:
            count += 1
        else:  # the b in input_str_test_1
            compressed_str += input_str[i] + str(count)
            count = 1
    # this is to catch the last part of string like aaa in input_str_test_1
    compressed_str += input_str[i] + str(count)

    # If the"compressed" string would not become smaller than the original string, your method should return the original string.
    if len(compressed_str) >= len(input_str):
        return input_str
    else:
        return compressed_str


input_str_test_1 = "aabcccccaaa"
input_str_test_2 = "aaaaaabbccbcaabb"


print(string_compression(input_str_test_1))  # return a2b1c5a3
print(string_compression(input_str_test_2))  # return a6b2c2b1c1a2b2
