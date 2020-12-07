# using a linear amount of time and a constant amount of space.
# palindrome - reading from back to front is also same as front to back
# solution uses extra space proportional to size of string "s"
s = "Was it a cat I saw?"
s1 = "Test"
# s = ''.join([i for i in s if i.isalpha()]).replace(" ", "").lower()
# # print(s) # return wasitcatisaw
# print(s == s[::-1])  # return True

# solution that does not require linear space and just require linear time

# will have i which will read character from front to back and j will read from back to front


def is_palindrome(s):  # this solution will need little time
    i = 0
    j = len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:  # so here we checking w is alphanumeric or not
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():  # if not equal
            return False
        i += 1  # if equal
        j -= 1
    return True  # if it goes through while loop then it is palindrome


print(is_palindrome(s))  # return True
print(is_palindrome(s1))  # return False
