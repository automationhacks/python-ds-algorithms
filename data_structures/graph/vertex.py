class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}  # adjacency list

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_connections(self):  # list of vertices connected to
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def __str__(self):
        connected_vertices = [connection.id for connection in self.connected_to]
        return f"{str(self.id)} connected to {str(connected_vertices)}"
