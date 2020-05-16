class BinaryHeap:
    def __init__(self):
        # Init list with 0, which is not used
        # This makes it easier for integer division

        self.heap_list = [0]
        self.current_size = 0

    def insert(self, item):
        self.heap_list.append(item)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def percolate_up(self, idx):
        while idx // 2 > 0:
            parent_idx = idx // 2

            if self.heap_list[idx] < self.heap_list[parent_idx]:
                temp = self.heap_list[parent_idx]
                self.heap_list[parent_idx] = self.heap_list[idx]
                self.heap_list[idx] = temp

            idx = idx // 2

    def find_min(self):
        return self.heap_list[1]

    def del_min(self):
        current_min = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()

        self.percolate_down(1)
        return current_min

    def percolate_down(self, idx):
        while idx * 2 <= self.current_size:
            mc = self.min_child(idx)

            if self.heap_list[idx] > self.heap_list[mc]:
                temp = self.heap_list[idx]
                self.heap_list[idx] = self.heap_list[mc]
                self.heap_list[mc] = temp

            idx = mc

    def min_child(self, idx):
        l_child = 2 * idx
        r_child = l_child + 1

        # Avoiding IndexError
        if r_child > self.current_size:
            return l_child

        if self.heap_list[l_child] > self.heap_list[r_child]:
            return r_child
        else:
            return l_child

    def build_heap(self, alist):
        mid = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist

        while mid > 0:
            self.percolate_down(mid)
            mid -= 1


def test_binary_heap_creation():
    binary_heap = BinaryHeap()
    binary_heap.build_heap([9, 5, 6, 2, 3])

    print()
    print(binary_heap.del_min())
    print(binary_heap.del_min())
    print(binary_heap.del_min())
    print(binary_heap.del_min())
    print(binary_heap.del_min())
