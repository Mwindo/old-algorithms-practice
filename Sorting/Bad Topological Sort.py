# Topological Sort

import random


def get_DAC():  # directed acyclic graph where key is node and value is list of nodes pointing to it
    retMe = {}
    for i in reversed(range(0, 30)):
        retMe[i] = []
        for j in range(0, i):
            num = random.randint(1, 4)
            if num == 4:
                retMe[i].append(j)
    # retMe = {2: [3], 3: [5, 6], 1: [2, 5], 5:[], 6:[]}
    return retMe


def node_and_ancestors(dic, node, array):
    array = all_ancestor_nodes(dic, node, node, [])
    array.append(node)
    return array


def all_ancestor_nodes(dic, orNode, curNode, array):
    if orNode in array:  # we've looped back
        return array
    if curNode not in dic:
        print("Error:", curNode, "not in dic")
    if len(dic[curNode]) < 1:
        return array
    for i in dic[curNode]:
        if i not in array:
            array.append(i)
        ancestors = all_ancestor_nodes(dic, orNode, i, array)
        for j in ancestors:
            if j not in array:
                array.append(j)
    return array


def is_DAC(dic):
    for i in dic:
        ancestors = all_ancestor_nodes(dic, i, i, [])
        if i in ancestors:
            return False
    return True


def free_nodes(dic):
    ret = []
    for i in dic:
        if len(dic[i]) < 1:
            ret.append(i)
    return ret


def nodes_dependent_on_x(x, dic):
    ret = []
    for i in dic:
        if x in dic[i]:
            ret.append(i)
    return ret


def topological_sort(dic):
    L = []
    S = free_nodes(dic)
    while len(S) > 0:
        n = S[0]
        L.append(n)
        del S[0]
        for i in nodes_dependent_on_x(n, dic):
            dic[i].remove(n)
            if len(dic[i]) < 1:
                S.append(i)
    return L


def test_DAC():
    d = get_DAC()
    for i in d:
        print(i)
        print("------")
        for j in d[i]:
            print(j)
        print("======")
    #for i in topological_sort(d):
    #     print(i)


def test():
    d = get_DAC()
    print(d)
    for i in topological_sort(d):
        print(i)


test()


# could implement Brent's algorithm for cycle detection here, actually
