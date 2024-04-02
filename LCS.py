# Longest subsequences

A = ["A", "B", "C", "D"]
B = ["A", "C", "B", "A", "D"]


def find_last_match(array, x, start):
    for i in reversed(range(0, start)):
        if x == array[i]:
            return i
    return -1


def a_appears_before_b(array, a, b, start):
    a_index = find_last_match(array, a, start)
    b_index = find_last_match(array, b, start)
    print("index", a, ":", a_index)
    print("index", b, ":", b_index)
    return a_index < b_index


def LCSLength(X, Y):
    print(len(X), len(Y))
    C = [[0 for x in range(len(Y))] for y in range(len(X))]
    print(C)
    for i in range(0, len(X)):
        C[i][0] = 0
    for i in range(0, len(Y)):
        C[0][i] = 0
    for i in range(0, len(X)):
        for j in range(0, len(Y)):
            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C[len(X)-1][len(Y)-1]


def LCSMatrix(X, Y):
    print(len(X), len(Y))
    C = [[0 for x in range(len(Y))] for y in range(len(X))]
    print(C)
    for i in range(0, len(X)):
        C[i][0] = 0
    for i in range(0, len(Y)):
        C[0][i] = 0
    for i in range(0, len(X)):
        for j in range(0, len(Y)):
            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C


def LCS(C, A, B, x, y):
    if x == 0 or y == 0:
        return ""
    if A[x-1] == B[y-1]:
        return LCS(C, A, B, x-1, y-1) + A[x-1]
    elif C[x][y-1] > C[x-1][y]:
        return LCS(C, A, B, x, y-1)
    else:
        return LCS(C, A, B, x-1, y)


print(LCS(LCSMatrix(A, B), A, B, len(A), len(B)))
