# Hamiltonian cycle

def add_edge(matrix, row, column, bidirectional=True):
    matrix[row][column] = 1
    if bidirectional:
        matrix[column][row] = 1


def make_adjacency_matrix():
    mat = []
    for i in range(0, 5):
        mat.append([])
        for j in range(0, 5):
            mat[i].append(0)
    add_edge(mat, 0, 1)
    add_edge(mat, 0, 2)
    add_edge(mat, 0, 4)
    add_edge(mat, 1, 2)
    add_edge(mat, 1, 3)
    add_edge(mat, 1, 4)
    add_edge(mat, 2, 3)
    add_edge(mat, 3, 4)
    return mat


def nodes_are_connected(matrix, node1, node2):
    return matrix[node1][node2] == 1


# pass matrix and list of nodes
# empty list will give duplicates
# single item in list will give all cycles with no duplicates
def Hamiltonian(matrix, nodes):
    # print(nodes)
    if len(nodes) == len(matrix):
        if nodes_are_connected(matrix, nodes[0], nodes[len(nodes)-1]):
            return True
        else:
            return False
    for i in range(0, len(matrix)):
        if i not in nodes and nodes_are_connected(matrix, nodes[len(nodes)-1], i):
            nodes.append(i)
            if Hamiltonian(matrix, nodes):
                print(nodes)
            nodes.remove(i)
    return False


Hamiltonian(make_adjacency_matrix(), [0])



