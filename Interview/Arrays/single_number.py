"""
Given an array of integers, every element appears twice except for one.Find that single one.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Input : [1, 2, 2, 3, 1] = 1 ^ 2 ^ 2 ^ 3 ^ 1 = 3
Output : 3
{ element : number of occurrences }
i = 0 { 1 : 1 } # dictionary key : value, i = 0 is index {1(key):1(value)}
i = 1 { 1 : 1, 2 : 1}
i = 2 { 1 : 1, 2 : 2}
i = 3 { 1 : 1, 2 : 2, 3 : 1}
i = 4 { 1 : 2, 2 : 2, 3 : 1} # but with this way it will take extra space as this is using the data structure dictionary
XOR : b1 | b2 # so to get rid of extra space will use the XOR function to make the table 
    0   0 : 0 # 0 ^ 0 = 0
    0   1 : 1 # 0 ^ 1 = 1 
    1   0 : 1 
    1   1 : 0

"""
nums = [1, 2, 2, 3, 1]
ans = 0
for i in range(len(nums)):
    ans ^= nums[i]  # ans = ans ^ nums
print(ans)  # return 3

