# Binary search can work only on a sorted list


def binary_search(item, alist):

    first = 0
    last = len(alist) - 1
    found = False

    while first < last and not found:
        mid = (first + last) // 2

        if item == alist[mid]:
            found = True
        else:
            if item < alist[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(3, testlist))
print(binary_search(13, testlist))


def binary_search_recursion(item, alist):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if item == alist[mid]:
            return True
        else:
            if item < alist[mid]:
                return binary_search_recursion(item, alist[:mid])
            else:
                return binary_search_recursion(item, alist[mid+1:])


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search_recursion(3, testlist))
print(binary_search_recursion(13, testlist))

"""
Analysis:

Binary search:
1 comparison, no of items left = n/2
2 comparison, no of items left = n/4

and so on, this can be expressioned as n/2^i
Solving for i gives log n.

Hence complexity is actually O(log n)

The slice operator [:mid] has complexity of O(k),
this can be resolved by passing the start and end indices.
"""
