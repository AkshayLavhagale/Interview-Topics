# how many ways to decode this message?
# 'a'- 1, 'b'-2,..., 'l'-12,..., 'z'-26, "ab"- "12"
# write a function input = data and returns number of messages that could have been the original message
# means how many ways there to decode this "12" message to original message
# data decode to either "12" or "l"
# if data is "01" then it will return 0 as there is no code assigned to "01"
# data string will only have digits between 0 and 9
# time complexity = O(n), n is number of letter in given string
# num_ways("3") = 1 - "c"
# num_ways("") = 1 - "" # 1. base condition for recursion
# num_ways("12345") = 1. recursive case - "a" + decode("2345") or "l" + decode("345") = num_ways("2345") + num_ways("345")
# num_ways("27345") = 2. recursive case - "b" + decode("7345")
# num_ways("011") = 0 # 2. base condition for recursion

def helper(data, k, memo):  # will call this function recursively, data is string and k is non-negative integer
    # in helper function will only look at last k letters of data. data = "abcd", k = 3, then will look at only "bcd"
    # helper function will tell like how many ways we can decode last k letters of the string
    if k == 0:  # if no. of letters we are going to look is 0, num_ways("") = 1
        return 1  # base condition 1

    # if first letter is 0, num_ways("011") = 0, s is starting index
    s = data.length - k
    if data[s] == '0':
        return 0  # base condition 2

    if memo[k] != None:
        return memo[k]

    result = helper(data, k - 1, memo)
    if k >= 2 and int(data[s:s+2]) <= 26:
        result += helper(data, k - 2, memo)
    memo[k] = result

    return result


def num_ways(data):  # this function should return 2 because there are two possible messages
    memo = new_int[data.length + 1]  # initialize to Nulls
    # data.length is full string and not just k letters
    return helper(data, data.length, memo)
