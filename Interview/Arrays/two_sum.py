# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# We investigate three different approaches to solving this problem.
A = [-2, 1, 2, 4, 7, 11]
target = 13

# Method 1: A brute-force approach that takes O(n ^ 2) time to solve with O(1) space. We loop through the array and create all possible pairings of elements.

# time complexity = O(n^2) as we are going through for loops here
# space complexity = 0(1) we are just looping through


def two_sum_brute_force(A, target):
    # we are looping through the length of array from 0 to len-1, means from -2 to 11
    for i in range(len(A)-1):
        # here we are looping through 1 to 11, in next loop we are removing the previous i
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                # printing the elements that form the target i.e. 2 and
                print(A[i], A[j])
                return True
    return False


# print(two_sum_brute_force(A, target))

# Method 2: A slightly better approach time-wise, taking O(n) time, but worse from a space standpoint, with a space complexity of O(n). In this approach, we make use of an auxiliary hash table to keep track of whether it's possible to construct the target based on the elements we've processed thus far in the array.
# A = [2, 4, 6]
# target = 10
# i = 0
# ht = dict()
# ht[8] = 2  # here in hashtable we do target - element , 10 - 2
# i = 1
# ht[6] = 4  # as the 4 was not there in hashtable before we minus that with target

# time complexity = O(n) we are just looping through the array one time
# space complexity = 0(n) we are just dictionary here, and in some case we might have to keep the entry which is not that ideal
def two_sum_hash_table(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:  # if i is present in the hashtable
            print(ht[A[i]], A[i])
            return True
        else:  # if i is not present in the hash table
            ht[target - A[i]] = A[i]
    return False


# print(two_sum_brute_force(A, target))


# Method 3: This approach has a time complexity of O(n) and a constant space complexity, O(1). Here, we have two indices that we keep track of, one at the front and one at the back. We move either the left or right indices based on whether the sum of the elements at these indices is either greater or lesser than the target element.
# time complexity = 0(n) (n is size of array)
# space complexity = 0(1) (as we are not using any hashtable here)
def two_sum(A, target):
    # it start at beginning with -2 and i keep increment with position if A[i] + A[j] < target
    i = 0
    # so j is at end of array i.e. at 11 and j keep decrement with position if A[i] + A[j] > target
    j = len(A) - 1
    while i <= j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1  # i keep increment with position if A[i] + A[j] < target
        else:
            j -= 1  # j keep decrement with position if A[i] + A[j] > target
    return False


print(two_sum(A, target))
