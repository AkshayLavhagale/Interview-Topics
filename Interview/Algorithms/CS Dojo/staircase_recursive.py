# if N = 4, then staircase will have 4 steps. we can take 1 or 2 steps at a time
# num_ways(N) return no.of ways we go bottom to top
# if N is 2 then there output should be 2 as well as we can take 1 step or 2 step
# num_ways(3) = num_ways(2)+num_ways(1) # num_ways(n)= num_ways(n-1) + num_ways(n-2)
# num_ways(0) = 1, num_ways(1) = 1 - base condition


def num_ways(n):  # first four lines are like fibonacci sequence only. but not effective. we need use the cache technique for better time complexity
    if n == 0 or n == 1:
        return 1
    else:
        return num_ways(n-1) + num_ways(n-2)


def num_ways_bottom_up(n):
    # to fix the cache requirement we can use the dynamic programming. we can use the bottom up approach
    if n == 0 or n == 1:
        return 1
    # else if we have not returned value yet means value is other than 0 and 1, then will initialize integer array [n+1]
    nums = [n + 1]
    nums[0] = 1
    nums[1] = 1  # first two variable of array 0 and 1
    for i in range(n):  # will run for loop for variable above 2
        nums[i] = nums[i-1] + nums[i-2]
    return nums[n]  # once we find last element of array will return that


def num_ways(n):
    # if we have given the x = {1, 3, 5} this is set which shows no. of steps we are allowed to take
    if n == 0 or n == 1:
        return 1
    return num_ways(n-1) + num_ways(n-2)


def num_ways_X(n):
    if n == 0:  # base condition
        return 1
    return num_ways(n - 1) + num_ways(n - 3) + num_ways(n - 5)  # x = {1, 3, 5}


def num_ways_X(n):
    if n == 0:
        return 1
    total = 0
    for i in {1, 3, 5}:
        if n - 1 >= 0:
            total += num_ways_X(n - i)

    return total


def num_ways_X_bottom_up(n, X):
    if n == 0:
        return 1
    nums = [n+1]  # this is integer array int[n + 1]
    nums[0] = 1  # first element of this array is set to 1
    for i in range(1+n):
        total = 0
        for j in X:
            if i - j >= 0:
                total += nums[i - j]  # num_ways_X[i-j]
        nums[i] = total  # nums[i] is number of ways we can climb the staircase
    return nums[n]

