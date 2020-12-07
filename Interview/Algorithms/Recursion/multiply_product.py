# Given two numbers, find their product using recursion.
x = 5
y = 3


# if we use the bigger numbers like x = 500, y=10000 then it will fail as maximum depth recursion exceeded
def recursive_multiply(x, y):
    #     if y == 0:
    #         return 0
    #     return x + recursive_multiply(x, y - 1)

    # this cuts down the total number of recursive calls
    if x < y:
        # will flip the y value first and then x
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    return x + recursive_multiply(x, y - 1)


# print(x * y)
print(recursive_multiply(x, y))
