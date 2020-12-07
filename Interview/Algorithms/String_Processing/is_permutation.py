# Given two strings, write a function to determine if one is a permutation of the other.
# ask interviewer if there are any spaces in string or not. If not no need of replace strings function
is_permutation_1 = "AbC  "
is_permutation_2 = "AcB"

# time complexity = O(n log n) as we are using sorting here
# space complexity = O(1) # as we are not using any external data structure once we sort them


def is_permutation(str_1, str_2):
    str_1 = str_1.replace(" ", "").lower()
    str_2 = str_2.replace(" ", "").lower()

    if len(str_1) != len(str_2):
        return False

    # we converted string to list because sorted applies on list and then we are converting that sorted list back to string
    str_1 = ''.join(sorted(str_1))
    str_2 = ''.join(sorted(str_2))

    # n is of same of length of str_1 and str_2 as this already passed through if len(str_1) != len(str_2):
    n = len(str_1)
    for i in range(n):
        if str_1[i] != str_2[i]:
            return False

    return True

# time complexity = O(n) - there is just for loop
# space complexity = O(n) - dictionary is looping through


def is_permutation_two(str_1, str_2):  # will use hashtable
    str_1 = str_1.replace(" ", "").lower()
    str_2 = str_2.replace(" ", "").lower()

    if len(str_1) != len(str_2):
        return False

    d = dict()
    # will add the value in dictionary per key and then will remove the value with next arrival
    # if all the values are not 0 then return False
    for i in str_1:
        if i in d:
            d[i] -= 1
        else:  # if i not in d
            d[i] = 1
    for i in str_2:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
    # for every value present in dict is every single value in dict = 0 if true it is permutation
    return all(value == 0 for value in d.values())


print(is_permutation(is_permutation_1, is_permutation_2))  # return True
print(is_permutation_two(is_permutation_1, is_permutation_2))  # return True
