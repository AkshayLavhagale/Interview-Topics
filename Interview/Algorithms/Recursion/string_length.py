# Given a string, calculate its length recursively.
str_1 = "lucidProgramming"
# print(len(str_1))


def iterative_str_length(input_str):
    count = 0
    for i in range(len(input_str)):
        count += 1
    return count


# base condition - will call this function till we get empty string
def recursive_str_length(input_str):
    if input_str == "":
        return 0
    # slicing function which ignores first character in string and return from first till end of string
    return 1 + recursive_str_length(input_str[1:])


print(iterative_str_length(str_1))
print(recursive_str_length(str_1))
