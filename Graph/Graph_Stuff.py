from abc import ABC, abstractmethod
import random


class Graph:

    def __init__(self):
        self.edge_dict = {}  # dictionary indexed by efferent node with value (target node, weight)
        self.vertices = []

    def add_edge(self, frm, to, weight, bidirectional=False):
        if frm not in self.vertices:
            self.vertices.append(frm)
        if to not in self.vertices:
            self.vertices.append(to)
        if frm not in self.edge_dict:
            self.edge_dict[frm] = [(to, weight)]
        else:
            self.edge_dict[frm].append((to, weight))
        if bidirectional:
            self.add_edge(to, frm, weight)

    def efferent_edges(self, node):
        if node not in self.edge_dict:
            return {}
        return self.edge_dict[node]

    def nodes(self):
        return self.vertices

    def edges(self):
        return self.edge_dict

    @classmethod
    def default(cls):  # this won't work with Dijkstra
        g = cls()
        g.add_edge("1", "2", 6)
        g.add_edge("1", "3", 5)
        g.add_edge("1", "4", 5)
        g.add_edge("2", "5", -1)
        g.add_edge("3", "2", -2)
        g.add_edge("3", "5", 1)
        g.add_edge("4", "3", -2)
        g.add_edge("4", "6", -1)
        g.add_edge("5", "7", 3)
        g.add_edge("6", "7", 3)
        return g

    @classmethod
    def default_2(cls):  # this should work with Dijkstra
        g = cls()
        g.add_edge("1", "2", 2)
        g.add_edge("1", "3", 4)
        g.add_edge("2", "3", 1)
        g.add_edge("2", "4", 7)
        g.add_edge("3", "5", 3)
        g.add_edge("4", "6", 1)
        g.add_edge("5", "4", 2)
        g.add_edge("5", "6", 5)
        g.add_edge("7", "8", 7)
        return g

    def root(self):
        if len(self.vertices) == 0:
            return None
        return self.vertices[0]


class GraphAlgorithm(ABC):

    @abstractmethod
    def test(self):
        pass

    @abstractmethod
    def name(self):
        pass

    @staticmethod
    def run_one_test(actual, result, name):
        if actual != result:
            return False, "{0}: Failed. Got {1} but should have gotten {2}".format(name, result, actual)
        return True, "{0}: Success".format(name)


class Dijkstra(GraphAlgorithm):

    def set_distances(self, start):
        for i in self.graph.vertices:
            self.distances[i] = float('inf')
            self.unvisited.append(i)
        self.distances[start] = 0

    def __init__(self, graph):
        super().__init__()
        self.unvisited = []
        self.distances = {}
        self.graph = graph

    def get_node_with_smallest_tentative_distance(self):
        if len(self.unvisited) == 0:
            return None
        m = self.unvisited[0]
        for i in self.unvisited:
            if self.distances[i] < self.distances[m]:
                m = i
        return m

    def run(self, start, end):
        if start not in self.graph.vertices or end not in self.graph.vertices:
            return float('inf')
        self.set_distances(start)
        cur = start
        while end in self.unvisited and len(self.unvisited) > 0:
            for i in self.graph.efferent_edges(cur):
                if i[0] in self.unvisited:
                    tentative = i[1] + self.distances[cur]
                    if tentative < self.distances[i[0]]:
                        self.distances[i[0]] = tentative
            self.unvisited.remove(cur)
            cur = self.get_node_with_smallest_tentative_distance()
        return self.distances[end]

    @staticmethod
    def test():
        d = Dijkstra(Graph.default_2())
        m1 = GraphAlgorithm.run_one_test(9, d.run("1", "6"), "Test start and end connected")
        m2 = GraphAlgorithm.run_one_test(float('inf'), d.run("1", "7"), "Test start and end unconnected")
        m3 = GraphAlgorithm.run_one_test(0, d.run("1", "1"), "Test start = end")
        m4 = GraphAlgorithm.run_one_test(float('inf'), d.run("1", "100"), "Test end does not exist")
        m5 = GraphAlgorithm.run_one_test(float('inf'), d.run("100", "1"), "Test start does not exist")
        for i in [m1, m2, m3, m4, m5]:
            if not i[0]:
                return i[1]
            print("  ", i[1])
        return " All tests passed"

    @staticmethod
    def name():
        return "Dijkstra's Algorithm"


def ret_massive_undirected_graph(connected=True):
    g = Graph()
    for i in range(0, 1000):
        for j in range(i, 1000):
            x = random.randint(0, 2)
            if connected and j == i+1:  # easy way to ensure connected graph
                x = 0
            if x == 0:
                w = random.randint(0, 1000)
                g.add_edge(str(i), str(j), w, bidirectional=True)
    return g


def test_all():
    a = [Dijkstra]
    for i in a:
        print("---", i.name(), "---")
        print(i.test())
