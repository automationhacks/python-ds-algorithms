# YouTube: https://www.youtube.com/watch?v=SvG5L6nILyg&feature=youtu.be&list=PLtbC5OfOR8aqfexTOHSzvdQhfCzp0mZ64
# Book: https://runestone.academy/runestone/books/published/pythonds/BasicDS/WhatIsaDeque.html


class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def add_front(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop()

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_rear(self):
        return self.items.pop(0)


def test_operations():
    deque = Deque()
    assert deque.is_empty()
    deque.add_front('dog')
    deque.add_front('cat')
    assert deque.items == ['dog', 'cat']
    deque.add_rear(8.4)
    assert deque.items == [8.4, 'dog', 'cat']
    deque.add_rear(124)
    assert deque.items == [124, 8.4, 'dog', 'cat']
    removed = deque.remove_front()
    assert removed == 'cat'
    removed = deque.remove_rear()
    assert removed == 124
    assert deque.items == [8.4, 'dog']


if __name__ == '__main__':
    test_operations()
