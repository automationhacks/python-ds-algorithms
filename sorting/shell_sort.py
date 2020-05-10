def shell_sort(items):
    sub_list_count = len(items) // 2

    while sub_list_count > 0:
        for start_position in range(sub_list_count):
            insertion_sort_with_gap(items, start_position, sub_list_count)

        print(
            f'After increment of size: {sub_list_count} the list is {items}')

        # Reducing the gap by a factor of 2
        sub_list_count = sub_list_count // 2

    return items


def insertion_sort_with_gap(items, start, gap):
    # Init loop from start position + gap until total items and step using gap
    for i in range(start + gap, len(items), gap):
        position = i
        # Store the current value
        current_value = items[i]

        # Gr than eq is important here.
        # If item on pos - gap is greater than current value, then continue
        while position >= gap and items[position - gap] > current_value:
            # Shift items by gap
            items[position] = items[position - gap]
            # Reduce the position with gap
            position -= gap

        # Finally, insert the current item at the last position
        items[position] = current_value


def test_shell_sort():
    before = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    after = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    assert shell_sort(before) == after
