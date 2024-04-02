from time import perf_counter
from abc import ABC, abstractmethod


class Board:

    @staticmethod
    def make_board(m, n):
        matrix = []
        for i in range(0, m):
            matrix.append([])
            for j in range(0, n):
                matrix[i].append(0)
        return matrix

    def __init__(self, m, n):
        self.board_matrix = Board.make_board(m, n)
        self.filled_spaces = 0
        self.total_spaces = len(self.board_matrix) * len(self.board_matrix[0])

    def mark_space(self, space):
        self.board_matrix[space[0]][space[1]] = self.filled_spaces + 1
        self.filled_spaces += 1

    def unmark_space(self, space):
        self.board_matrix[space[0]][space[1]] = 0
        self.filled_spaces -= 1

    def board_done(self):
        return self.filled_spaces == self.total_spaces

    def space_is_valid(self, space):
        if space[0] >= len(self.board_matrix) or space[0] < 0:  # number of rows = y component
            return False
        if space[1] >= len(self.board_matrix[0]) or space[1] < 0:  # number of columns = x component
            return False
        return self.board_matrix[space[0]][space[1]] == 0

    def num_rows(self):
        return len(self.board_matrix)

    def num_columns(self):
        return len(self.board_matrix[0])

    def num_spaces(self):
        return self.num_rows() * self.num_columns()


class Piece:

    def __init__(self, position):
        self.position = position
        self.start = position

    @abstractmethod
    def moves_from_position(self, board, position):
        pass


class Knight(Piece, ABC):

    @staticmethod
    def moves_from_pos(pos):
        moves = []  # I prefer the readability of this over initializing with values
        moves.append((pos[0] + 1, pos[1] + 2))
        moves.append((pos[0] + 1, pos[1] - 2))
        moves.append((pos[0] - 1, pos[1] + 2))
        moves.append((pos[0] - 1, pos[1] - 2))
        moves.append((pos[0] + 2, pos[1] + 1))
        moves.append((pos[0] + 2, pos[1] - 1))
        moves.append((pos[0] - 2, pos[1] + 1))
        moves.append((pos[0] - 2, pos[1] - 1))
        return moves

    @staticmethod
    def valid_moves_from_pos(board, pos):
        moves = Knight.moves_from_pos(pos)
        for i in reversed(range(0, len(moves))):
            if board.space_is_valid(moves[i]) is False:
                del moves[i]
        return moves

    @staticmethod
    def valid_moves_from_pos_sorted(board, pos):
        moves = Knight.valid_moves_from_pos(board, pos)
        return sorted(moves, key=lambda i: len(Knight.valid_moves_from_pos(board, i)))

    def moves_from_position(self, board, position):
        if board is None:
            return Knight.moves_from_pos(position)
        return Knight.valid_moves_from_pos_sorted(board, position)


class BoardTour:

    def __init__(self, board, piece):
        self.board = board
        self.piece = piece
        self.board.mark_space(piece.position)

    def tour_finished(self, closed=False):
        if not self.board.board_done():
            return False
        if not closed:
            return True
        return self.piece.start in self.piece.moves_from_position(None, self.piece.position)

    def solve(self, closed=False):
        if self.tour_finished(closed):
            return True
        start = self.piece.position
        for i in self.piece.moves_from_position(self.board, self.piece.position):
            self.piece.position = i
            self.board.mark_space(i)
            try_this = self.solve(closed)
            if try_this:
                return True
            self.board.unmark_space(i)
            self.piece.position = start
        return False

    def print(self):
        pos = []
        for i in range(1, self.board.num_spaces()+1):
            for a in range(0, self.board.num_rows()):
                for b in range(0, self.board.num_columns()):
                    if self.board.board_matrix[a][b] == i:
                        pos.append((a, b))
        for i in pos:
            print(i)


bo = Board(8, 8)
p = Knight((0, 0))
kt = BoardTour(bo, p)
t1 = perf_counter()
k = kt.solve(closed=True)
kt.print()
print(k)
t2 = perf_counter()
print(t2-t1)
