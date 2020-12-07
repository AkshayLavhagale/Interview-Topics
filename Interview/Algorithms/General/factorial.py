"""
Write a iterative and recursive function that implements the factorial
of a number.
5! = 5 * 4 * 3 * 2 * 1
   = 120
n! = n * n - 1 * ... * 1
"""
n = 5


def fact_iter(n):
    x = 1  # this variable will store the multiplications
    for i in range(n, 0, -1):
        # print(i)  # return 5 4 3 2 1
        x *= i  # x = x * i
    return x


def fact_recursive(n):  # with recursive way the cache memory is stored for previous history, so it will take less time
    if n <= 1:  # base condition, when the last number takes us too 1 then will return 1
        return 1
    else:
        return n * fact_recursive(n - 1)


print(fact_iter(n))  # return 120
print(fact_recursive(n))  # return 120
