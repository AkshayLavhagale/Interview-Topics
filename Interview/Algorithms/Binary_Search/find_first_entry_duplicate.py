# takes an array of sorted integers and a key and returns the index of the first occurrence of that key from the array.

# For example, for the array:
# [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

# with target = 108, the algorithm would return 3, as the first occurrence of 108 in the above array is located at index 3.
#     0    1   2   3    4    5    6    7   8    9
A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108


# def find_(A, target): linear approach takes time as have to go through looping each element
#     for i in range(len(A)):
#         if A[i] == target:
#             return i  # return index
#     return None


def find(A, target):  # binary search approach
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2

        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            # so in our case 243(mid) is higher than 108, so 108 will be our highest point
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if A[mid - 1] != target:
                return mid
            high = mid - 1
    return None


x = find(A, target)  # return 3
print(x)
