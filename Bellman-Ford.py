# Bellman-Ford


class Graph:

    def __init__(self):
        self.edge_dict = {}  # dictionary indexed by efferent node with value (target node, weight)
        self.vertices = []

    def add_edge(self, frm, to, weight):
        if frm not in self.vertices:
            self.vertices.append(frm)
        if to not in self.vertices:
            self.vertices.append(to)
        if frm not in self.edge_dict:
            self.edge_dict[frm] = [(to, weight)]
        else:
            self.edge_dict[frm].append((to, weight))

    def efferent_edges(self, node):
        if node not in self.edge_dict:
            return {}
        return self.edge_dict[node]

    def nodes(self):
        return self.vertices

    @classmethod
    def default(cls):
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
    def default_2(cls):
        g = cls()
        g.add_edge("1", "2", 2)
        g.add_edge("1", "3", 4)
        g.add_edge("2", "3", 1)
        g.add_edge("2", "4", 7)
        g.add_edge("3", "5", 3)
        g.add_edge("5", "4", 2)
        g.add_edge("4", "6", 1)
        g.add_edge("5", "6", 5)


def get_next_node(graph, visited):
    for i in graph.vertices:
        if i not in visited:
            return i
    return None


def bellman_ford(graph, start, end):
    weights = {}
    cur = start
    visited = [cur]
    for i in graph.nodes():  # initialize all weights to infinity
        weights[i] = float('inf')
    weights[start] = 0  # our start node has a distance of 0
    limit = len(graph.nodes()) - 1
    for i in range(0, limit):  # we need to repeat this V - 1 times
        change = False  # if no change in one iteration, then we can end
        for j in range(0, limit):  # get all the nodes
            for z in graph.efferent_edges(cur):  # so that we can get all the edges
                if weights[cur] + z[1] < weights[z[0]]:  # relaxation
                    weights[z[0]] = weights[cur] + z[1]
                    change = True
            cur = get_next_node(graph, visited)
            visited.append(cur)
        if change is False:
            return weights[end]
        cur = start  # repeat the process
        visited = [cur]
    return weights[end]


def dijkstra(graph, start, end):
    weights = {}
    cur = start
    visited = [cur]
    for i in graph.nodes():  # initialize all weights to infinity
        weights[i] = float('inf')
    weights[start] = 0  # our start node has a distance of 0
    limit = len(graph.nodes()) - 1
    for j in range(0, limit):  # get all the nodes
        for z in graph.efferent_edges(cur):  # so that we can get all the edges
            if weights[cur] + z[1] < weights[z[0]]:  # relaxation
                weights[z[0]] = weights[cur] + z[1]
        cur = get_next_node(graph, visited)
        visited.append(cur)
    return weights[end]


def test():
    x = bellman_ford(Graph.default(), "1", "7")
    print(x)


def test_2():
    x = dijkstra(Graph.default_2(), "1", "6")
    print(x)

test_2()
