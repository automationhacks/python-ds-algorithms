def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number

    return total


def sum_list_recursive(numbers):
    if len(numbers) == 1:
        return numbers[0]

    return numbers[0] + sum_list_recursive(numbers[1:])


numbers = [1, 2, 5, 9, 13, 7]


def test_sum():
    total = sum_list(numbers)
    assert total == 37


def test_sum_recursive():
    total = sum_list_recursive(numbers)
    assert total == 37
