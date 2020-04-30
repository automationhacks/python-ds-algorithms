# List class does not hold any data itself
# But reference to node which actually holds data


class UnorderedList:
    def __init__(self):
        # head points to first item in list
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        # add item to first item (i.e. head)
        # reset head to point to the new first item in the list
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found


class Node:
    def __init__(self, data):
        # data stored in the node
        self.data = data
        # reference to next node in the list
        # if None, then it means we are on the last node of the list
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


def test_list_operations():
    numbers = UnorderedList()
    numbers.add(17)
    numbers.add(10)
    numbers.add(5)
    numbers.add(3)

    assert numbers.size() == 4
    assert numbers.search(5)
    assert not numbers.search(100)
