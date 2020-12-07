# Given a string, calculate the number of consonants present using recursion
# consonants are other than vowels - a, e, i, o, u

input_str = "abc de"
vowels = "aeiou"


def iterative_count_consonants(input_str):
    count = 0
    for i in range(len(input_str)):
        # is the character we are on is not in vowels and we are normalizing every character to lower case
        # isalpha check the alphabetical character or no that means it do not consider the spaces
        if input_str[i].lower() not in vowels and input_str[i].isalpha():  # if both conditions true
            count += 1  # then will add up count by 1

    return count  # otherwise will not add up in count


def recursive_count_consonants(input_str):
    if input_str == "":  # will run the recursive call till string is empty, base condition
        return 0
    # if first character of input str means input_str[0]
    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])


print(iterative_count_consonants(input_str))
print(recursive_count_consonants(input_str))
