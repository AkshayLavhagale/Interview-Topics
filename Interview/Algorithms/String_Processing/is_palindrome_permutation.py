# Palindrome: A word or phrase that is the same forwards and backward.
# Permutation: A rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# "Taco Cat" tac o cat - palindrome, just one letter is separating others are twice
palin_perm = "Tact Coa"
# will use dictinary , key t = value 2, key a = value 2,  key c = value 2, key o = value 1

# time complexity = O(n), n is length of string
# space complexity = O(n), as we are filling up this dictionary


def is_palin_perm(input_str):
    input_str = input_str.replace(" ", "").lower()

    d = dict()  # created hashtable

    # time complexity = O(n), n is length of string
    for i in input_str:  # will check whether character is in string
        if i in d:
            d[i] += 1  # increment value of that key by 1
        else:
            d[i] = 1

    odd_count = 0
    for k, v in d.items():  # for key and values in dictionary
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:  # means it is more than 1
            return False
    return True


print(is_palin_perm(palin_perm))
