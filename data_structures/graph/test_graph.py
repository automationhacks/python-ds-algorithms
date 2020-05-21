from data_structures.graph.graph import Graph


def test_graph():
    graph = Graph()
    for num in range(6):
        graph.add_vertex(num)

    print(graph.vertices)

    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 5, 2)
    graph.add_edge(1, 2, 4)
    graph.add_edge(2, 3, 9)
    graph.add_edge(3, 4, 7)
    graph.add_edge(3, 5, 3)
    graph.add_edge(4, 0, 1)
    graph.add_edge(5, 4, 8)
    graph.add_edge(5, 2, 1)

    for vertex in graph:
        for connection in vertex.get_connections():
            print(f"{vertex.get_id()} connected to {connection.get_id()}")

