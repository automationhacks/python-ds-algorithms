import sys


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}  # adjacency list
        self.color = 'white'
        self.distance = sys.maxsize
        self.predecessor = None
        # Below tracks the no of steps in the algorithm before a vertex is
        # first encountered
        self.discovery = 0
        # Below tracks the no of steps before a vertex is colored black
        self.finish_time = 0

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_predecessor(self, predecessor):
        self.predecessor = predecessor

    def get_predecessor(self):
        return self.predecessor

    def set_discovery(self, discovery_time):
        self.discovery = discovery_time

    def get_discovery(self):
        return self.discovery

    def set_finish(self, finish_time):
        self.finish_time = finish_time

    def get_finish(self):
        return self.finish_time

    def get_connections(self):  # list of vertices connected to
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def __str__(self):
        connected_vertices = [connection.id for connection in self.connected_to]
        return f"{str(self.id)} connected to {str(connected_vertices)}"
