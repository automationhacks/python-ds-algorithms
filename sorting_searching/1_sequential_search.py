def search_sequentially(item, list_):

    pos = 0
    found = False
    while pos < len(list_) and not found:
        if item == list_[pos]:
            found = True
        else:
            pos += 1

    return found

# print(search_sequentially(1, [2, 3, 4, 1]))
# print(search_sequentially('a', ['b', 'c', 'a', 'd']))

"""
Algorithmic analysis:
1. In an unsorted list, probability of finding item is same for all items
2. Basic unit of computation is the no of comparisons performed.

Best case: Item is the first item requiring only single comparison
Worst case: Item is the last item in the list
Average case: Item is found in middle of the list

Time complexity is O(n)
"""

# Sequential search after sorting:


def search_sequentially_after_sort(item, alist):
    pos = 0
    found = False
    alist.sort()

    while pos < len(alist) and not found:

        if alist[pos] > item:
            break

        if item == alist[pos]:
            found = True
        else:
            pos += 1

    return found


alist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(search_sequentially_after_sort(19, alist))

"""
Complexity is still O(n), however if item is not present,
then sorting ensures the average case becomes n/2 instead of n
"""
