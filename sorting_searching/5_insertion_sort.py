def insertion_sort(alist):

    # Assume 1st item to be sorted sublist
    for index in range(1, len(alist)):

        # Take one item at a time
        current_val = alist[index]
        # Get current position
        position = index

        # Decrement position by 1 till it becomes 0 and
        # check if item is greater than current item
        # if yes, shift the greater item to the right
        while position > 0 and alist[position - 1] > current_val:
            alist[position] = alist[position - 1]
            position -= 1

        # Update the value in the newly made space
        alist[position] = current_val


alist = [34, 56, 23, 67, 234, 456, 45]
insertion_sort(alist)
print(alist)
