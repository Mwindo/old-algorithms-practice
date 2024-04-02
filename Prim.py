# a naive implementation of Prim

from Graph import Graph_Stuff


def ret_test_graph():
    g = Graph_Stuff.Graph()
    g.add_edge("1", "2", 28, bidirectional=True)
    g.add_edge("1", "6", 10, bidirectional=True)
    g.add_edge("2", "3", 16, bidirectional=True)
    g.add_edge("2", "7", 14, bidirectional=True)
    g.add_edge("3", "4", 12, bidirectional=True)
    g.add_edge("4", "5", 22, bidirectional=True)
    g.add_edge("4", "7", 18, bidirectional=True)
    g.add_edge("5", "6", 25, bidirectional=True)
    g.add_edge("5", "7", 24, bidirectional=True)
    # g.add_edge("8", "9", 3, bidirectional=True)
    return g


def get_min_connected_edge(g, used_vertices, used_vert_dict):
    m = float('inf')
    edge = None
    for i in used_vertices:
        for j in g.efferent_edges(i):
            if used_vert_dict[j[0]] is False and j[1] < m:
                m = j[1]
                edge = (i, j[0])
    return edge


# in this implementation:
# used_vertices is here to avoid looping over all vertices
# used_vert_dict is used to quickly check if a vertex has already been mapped rather than use "in used_vertices"
def Prim(g):
    edges = []
    v = [g.vertices[0]]
    used_dict = {}
    for i in g.vertices:
        used_dict[i] = False
    while len(edges) < len(g.vertices)-1:
        cur = get_min_connected_edge(g, v, used_dict)
        if cur is None:
            print("Disconnected Graph!")
            return edges
        v.append(cur[1])
        edges.append(cur)
    return edges


def test():
    g = ret_test_graph()
    x = Prim(g)
    print(x)


test()
