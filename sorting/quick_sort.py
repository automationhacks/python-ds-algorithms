def quick_sort(alist):
    return quick_sort_recurse(alist, 0, len(alist) - 1)


def quick_sort_recurse(alist, first, last):
    if first < last:
        split_point = partition(alist, first, last)

        # Recurse this for left and right halves
        quick_sort_recurse(alist, first, split_point - 1)
        quick_sort_recurse(alist, split_point + 1, last)

    return alist


def partition(alist, first, last):
    # Choosing first item as pivot value
    # We can also choose a random value between first and last to improve
    # performance
    pivot_value = alist[first]

    left_mark = first + 1
    right_mark = last
    stop = False

    while not stop:
        # Increment left mark till we find a value > pivot value
        while left_mark <= right_mark and alist[left_mark] <= pivot_value:
            left_mark += 1

        # Decrement right mark till we find a value < pivot value
        while alist[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1

        # If we have crossed over
        if right_mark < left_mark:
            stop = True
        else:
            # Exchange left and right mark values
            temp = alist[left_mark]
            alist[left_mark] = alist[right_mark]
            alist[right_mark] = temp

    # At split point, exchange pivot value with right mark and return the
    # partition point
    temp = alist[first]
    alist[first] = alist[right_mark]
    alist[right_mark] = temp

    return right_mark


def test_merge_sort():
    before = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    after = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    assert quick_sort(before) == after
