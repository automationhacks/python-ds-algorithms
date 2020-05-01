# List class does not hold any data itself
# But reference to node which actually holds data
# Reference: https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html#fig-node2


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

    def append(self, item):
        current = self.head
        temp = Node(item)

        while current.get_next() is not None:
            current = current.get_next()

        current.set_next(temp)

    def index(self, item):
        current = self.head
        index = 0
        found = False

        while current is not None and not found:
            if current.get_data() == item:
                found = True
                break
            else:
                current = current.get_next()
                index += 1

        if found:
            return index
        else:
            return 'Not Found'

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

    def insert(self, item, pos):
        node = Node(item)
        current = self.head
        previous = None
        index = 0

        while current.get_next() is not None:
            if index == pos:
                if previous is not None:
                    previous.set_next(node)
                    node.set_next(current)
                else:
                    node.set_next(current)
                    self.head = node
                return
            else:
                previous = current
                current = current.get_next()
                index += 1

        # If item is to be inserted at the last index
        previous.set_next(node)
        node.set_next(None)

    def pop(self):
        current = self.head
        previous = None

        while current.get_next() is not None:
            previous = current
            current = current.get_next()

        previous.set_next(None)
        return current.get_data()

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        # If item to be removed is first item
        if previous is None:
            self.head = current.get_next()
        else:
            # set link of previous to current items next
            # effectively removing the item from the list since no node points
            # to it
            previous.set_next(current.get_next())


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

    # Add items to list
    numbers.add(17)
    numbers.add(10)
    numbers.add(5)
    numbers.add(3)

    assert numbers.size() == 4

    # Search
    assert numbers.search(5)
    assert not numbers.search(100)

    # Remove item from list
    numbers.remove(10)
    assert numbers.size() == 3
    assert not numbers.search(10)

    # Remove last item from list
    numbers.remove(17)
    assert numbers.size() == 2
    assert not numbers.search(17)

    numbers.append(2)
    assert numbers.search(2)

    # Get index of an item
    assert numbers.index(5) == 1

    # Pop last item in the list
    prime = UnorderedList()
    prime.add(3)
    prime.add(5)
    prime.add(7)
    prime.add(11)
    item = prime.pop()
    assert item == 3
    assert not prime.search(3)

    # Insert at index
    person = UnorderedList()
    person.add("Rob")
    person.add("Joe")
    person.add("Margaret")
    person.add("Ramesh")

    person.insert("Satya", 0)
    assert person.index("Satya") == 0
    person.insert("Gaurav", 2)
    assert person.index("Gaurav") == 2
    last_index = person.size() - 1
    print(last_index)
    person.insert("Jay", last_index)
    assert person.search("Jay")
