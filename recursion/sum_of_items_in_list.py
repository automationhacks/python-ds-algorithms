def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number

    return total


def sum_list_recursive(numbers):
    if len(numbers) == 0:
        return 0

    return numbers[0] + sum_list_recursive(numbers[1:])


def test_sum():
    numbers = [1, 2, 5, 9, 13, 7]
    total = sum_list(numbers)
    assert total == 37


def test_sum_recursive():
    # Basic case
    numbers = [1, 2, 3, 4]
    assert sum_list_recursive(numbers) == 10

    # Empty list (special case)
    numbers = []
    assert sum_list_recursive(numbers) == 0

    # Single item in list (special case)
    numbers = [10]
    assert sum_list_recursive(numbers) == 10

    # Larger numbers
    numbers = [1000, 2000, 3000, 4000]
    assert sum_list_recursive(numbers) == 10000



