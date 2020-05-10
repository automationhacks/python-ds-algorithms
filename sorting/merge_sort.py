def merge_sort(alist):
    print(f'Splitting {alist}')

    if len(alist) > 1:
        mid = len(alist) // 2
        # slice operator is O(k), this can be avoided by passing start, end
        # indexes into merge sort
        left = alist[:mid]
        right = alist[mid:]

        # Assume list is sorted
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        # Merge process
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        # Merge any remaining nos in left
        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        # Merge any remaining nos in right
        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1

    print(f'Merging {alist}')
    return alist


def test_merge_sort():
    before = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    after = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    assert merge_sort(before) == after
