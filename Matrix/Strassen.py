def ret_matrix():
    return [[1, 1, 0, 0], [0, 1, 0, 0], [10, 0, 1, 0], [0, 0, 0, 1]]


def ret_new_square_matrix(n):
    c = []
    for i in range(0, n):
        c.append([])
        for j in range(0, n):
            c[i].append(0)
    return c


def divide_matrix(m, n):
    ret1 = []
    ret2 = []
    ret3 = []
    ret4 = []
    for i in range(0, n):
        ret1.append([])
        ret2.append([])
        for j in range(0, n):
            ret1[i].append(m[i][j])
        for j in range(n, n*2):
            ret2[i].append(m[i][j])
    for i in range(n, n*2):
        ret3.append([])
        ret4.append([])
        for j in range(0, n):
            ret3[i-n].append(m[i][j])
        for j in range(n, n*2):
            ret4[i-n].append(m[i][j])
    return ret1, ret2, ret3, ret4


def add_matrices(m1, m2):
    n = len(m1)
    c = ret_new_square_matrix(n)
    for i in range(0, n):
        for j in range(0, n):
            c[i][j] = m1[i][j] + m2[i][j]
    return c


def strassen(m1, m2):
    n = len(m1)
    c = ret_new_square_matrix(n)
    if n == 2:
        p = (m1[0][0] + m1[1][1]) * (m2[0][0] + m2[1][1])
        q = (m1[1][0] + m1[1][1]) * m2[0][0]
        r = m1[0][0] * (m2[0][1] - m2[1][1])
        s = m1[1][1] * (m2[1][0] - m2[0][0])
        t = (m1[0][0] + m1[0][1]) * m2[1][1]
        u = (m1[1][0] - m1[0][0]) * (m2[0][0] + m2[0][1])
        v = (m1[0][1] - m1[1][1]) * (m2[1][0] + m2[1][1])
        c[0][0] = p + s - t + v
        c[0][1] = r + t
        c[1][0] = q + s
        c[1][1] = p + r - q + u
        return c
    else:
        mid = int(n / 2)
        a = divide_matrix(m1, mid)
        print(a)
        b = divide_matrix(m2, mid)
        c0 = add_matrices(strassen(a[0], b[0]), strassen(a[1], b[2]))
        c1 = add_matrices(strassen(a[0], b[1]), strassen(a[1], b[3]))
        c2 = add_matrices(strassen(a[2], b[0]), strassen(a[3], b[2]))
        c3 = add_matrices(strassen(a[2], b[1]), strassen(a[3], b[3]))
        print(c0)
        print(c1)
        print(c2)
        print(c3)
        for i in range(0, mid):
            c[0][i] = c0[0][i]
            c[0][i+mid] = c1[0][i]
            c[1][i] = c0[1][i]
            c[1][i+mid] = c1[1][i]
            c[2][i] = c2[0][i]
            c[2][i+mid] = c3[0][i]
            c[3][i] = c2[1][i]
            c[3][i+mid] = c3[1][i]
        return c


print(strassen(ret_matrix(), ret_matrix()))


