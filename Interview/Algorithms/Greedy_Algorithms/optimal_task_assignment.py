# optimal way in which to assign tasks to workers. Each worker must work on exactly two tasks. Tasks are independent and each task takes a fixed amount of time.

# Problem: Assign tasks to workers such that the time it takes to complete all tasks is minimized.
# given an array represent the duration of task
# max(6+3, 2+7, 5+5) = 10

# Method 1 - brute force = enumerating every possible pair would require generating n!/2^n/2 pairs,
# where n is number of tasks in given array


# Method 2 - Greedy approach - pair the longest task with shortest one
# first will sort the tasks, then will pick longest and shortest duration
# time complexity is O(n log n) due to sorting

A = [6, 3, 2, 7, 5, 5]


# def task_assignment(A):
#     A = sorted(A)
#     # print(A) # return [2, 3, 5, 5, 6, 7]

#     # now we will do length of Array / 2
#     for i in range(len(A) // 2):
#         # [~i] = not i, print(~0) = -1, print(~1) = -2, this will start from back of array
#         # now A[i] and A[~i] will give us pairs of 2,7 3,6 and 5,5
#         # print(A[i], A[~i]) # this will return None at end of result due to two print statement.
#         # First is inside function and second is outside function. When function not return any thing that time it return None value.
#         return A[i], A[~i]
# print(task_assignment(A))
A = sorted(A)
for i in range(len(A) // 2):
    print(A[i], A[~i]) # return pairs of 2,7 3,6 and 5,5
    