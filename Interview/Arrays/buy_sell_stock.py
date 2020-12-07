# Given an array of numbers consisting of daily stock prices, calculate the maximum amount of profit that can be made from buying on one day and selling on another day.
# We consider two approaches to this problem. In the first, we consider a brute force approach that solves the problem in O(N^2), where N is the size of the array of numbers.
A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# time complexity = O(n^2)
# space complexity = 0(1)


def buy_sell_once(A):
    max_profit = 0
    # this start with 310 and goes with further elements.
    for i in range(len(A) - 1):
        # this start with i + 1, so start with 315 and further elements
        for j in range(i + 1, len(A)):
            if A[j] - A[i] > max_profit:
                max_profit = A[j] - A[i]
    return max_profit


# print(buy_sell_once(A))

# We then improve upon this solution to take our solution to a time complexity of O(N).
#       0    5   0     20   0    10   30   0    25   20
# A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# time complexity = O(n) just equal to size of array
# space complexity = 0(1)
def buy_sell_once_two(A):
    max_profit = 0  # start with 0 and then to 5 so we keep track of max profit till now by comparing it
    min_price = A[0]  # start with first element of the array
    for price in A:  # we are looping through all the prices in array
        # we compare 310 and 315 in the beginning
        min_price = min(min_price, price)
        compare_profit = price - min_price  # so 315 - 310 = 5
        # checking the compared profit we have is maximum compare till so far
        max_profit = max(max_profit, compare_profit)

    return max_profit


print(buy_sell_once_two(A))
