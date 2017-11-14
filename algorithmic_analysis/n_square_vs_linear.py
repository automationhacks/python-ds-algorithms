import time
from random import randrange

"""
Write two Python functions to find the minimum number in a list. 
The first function should compare each number,
to every other number on the list. O(n2).

The second function should be linear O(n).
"""


def find_min(a_list):
    overall_min = a_list[0]

    for i in a_list:
        is_smallest = True
        for j in a_list:
            if i > j:
                is_smallest = False

        if is_smallest:
            overall_min = i

    return overall_min


def find_min_linear(lst):
    min_so_far = lst[0]
    for num in lst:
        if num < min_so_far:
            min_so_far = num

    return min_so_far


def run(func):
    for list_size in range(1000, 10001, 1000):
        a_list = [randrange(1000000) for x in range(list_size)]
        start = time.time()
        print('minimum: ', func(a_list))
        end = time.time()
        print('size: {} time: {}'.format(list_size, end - start))

if __name__ == '__main__':
    print('Quadratic: O(n^2)')
    print('=' * 40)
    run(find_min)

    print('Linear: O(n)')
    print('=' * 40)
    run(find_min_linear)
