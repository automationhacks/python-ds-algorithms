# Finds position of item with max value and does only one exchange
# Complexity is O(n^2) but performs better in benchmarks
# because of limited exchanges


def selection_sort(numbers):
    for fill_slot in range(len(numbers) - 1, 0, -1):
        max_pos = 0
        for idx in range(1, fill_slot + 1):
            if numbers[idx] > numbers[max_pos]:
                max_pos = idx

        temp = numbers[fill_slot]
        numbers[fill_slot] = numbers[max_pos]
        numbers[max_pos] = temp
    return numbers


def test_selection_sort():
    numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sorted = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    assert selection_sort(numbers) == sorted
