class BaseList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

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

    def pop(self):
        current = self.head
        previous = None

        while current.get_next() is not None:
            previous = current
            current = current.get_next()

        previous.set_next(None)
        return current.get_data()