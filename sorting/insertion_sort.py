def insertion_sort(numbers):
    # Assume 1st item to be sorted sublist
    for index in range(1, len(numbers)):

        current_val = numbers[index]
        position = index

        # Decrement position by 1 till it becomes 0 and
        # check if item is greater than current item
        # if yes, shift the greater item to the right
        while position > 0 and numbers[position - 1] > current_val:
            numbers[position] = numbers[position - 1]
            position -= 1

        # Update the value in the newly made space
        numbers[position] = current_val
    return numbers


def test_insertion_sort():
    unsorted_numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sorted_numbers = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    assert insertion_sort(unsorted_numbers) == sorted_numbers
