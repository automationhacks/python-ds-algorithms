# https://www.youtube.com/watch?v=RHfngV3DpBU&list=PLtbC5OfOR8aqfexTOHSzvdQhfCzp0mZ64&index=7


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        # Treating the first item in the list as the rear
        self.items.insert(0, item)

    def dequeue(self):
        # Remove item from the end of the list
        return self.items.pop()

    def size(self):
        return len(self.items)
