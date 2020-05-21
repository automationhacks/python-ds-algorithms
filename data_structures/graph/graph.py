from data_structures.graph.vertex import Vertex


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex

        return new_vertex

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, from_vertex, to_vertex, weight=0):
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)

        self.vertices[from_vertex].add_neighbor(self.vertices[to_vertex],
                                                weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())
