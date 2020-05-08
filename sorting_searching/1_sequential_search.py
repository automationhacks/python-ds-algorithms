# Algorithmic analysis:
# 1. In an unsorted list, probability of finding item is same for all items
# 2. Basic unit of computation is the no of comparisons performed.
# Time complexity is O(n)


def search_sequentially(item, items):
    pos = 0
    found = False
    while pos < len(items) and not found:
        if item == items[pos]:
            found = True
        else:
            pos += 1

    return found


def test_sequential_search():
    items = [2, 3, 4, 1]
    assert search_sequentially(1, items)
    assert not search_sequentially(10, items)


# Complexity is still O(n), however if item is not present,
# then sorting ensures the average case becomes n/2 instead of n
def search_sequentially_after_sort(item, items):
    pos = 0
    found = False
    items.sort()

    while pos < len(items) and not found:
        if items[pos] > item:
            break

        if item == items[pos]:
            found = True
        else:
            pos += 1

    return found


def test_sequential_search_after_sort():
    numbers = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    assert search_sequentially_after_sort(19, numbers)
