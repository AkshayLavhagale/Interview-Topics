# how to determine if a string has all unique characters
unique_str = "AbcDEfgH"

non_unique_str = "non Unique str"


def normalize(input_str):
    input_str = input_str.replace(" ", "").lower()
    return input_str


# Method 1 - using hashtable - this using data structure as dictionary - which affect space complexity
def is_unique_1(input_str):
    d = dict()
    for i in input_str:
        if i in d:
            return False  # means we have already encountered that character before in dictionary
        else:
            d[i] = 1
    return True


def is_unique_2(input_str):  # method 2 - without data structure use
    # set function returns all the unique characters by unfolding the string
    # print(set("unique")) = ['i', 'q', 'u', 'e', 'n']
    return len(set(input_str)) == len(input_str)


def is_unique_3(input_str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in input_str:
        if i in alpha:
            # so if that character is in alphabet will replace that character with Nothing
            alpha = alpha.replace(i, "")
        else:
            return False  # so in non_unique_str when the second time n occurs it returns false
    return True  # if we don't write this line it will return None


unique_str = normalize(unique_str)
non_unique_str = normalize(non_unique_str)

print(is_unique_1(unique_str))  # True
print(is_unique_1(non_unique_str))  # False

print(is_unique_2(unique_str))  # True
print(is_unique_2(non_unique_str))  # False

print(is_unique_3(unique_str))  # True
print(is_unique_3(non_unique_str))  # False
