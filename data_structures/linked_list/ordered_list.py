from data_structures.linked_list.base_list import BaseList
from data_structures.linked_list.node import Node


class OrderedList(BaseList):
    def __init__(self):
        super().__init__()

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            # Make use of sorted property to stop traversal early
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        node = Node(item)
        # if item has to be inserted in first position
        # i.e. previous is None, reset head to new item
        if previous is None:
            node.set_next(self.head)
            self.head = node
        # Normal case: prev to item, item to current
        else:
            previous.set_next(node)
            node.set_next(current)


def test_ordered_list_addition():
    numbers = OrderedList()
    numbers.add(17)
    numbers.add(20)
    numbers.add(3)
    numbers.add(5)

    assert numbers.index(3) == 0
