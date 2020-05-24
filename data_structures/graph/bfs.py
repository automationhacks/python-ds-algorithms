from data_structures.queue.queue import Queue


def bfs(graph, start):
    start.set_distance(0)
    start.set_predecessor(None)
    vertex_queue = Queue()
    vertex_queue.enqueue(start)

    while vertex_queue.size() > 0:
        current_vertex = vertex_queue.dequeue()
        for nbr in current_vertex.get_connections():
            if nbr.get_color() == 'white':
                nbr.set_color('gray')
                nbr.set_distance(current_vertex.get_distance() + 1)
                nbr.set_predecessor(current_vertex)
                vertex_queue.enqueue(nbr)
        current_vertex.set_color('black')


def traverse(vertex):
    temp = vertex

    while temp.get_predecessor():
        print(temp.get_id())
        temp = temp.get_predecessor()
    print(temp.get_id())


