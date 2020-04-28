from data_structures.queue.queue import Queue


# You have a group of people
# One person is holding a hot potato
# Each turn the person passes the potato to the person in the left
# Then the person gives the potato to his left and then leaves

def play_hot_potato_game(items, reps):
    queue = Queue()

    # O(n)
    for item in items:
        queue.enqueue(item)

    # O(n - 1)
    while queue.size() > 1:
        # O(#reps,
        for i in range(reps):
            first = queue.dequeue()
            print(first)

            queue.enqueue(first)
        print('-' * 10)
        print('Removing {}'.format(queue.dequeue()))

    return queue.dequeue()


if __name__ == "__main__":
    people = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    num = 5
    print('Winner is: {}'.format(play_hot_potato_game(people, num)))

