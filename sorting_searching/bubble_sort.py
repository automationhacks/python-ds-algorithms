def bubble_sort(alist):
    # generate n - 1, n - 2 as the final limit
    # since after every pass the largest no is present
    # at the end thru bubble sort

    for pass_num in range(len(alist) - 1, 0, -1):
        for i in range(pass_num):
            if alist[i] > alist[i + 1]:
                # Exchange nos if left > right
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp

# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# bubble_sort(alist)
# print('After sorting {}'.format(alist))

"""
Algorithmic analysis:

Regardless of how elements are stored in list
n - 1 passes will be made to sort a list of size n

total comparisons is sum of first n - 1 integers

sum of first n integers is = n^2 / 2 + n / 2

sum of first n - 1 integers is = n^2 / 2 + n / 2 - n which is n ^ 2 / 2 - n / 2 

finally: this is still O(n^2)
"""

# Bubble sort can be enhanced to stop if it finds the list is already sorted.
# This approach called as short bubble.


def short_bubble_sort(alist):
    exchanges = True
    pass_num = len(alist) - 1

    while pass_num > 0 and exchanges:
        for i in range(pass_num):

            exchanges = False
            if alist[i] > alist[i + 1]:

                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp

        pass_num -= 1

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
short_bubble_sort(alist)
print('After sorting {}'.format(alist))
