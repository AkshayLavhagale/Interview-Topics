# anagram - two strings are written using same letter
# "rail safety" = "fairy tales"
# "roast beef" = "eat for BSE"
# It sometimes changes a proper noun or personal name into a sentence:
# "William Shakespeare" = "I am a weakish speller"
# "Madam Curie" = "Radium came"

s1 = "rail safety"
s2 = "fairy tales"

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

# the sorted built in requires n log n time to process
# (since any comparison based sorting algorithm requires at least n log n time to sort)
# print(sorted(s1) == sorted(s2))  # return True


def is_anagram(s1, s2):
    ht = dict()

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in ht:  # if i is present in hashtable
            ht[i] += 1
        else:  # if we have seen this character first time in hashtable
            ht[i] = 1

    for i in s2:
        if i in ht:
            # so as we have seen f in s1 so if the same character f comes in s2 will remove it
            ht[i] -= 1
        else:
            ht[i] = 1

    # checking the any of the entries in dictionary are 0,
    # if any of them are not equal to 0 means we have not encountered equal amount of same characters in both string then return False
    for i in ht:
        if ht[i] != 0:  # key is not equal to zero
            return False
    return True


print(is_anagram(s1, s2))  # return True
