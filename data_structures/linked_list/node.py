# List class does not hold any data itself
# But reference to node which actually holds data
# Reference: https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html#fig-node2


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


