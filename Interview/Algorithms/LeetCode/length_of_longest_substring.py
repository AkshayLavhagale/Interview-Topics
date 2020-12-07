"""
Given a string, find the length of the longest substring without repeating characters.
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
"""
# sliding window technique


def length_of_longest_substring(s: str) -> int:
    if len(s) == 0:  # base condition
        return 0
    map = {}  # dictionary
    max_length = start = 0  # two variables max_length and start
    for i in range(len(s)):
        # if s[i](particular character) is in dictionary or not and also the start value is less than or equal to value we are currently on
        if s[i] in map and start <= map[s[i]]:
            # then we are increasing the value in start
            start = map[s[i]] + 1
        else:  # i - start + 1 = new length
            max_length = max(max_length, i - start + 1)
        map[s[i]] = i
    return max_length


s = "abcabcbb"
print(length_of_longest_substring(s))  # return 3
