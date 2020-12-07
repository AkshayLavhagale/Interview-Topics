# String Rotation: Given two strings, s1 and s2, write code to check if s2 is
# a rotation of s1 (e.g. "waterbottle" is a rotation of "erbottlewat"). just checking if it had all same letters

import string
test_rot_string_1 = "waterbottle"
test_rot_string_2 = "erbottlewat"


def is_string_rotation(str_1, str_2):
    if len(str_1) != len(str_2):
        return False
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    # key = list(string.ascii_lowercase)-means list of all alphabet characters, value = 0
    # print(list(string.ascii_lowercase)) - will print all the alphabets ['a', 'b', 'c', 'd', 'e', 'f',.....,'z']
    dict_1 = dict.fromkeys(list(string.ascii_lowercase), 0)
    dict_2 = dict.fromkeys(list(string.ascii_lowercase), 0)
    # print(dict_1)  # {'a': 0, 'b': 0, 'c': 0, 'd': 0, ....., 'z':0}
    for i in range(len(str_1)):  # here we already know the length of both strings is equal
        # here we are looping through the string and anytime when encounter a letter we are checking the dictionary of that letter
        # and checking that we encountered in first string and adding the value of that corresponding letter
        dict_1[str_1[i]] += 1
        dict_2[str_2[i]] += 1
    # if both dict are equal to each other then string rotation is true
    return dict_1 == dict_2


print(is_string_rotation(test_rot_string_1, test_rot_string_2))  # return True
