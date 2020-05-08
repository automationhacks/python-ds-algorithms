def selection_sort(alist):
    for fill_slot in range(len(alist) - 1, 0, -1):

        position_of_max = 0

        for location in range(1, fill_slot + 1):

            # find location of max value
            if alist[location] > alist[position_of_max]:
                position_of_max = location

        # exchange the last value with the max value item
        temp = alist[fill_slot]
        alist[fill_slot] = alist[position_of_max]
        alist[position_of_max] = temp 


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(alist)
print('After sorting {}'.format(alist))
