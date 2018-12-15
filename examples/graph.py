import math


class Vertex:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Vertex2D(Vertex):
    def __init__(self, name, x, y):
        self.__x = x
        self.__y = y
        super().__init__(name)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


class Edge:
    def __init__(self, name, source, destination):
        self.__name = name
        self.__source = source
        self.__destination = destination

    def get_name(self):
        return self.__name

    def get_length(self):
        return math.sqrt(
            (self.__source.get_x() - self.__destination.get_x()) ** 2
            + (self.__source.get_y() - self.__destination.get_y()) ** 2
        )


class Graph:
    def __init__(self, vertices, edges):
        self.__vertices = vertices
        self.__edges = edges

    def get_vertices(self):
        return self.__vertices

    def get_edges(self):
        return self.__edges

    def add_vertex(self, vertex):
        pass

    def add_edge(self, edge):
        pass

    def has_edge(self, source, destination):
        pass


class GraphVertexIterator:
    def __init__(self, graph):
        self.__graph = graph

        self.__visited = set()
        self.__not_visited = set(graph.get_vertices())

        self.__current = self.__not_visited.pop()

    def get_current(self):
        return self.__current

    def go_next(self):
        self.__visited.add(self.__current)

        if not self.__not_visited:
            self.__current = None
            return None

        self.__current = self.__not_visited.pop()

    def is_stopped(self):
        return self.__current is None


vertices = [
    Vertex2D('a', 0, 5),
    Vertex2D('b', 5, 0),
    Vertex2D('c', 0, 0),
    Vertex2D('d', 123, 123),
    Vertex2D('e', 123, 124),
]

edges = [
    Edge('a -> b', vertices[0], vertices[1]),
    Edge('b -> c', vertices[1], vertices[2]),
    Edge('c -> a', vertices[2], vertices[0]),
]

graph = Graph(
    vertices,
    edges,
)

graph_iterator = GraphVertexIterator(graph)

while not graph_iterator.is_stopped():
    v = graph_iterator.get_current()
    print(v.get_name())
    graph_iterator.go_next()
