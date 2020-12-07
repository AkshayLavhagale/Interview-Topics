"""
Question - Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
The solution set must not contain duplicate triplets.
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def three_sum(nums):
    res = []  # empty array, will store our result here
    # to sort the nums to ascending order, return  [-4, -1, -1, 0, 1, 2]
    # nums = nums.sort() # TypeError: object of type 'NoneType' has no len()
    nums.sort()  # correct way
    length = len(nums)
    # -2 because because we are making two pointers, left and right, which are ahead of i.
    for i in range(length-2):
        # The solution set must not contain duplicate triplets. we are checking that if
        # if there is just three 0 in triplet then that will be answer, so to avoid that
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # this will eliminate duplicate values
        l = i + 1  # [-4, -1, -1, 0, 1, 2] -4 is i and -1 is l(left)
        r = length - 1   # right is last element in array i.e. 2
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:  # so will increase the left by 1, so left at index 1 will go to index 2
                l = l + 1
            elif total > 0:
                r = r - 1  # if total is more than 0 , will move the index from last to second last
            else:  # total = 0
                res.append([nums[i], nums[l], nums[r]])
                # we also need to take care that l and r are not repeating like there are two -1 in left
                while l < r and nums[l] == nums[l+1]:
                    # will increase value of l so it will go to next index, so it will not spend time to recalculate the same number
                    l = l + 1
                while l < r and nums[r] == nums[r-1]:
                    r = r - 1

                # else, means if we did not find any duplicate value of left and right so we can just append the
                # resulting value res.append([nums[i], nums[l], nums[r]]), and will move forward with next index values
                l = l + 1
                r = r - 1
    return res


nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))  # return [[-1, -1, 2], [-1, 0, 1]]

"""
TIME COMPLEXITY
--Sorting takes O(NlogN) - O(NlogN+N^2) so we will consider upper bound - O(N^2)

For space complexity - We didn't use extra space except the 'res', Since we may store the whole 'nums' in it
So it is O(N), N is the length of 'nums'
"""
