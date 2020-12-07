"""
Given an array of sorted integers. We need to find the closest value to the 
given number.
Array may contain duplicate values and negative numbers.
Examples:
    Input :arr[] = {2, 5, 6, 7, 8, 8, 9};
    Target number = 4
    Output : 5
"""


def find_closest_num(A, target):
    # just set to huge value in beginning i.e. infinity, as this is global
    min_diff = float("inf")
    low = 0  # first element in array
    high = len(A) - 1
    closest_num = None  # initially set to None

    # edge cases - for empty list or when the list is only one element
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]

    while low <= high:
        mid = (low + high) // 2

        if mid + 1 < len(A):
            min_diff_right = abs(A[mid+1] - target)  # 8 - 4 = 4
        if mid > 0:
            min_diff_left = abs(A[mid-1] - target)  # 6 - 4 = 2

        # check if absolute value between left and right elements are smaller than any seen prior
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid - 1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid + 1]

        # move the mid point accordingly as is done via binary search
        if A[mid] < target:
            low = mid + 1  # here 8 will be our starting point
        elif A[mid] > target:
            high = mid - 1  # now 6 is our high point
        # if element is the target itself, the closest number itself
        else:
            # if the target number itself present in the list i.e. 4
            return A[mid]
    return closest_num


A = [2, 5, 6, 7, 8, 8, 9]
print(find_closest_num(A, target=4))  # return 5
