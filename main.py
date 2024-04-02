# Knuth-Morris-Pratt (KMP)

def make_table(pattern):
    pointer = 1
    cnd = 0
    t = [None] * (len(pattern)+1)
    t[0] = -1
    while pointer < len(pattern):
        if pattern[pointer] == pattern[cnd]:
            t[pointer] = t[cnd]
        else:
            t[pointer] = cnd
            while cnd >= 0 and pattern[pointer] != pattern[cnd]:
                cnd = t[cnd]
        pointer = pointer + 1
        cnd = cnd + 1
    t[pointer] = cnd
    print(t)
    return t


def KMP(pattern, searchstring):
    p = 0
    s = 0
    indices = []
    t = make_table(pattern)
    while s < len(searchstring):  # loop to the end of the search string
        if pattern[p] == searchstring[s]:  # if a match between current location of pattern and searchstring
            s += 1  # iterate the vars
            p += 1
            if p == len(pattern):  # if we have found a match across searchstring for every char in pattern
                indices.append(s-p)  # add the index of the current place in searchstring - the num chars in pattern
                p = t[p]  # now, jump based on the table; note that t[p] >= 0
        else:
            p = t[p]  # no match, so jump
            if p < 0:  # if jump goes back too far, increment
                s += 1
                p += 1
    return indices


print(KMP("aaa", "aaaabaanaan"))