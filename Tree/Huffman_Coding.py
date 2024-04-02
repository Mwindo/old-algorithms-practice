# Huffman coding
# I think get_encoding can be done more efficiently, but I need to move on

# take in a string and return a frequency table (sorted ascending)
def get_frequency_table(m):
    d = dict()
    for i in range(0, len(m)):
        letter = m[i]
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
    d = dict(sorted(d.items(), key=lambda item: item[1]))
    return d


# from a tuple (representing a graph branch left right), get the original letters
# e.g. (b, (a, c)) is a graph with left node b, right node (a,c), which itself has left node a, right node b
# so we would return b, a, c
def get_bases(key, t):
    if isinstance(key, tuple):
        return get_bases(key[0], t) + get_bases(key[1], t)
    else:
        return key


# take in a frequency table (sorted ascending) and return a tree represented as nested tuples
def huffman_tree(d):
    while len(d) > 1:
        m1 = min(d, key=d.get)  # get the node with the minimum frequency
        v1 = d[m1]
        del d[m1]  # remove this node
        m2 = min(d, key=d.get)  # get the node with the minimum frequency (i.e. the next smallest node)
        v2 = d[m2]
        del d[m2]  # remove this node
        d[(m1, m2)] = v1 + v2  # consolidate the two removed nodes, placing them as one node in the dict
    return list(d.keys())[0]  # all that remains in the dictionary is the root node, so return that


# given a tree represented as a nested tuple, return a dictionary key as original letter, value as Huffman code
def get_encoding(tree, encoding):
    if isinstance(tree, tuple):  # while still a tuple (i.e. not an original letter)
        for i in get_bases(tree[0], tree):  # get the original letters from the left side
            encoding[i] = "0" + encoding[i]
        for i in get_bases(tree[1], tree):  # get the original letters from the right side
            encoding[i] = "1" + encoding[i]
        for i in tree:  # recurse over the children nodes
            encoding = get_encoding(i, encoding)
    return encoding


# returns the a dictionary where keys are letters in the message, values are Huffman codes
def huffman(m):
    d = get_frequency_table(m)
    encoding = {}
    for i in d:
        encoding[i] = ""
    tree = huffman_tree(d)
    return get_encoding(tree, encoding)


# Huffman coding guarantees that sum(2^(-l_i)) = 1 for l_i the message length of letter i
# so we check that this is the case with the message; if not, the function huffman is wrong
def check_Kraft_inequality(message):
    encoding = huffman(message)
    should_be_one = 0
    for i in encoding.values():
        should_be_one += 2 ** (-1 * len(i))
    if should_be_one == 1:
        return True
    return False


def test():
    message1 = "This is a test of Huffman encoding"
    message2 = "abbbbbce"
    message3 = "Blah blagh blah"
    messages = [message1, message2, message3]
    for i in messages:
        if not check_Kraft_inequality(i):
            return False
    return True
