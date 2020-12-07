# Binary Search is a technique that allows you to search an ordered list of elements very efficiently using a divide-and-conquer strategy.

# Method 1 Linear Search - Not effective - to find element we have to iterate all element in list to check whether present or not


def linear_search(data, target):  # data is list and target is element we are looking for
    for i in range(len(data)):
        if data[i] == target:  # if element in loop is target element we are looking for
            return True
    return False

# Method 2 - iterative approach - O(log n) means if list have billion entries then log n is 30 so we need to take 30 operations so its good


def binary_search_iterative(data, target):
    low = 0  # index of first element
    high = len(data) - 1  # index of last element
    while low <= high:  # while low is less than equal to high
        mid = (low + high) // 2  # getting middle element, by taking index of 0
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1  # if the target is 5, the middle point of list 17. Now the elements greater than 17 are invalid. so 17 is new last point
        else:
            low = mid + 1  # if target is 25, then we see the right side of list. 19 becomes first element and 37 become last
    return False

# method 3 - recursive method


# we are not using loop so we are taking the low and high point as parameter
def binary_search_recursive(data, target, low, high):
    if low > high:  # base condition, if this is case where low is greater than high so we cannot find element in the list
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # mid - 1 becomes new high point
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            # mid + 1 becomes new high point
            return binary_search_recursive(data, target, mid + 1, high)
    return False


data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 25

print(binary_search_iterative(data, target))
# in recursive low is 0 and high is len(data) - 1
print(binary_search_recursive(data, target, 0, len(data) - 1))
