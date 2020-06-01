from data_structures.binary_heap.priority_queue import PriorityQueue


def dijkstra(graph, start):
    pq = PriorityQueue()
    start.set_distance(0)
    pq.build_heap([(vertex.get_distance(), vertex) for vertex in graph])

    while not pq.is_empty():
        current_vertex = pq.del_min()

        for next_vertex in current_vertex.get_connections():
            new_distance = current_vertex.get_distance() \
                           + current_vertex.get_weight(next_vertex)

            if new_distance < next_vertex.get_distance():
                next_vertex.set_distance(new_distance)
                next_vertex.set_predecessor(current_vertex)
                pq.decrease_key(next_vertex, new_distance)
