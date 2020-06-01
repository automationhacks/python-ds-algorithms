import pytest


class PriorityQueue:
    def __init__(self):
        # Init list with 0, which is not used
        # This makes it easier for integer division

        self.heap_list = [(0, 0)]
        self.current_size = 0

    def add(self, item):
        self.heap_list.append(item)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def is_empty(self):
        return self.current_size == 0

    def __contains__(self, item):
        for pair in self.heap_list:
            if pair[1] == item:
                return True

        return False

    def decrease_key(self, key, weight):
        # item in heap are of the form (2, 'x) i.e. value followed
        # by the key
        # We use this if we want to remove the value
        done = False
        index = 1
        my_key = 0

        # Find key in heap
        while not done and index <= self.current_size:
            if self.heap_list[index][1] == key:
                done = True
                my_key = index
            else:
                index += 1

        # If key is found in heap then update the weight
        # and percolate the key up to the appropriate position in
        # the heap
        if my_key > 0:
            key_in_heap = self.heap_list[my_key][1]
            self.heap_list[my_key] = (weight, key_in_heap)
            self.percolate_up(my_key)

    def percolate_up(self, idx):
        while idx // 2 > 0:
            parent_idx = idx // 2

            if self.heap_list[idx][0] < self.heap_list[parent_idx][0]:
                temp = self.heap_list[parent_idx]
                self.heap_list[parent_idx] = self.heap_list[idx]
                self.heap_list[idx] = temp

            idx = idx // 2

    def find_min(self):
        return self.heap_list[1]

    def del_min(self):
        current_min = self.heap_list[1][1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolate_down(1)

        return current_min

    def percolate_down(self, idx):
        while idx * 2 <= self.current_size:
            mc = self.min_child(idx)

            if self.heap_list[idx][0] > self.heap_list[mc][0]:
                temp = self.heap_list[idx]
                self.heap_list[idx] = self.heap_list[mc]
                self.heap_list[mc] = temp

            idx = mc

    def min_child(self, idx):
        l_child = 2 * idx
        r_child = (2 * idx) + 1

        if l_child > self.current_size:
            return -1
        else:
            # Avoiding IndexError
            if r_child > self.current_size:
                return l_child
            else:
                if self.heap_list[l_child][0] < self.heap_list[r_child][0]:
                    return l_child
                else:
                    return r_child

    def build_heap(self, alist):
        self.current_size = len(alist)
        self.heap_list = [(0, 0)]

        for item in alist:
            self.heap_list.append(item)

        mid = len(alist) // 2
        while mid > 0:
            self.percolate_down(mid)
            mid -= 1


@pytest.fixture
def heap():
    heap = PriorityQueue()
    heap.add((2, 'x'))
    heap.add((3, 'y'))
    heap.add((5, 'z'))
    heap.add((6, 'a'))
    heap.add((4, 'd'))
    yield heap


def test_insert(heap):
    assert heap.current_size == 5


def test_del_min(heap):
    assert heap.del_min() == 'x'
    assert heap.del_min() == 'y'


def test_dec_key(heap):
    heap.decrease_key('d', 1)
    assert heap.del_min() == 'd'
