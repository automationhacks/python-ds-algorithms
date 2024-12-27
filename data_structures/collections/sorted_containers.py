from sortedcontainers import SortedSet


def test_add_item_to_sorted_set():
    sorted_set = SortedSet()
    sorted_set.add(1)
    sorted_set.add(2)
    sorted_set.add(3)
    assert sorted_set == SortedSet([1, 2, 3])


def test_remove_item_from_sorted_set():
    sorted_set = SortedSet([1, 2, 3])
    sorted_set.remove(2)
    assert sorted_set == SortedSet([1, 3])


if __name__ == '__main__':
    test_add_item_to_sorted_set()
    test_remove_item_from_sorted_set()
    print('All tests passed')