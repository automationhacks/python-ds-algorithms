from data_structures.graph.graph import Graph


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        # Used to track discovery and finish_time
        self.time = 0

    def dfs(self):
        # Note: in self will call the __iter__ method
        # initializes all the vertices with white color
        for vertex in self:
            vertex.set_color('white')
            vertex.set_predecessor(-1)

        for vertex in self:
            if vertex.get_color() == 'white':
                self.dfs_visit(vertex)

    def dfs_visit(self, start_vertex):
        start_vertex.set_color('gray')
        self.time += 1
        start_vertex.set_discovery(self.time)

        for next_vertex in start_vertex.get_connections():
            if next_vertex.get_color() == 'white':
                next_vertex.set_predecessor(start_vertex)
                self.dfs_visit(next_vertex)

        start_vertex.set_color('black')
        self.time += 1
        start_vertex.set_finish_time(self.time)


