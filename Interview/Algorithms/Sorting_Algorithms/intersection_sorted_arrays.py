# Given two arrays, A and B, determine their intersection. That is, what elements are common to A and B?
A = [2, 3, 3, 5, 7, 11]  # i will iterate through list A
B = [3, 3, 7, 15, 31]  # j will iterate through list B

# set function in python operates on list and returns unique element in list
# print(set(A)) # return {2, 3, 5, 7, 11}
# print(set(A).intersection(B))  # return {3, 7}


def intersect_two_array(A, B):
    i = 0
    j = 0
    intersection = []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            # [2, 3, 3, 5, 7, 11] checking the 3 is not equal to 2
            # if i == 0 or A[i] != A[i-1]: # to check the edge case
            if A[i] != A[i-1]:
                intersection.append(A[i])  # will add that in intersection
            i += 1
            j += 1
        elif A[i] < B[j]:  # so if i is on 5 and j is on 7, we want to i and j to equal so we are moving the i to next and check whether it is 7 or no
            i += 1
        else:  # A[i] > B[j]
            j += 1
    # will have O(n + m),  n is size of array A and M is size of array B
    return intersection


print(intersect_two_array(A, B))  # return [3, 7]
