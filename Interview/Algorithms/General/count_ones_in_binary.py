"""
Problem: Find the number of 1s in the binary representation of a number.
num_ones(2) = 1 --> since "10" is the binary representation of the number "2".
num_ones(5) = 2 --> since "101" is the binary representation of the number "5"
num_ones(11) = 3 --> since "1011" is the binary representation of the number "11"
"""

# Method 1 - using python bin function
num = 5  # we can use the 'bin' as python built in function
# print(bin(num))  # return 0b101 - python show 0b to showcase it is binary number
one_sum = 0
bin_rep = bin(num)[2:]  # to remove 0b form result
for i in bin_rep:
    # this i we are using to convert that to int so we can actually sum it
    one_sum += int(i)
print(one_sum)  # return 2

# complicated so avoid - method 2 - using bitwise operators like '&'(and), '>>'(shift)
# 1011 (num=11)
# 0001 # so in (one_sum += num & 1) the last 1 we are adding with num
#
one_sum = 0
while num:
    # 0001 # so in (one_sum += num & 1) the last 1 we are adding with num - 1011
    one_sum += num & 1
    # 001 # so in (one_sum += num & 1) the last 1 we are adding with num and shifting gets us new number to - 101
    num >>= 1
print(one_sum)  # return 2
