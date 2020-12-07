# A = 149 + 1 = 150 - Add one two rightmost digit, propagate carry throughout array, similar to standard grade school approach
A1 = [1, 4, 9]
A2 = [9, 9, 9]
# map applies the string function to each element of the array
# s = ''.join(map(str, A))
# print(s)  # it will return string 149
# print(int(s) + 1)  # it will return the string 150, but to do with arbitrary precision increment we have to do other way


def plus_one(A):
    A[-1] += 1  # adding the one to right most element of the array
    # staring in the reversed order till we reach last element of the array, means in 149, 9 is first and 1 is last
    for i in reversed(range(1, len(A))):
        if A[i] != 10:  # if there is just one digit so we don't have anything to go ahead
            break
        A[i] = 0
        A[i-1] += 1
    # means the first element is 10 (in case of 9,9,9 array) so we have to add one more array and append it to array
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


print(plus_one(A1))  # return [1, 5, 0]
print(plus_one(A2))  # return [1, 0, 0, 0]
