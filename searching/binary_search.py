# Binary search can work only on a sorted list
def binary_search(item, items):
    first = 0
    last = len(items) - 1
    found = False

    while first < last and not found:
        mid = (first + last) // 2

        if item == items[mid]:
            found = True
        else:
            if item < items[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


def test_binary_search():
    numbers = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    assert not binary_search(3, numbers)
    assert binary_search(13, numbers)


def binary_search_recursion(item, items):
    if len(items) == 0:
        return False
    else:
        mid = len(items) // 2
        if item == items[mid]:
            return True
        else:
            if item < items[mid]:
                return binary_search_recursion(item, items[:mid])
            else:
                return binary_search_recursion(item, items[mid + 1:])


def test_binary_search_recursion():
    numbers = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    assert not binary_search_recursion(3, numbers)
    assert binary_search_recursion(13, numbers)


"""
Analysis:

Binary search:
1 comparison, no of items left = n/2
2 comparison, no of items left = n/4

and so on, this can be expressed as n/2 ^ i
Solving for i gives log n.

Hence complexity is actually O(log n)

The slice operator [:mid] has complexity of O(k),
this can be resolved by passing the start and end indices.
"""
