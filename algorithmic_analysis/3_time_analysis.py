# Program to find sum of n natural numbers
import time


def sum_of_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


def sum_of_n_using_summation(n):
    return (n * (n + 1)) // 2


def timer(func, args):
    start = time.time()
    value = func(args)
    end = time.time()
    return value, end - start


print(timer(sum_of_n, 10))
print(timer(sum_of_n_using_summation, 10))
