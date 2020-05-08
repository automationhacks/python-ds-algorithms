# generate n - 1, n - 2 as the final limit
# since after every pass the largest no is present
# at the end thru bubble sort


def bubble_sort(numbers):
    for last in range(len(numbers) - 1, 0, -1):
        for idx in range(last):
            if numbers[idx] > numbers[idx + 1]:
                temp = numbers[idx]
                numbers[idx] = numbers[idx + 1]
                numbers[idx + 1] = temp

    return numbers


"""
Bubble sort: Algorithmic analysis:

Regardless of how elements are stored in list
n - 1 passes will be made to sort a list of size n

total comparisons is sum of first n - 1 integers
sum of first n integers is = (n+1)^2 / 2
sum of first n - 1 integers is = (n-1)^2 / 2
Finally: O(n^2)
"""


# Stops if it finds that the list is already sorted
def short_bubble_sort(numbers):
    exchanges = True
    last = len(numbers) - 1

    while last > 0 and exchanges:
        for idx in range(last):
            exchanges = False

            if numbers[idx] > numbers[idx + 1]:
                exchanges = True
                temp = numbers[idx]
                numbers[idx] = numbers[idx + 1]
                numbers[idx + 1] = temp

        last -= 1
    return numbers


NUMBERS = [54, 26, 93, 17, 77, 31, 44, 55, 20]
SORTED = [17, 20, 26, 31, 44, 54, 55, 77, 93]


def test_bubble_sort():
    assert bubble_sort(NUMBERS) == SORTED


def test_short_bubble_sort():
    assert short_bubble_sort(NUMBERS) == SORTED
