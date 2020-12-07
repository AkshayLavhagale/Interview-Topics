"""
Given a N cross M matrix in which each row is sorted, find the overall median of the matrix.
Assume N*M is odd.
For example,
Matrix=
[1, 3, 5]
[2, 6, 9]
[3, 6, 9]
A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
Median is 5. So, we return 5.
"""


def median_matrix(A):
    if len(A) == 1:  # if array have just one list
        vec = A[0]
        # this will give the middle element of the vector
        # divided by 2 to get middle element of the list
        return vec[len(vec) // 2]
    else:  # if matrix have many rows and not just one
        new_list = []
        for row in range(len(A)):  # looping through all the rows in the array
            # extend function is for list, it taking the list of A[i] and continuously extending the new list on top of row is
            new_list.extend(A[row])
        # print(new_list)  # return [1, 3, 5, 2, 6, 9, 3, 6, 9]
        new_list = sorted(new_list)
        # print(new_list) # return [1, 2, 3, 3, 5, 6, 6, 9, 9]
    # divided by 2 to get middle element of the list
    return new_list[len(new_list) // 2]


l1 = [1, 3, 5]
l2 = [2, 6, 9]
l3 = [3, 6, 9]
A = [l1, l2, l3]

A1 = [l1]  # if just one list, edge case to consider

print(median_matrix(A))  # return 5
print(median_matrix(A1))  # return 3
