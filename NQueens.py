class NQueensSolver:

    def make_matrix(self):
        ret = []
        for i in range(0, self.n):
            ret.append([])
            for j in range(0, self.n):
                ret[i].append(0)
        return ret

    def __init__(self, n):
        self.n = n
        self.matrix = self.make_matrix()
        self.solutions = []

    def is_on_diagonal(self, column_pos, columns_pos):
        cur_column = len(columns_pos)
        if cur_column == 0:
            return False
        for i in range(1, cur_column+1):
            if columns_pos[cur_column-i] == column_pos - i:
                return True
            if columns_pos[cur_column-i] == column_pos + i:
                return True
        return False

    def is_valid_position(self, column_pos, columns_pos):
        if column_pos in columns_pos:
            return False
        if self.is_on_diagonal(column_pos, columns_pos):
            return False
        return True

    def solve(self, columns_pos=None):
        if columns_pos is None:
            columns_pos = []
        if len(columns_pos) == self.n:
            return True
        for i in range(0, self.n):
            if self.is_valid_position(i, columns_pos):
                columns_pos.append(i)
                t = self.solve(columns_pos)
                if t:
                    self.solutions.append(columns_pos.copy())
                columns_pos.remove(i)
        return False


q = NQueensSolver(8)
q.solve()
print(len(q.solutions), "solutions")
print(q.solutions)
