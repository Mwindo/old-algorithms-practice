import random


class RandomString:

    def __init__(self, max_length, fixed_length=False):
        self.max_length = max_length
        if fixed_length:
            self.length = max_length
        else:
            self.length = -1
        self.str = ""

    def __generate_length(self):
        r = random.randint(1, self.max_length)
        return r

    def generate(self):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                    "j", "k", "l", "m", "n", "o", "p", "q", "r",
                    "s", "t", "u", "v", "w", "x", "y", "z"]
        if self.length < 0:
            self.length = self.__generate_length()
        for i in range(0, self.length):
            r = random.randint(0, 25)
            self.str += alphabet[r]
        return self.str


class LongestCommonSubsequence:

    @staticmethod
    def init_matrix(str1, str2):
        m = len(str1)
        n = len(str2)
        matrix = []
        for i in range(0, m+1):
            matrix.append([])
            for j in range(0, n+1):
                matrix[i].append(0)
        return matrix

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.matrix = LongestCommonSubsequence.init_matrix(str1, str2)

    def solve(self):
        for i in range(1, len(self.str1) + 1):
            for j in range(1, len(self.str2) + 1):
                self.matrix[i][j] = self.update_matrix(i, j)
        n = len(self.str2)
        ret_me = ""
        for i in reversed(range(1, len(self.str1)+1)):
            if self.matrix[i][n] != self.matrix[i-1][n]:
                ret_me = self.str1[i-1] + ret_me
                n -= 1
        return ret_me

    def update_matrix(self, i1, i2):
        if i1 == 0 or i2 == 0:
            return 0
        if self.str1[i1-1] == self.str2[i2-1]:
            return 1 + self.matrix[i1-1][i2-1]
        else:
            return max(self.matrix[i1-1][i2], self.matrix[i1][i2-1])


def calc_expected_value(d):
    tot = 0
    for i in d:
        tot += d[i]
    e = 0
    for i in d:
        e += i * d[i]/tot
    return e


def test(n, z):
    s = {}
    for i in range(0, n+1):
        s[i] = 0
    for i in range(0, z):
        x = RandomString(n, True).generate()
        y = RandomString(n, True).generate()
        # print("String 1 ({0}): {1}".format(len(x), x))
        # print("String 2 ({0}): {1}".format(len(y), y))
        k = LongestCommonSubsequence(x, y)
        b = k.solve()
        # print("Longest Common Subsequence ({0}): {1}".format(len(b), b))
        s[len(b)] += 1
        # print(k.matrix)
    print(s)
    print(calc_expected_value(s))


# fun problem: relationship between size of strings, number of letters, and expected value
# for alphabet of 26 letters, linear relationship: ~ 2.9183x + b

