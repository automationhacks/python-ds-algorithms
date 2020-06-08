def shell_sort(items):
    # Choosing mid point as the gap
    gap = len(items) // 2

    while gap > 0:
        for start_pos in range(gap):
            insertion_sort_with_gap(items, start_pos, gap)

        print(f'After increment of size: {gap} the list is {items}')

        # Reducing the gap by a factor of 2
        gap = gap // 2

    return items


def insertion_sort_with_gap(sublist, start, gap):
    # Init loop from start position + gap until total items and step using gap
    for i in range(start + gap, len(sublist), gap):
        # Below is insertion sort logic
        position = i
        # Store the current value
        current_value = sublist[i]

        # Gr than eq is important here.
        # If item on pos - gap is greater than current value, then continue
        while position >= gap and sublist[position - gap] > current_value:
            # Shift items by gap
            sublist[position] = sublist[position - gap]
            # Reduce the position with gap
            position -= gap

        # Finally, insert the current item at the last position
        sublist[position] = current_value


def test_shell_sort():
    before = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    after = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    assert shell_sort(before) == after
