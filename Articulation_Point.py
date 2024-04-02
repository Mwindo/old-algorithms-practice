from Graph.Graph_Stuff import Graph


def return_graph():
    g = Graph()
    g.add_edge("1", "4", 1, True)
    g.add_edge("1", "2", 1, True)
    g.add_edge("4", "3", 1, True)
    g.add_edge("2", "3", 1, True)
    g.add_edge("5", "3", 1, True)
    g.add_edge("6", "3", 1, True)
    # 3 is an articulation point
    return g


class ArticulationPoint:

    def __init__(self, g):
        self.DFS = []
        self.levels = {}
        self.graph = g

    def make_DFS_tree(self, v):
        if v not in self.DFS:
            self.DFS.append(v)
        if len(self.DFS) == len(self.graph.vertices):
            return
        for i in self.graph.efferent_edges(v):
            if i[0] not in self.DFS:
                self.DFS.append(i[0])
                self.make_DFS_tree(i[0])

    def min_level(self, v):
        if self.DFS.index(v) == 0:  # to ensure index > 0 otherwise
            return 0
        efferent = self.graph.efferent_edges(v)
        index = self.DFS.index(v)
        for i in [x[0] for x in efferent]:
            if self.DFS.index(i) < index and i != self.DFS[index-1]:
                return self.DFS.index(i)
        return self.min_level(self.DFS[self.DFS.index(v)+1])

    def get_levels(self):
        for i in self.DFS:
            self.levels[i] = self.min_level(i)

    def root_is_articulation_point(self):
        efferent = self.graph.efferent_edges(self.graph.root)
        if len(efferent) > 1:
            return True
        elif len(efferent) < 1:
            return False
        else:
            return efferent[0][0] != self.graph.root()

    def is_articulation_point(self, v):
        if self.graph.root() == v:
            return self.root_is_articulation_point()
        for i in self.graph.efferent_edges(v):
            if self.DFS.index(v) <= self.levels[i[0]]:
                return True

    def get_articulation_points(self):
        self.make_DFS_tree(self.graph.root())
        print(self.DFS)
        self.get_levels()
        ret = []
        for i in self.DFS:
            if self.is_articulation_point(i):
                ret.append(i)
        return ret


f = ArticulationPoint(return_graph())
print(f.get_articulation_points())
