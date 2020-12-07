# "Look-and-Say" sequence. The first few terms of the sequence are:

# 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...

# To generate a member of the sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit. For example:

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 1211 is read off as "one 1, one 2, then two 1s" or 111221.
# 111221 is read off as "three 1s, two 2s, then one 1" or 312211.

def next_numbers(s):
    result = []  # it will save the next term in the sequence
    i = 0  # this will allow us to move one by one and keep track of how many times we encountered the number
    # two loops - first loop - it will go through each term
    while i < len(s):
        count = 1
        # second loop - will check the term we are on right now is same of next one or not
        # s[i] term we are processing is equal to next term s[i+1]
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    # we are storing result in list but we want to join those elements in list into final string
    return ''.join(result)


# s = "1211"  # return 111221
# print(next_numbers(s))

s = "1"  # s is initially equal to 1
n = 4  # we want to get the 4th term of sequence
# for i in range(n):
#     s = next_numbers(s)  # so if we call next term of s it will be 11
#     print(s) # return 11 21 1211 111221

for i in range(n - 1):
    s = next_numbers(s)  # so if we call next term of s it will be 11
    print(s)  # return 11 21 1211
