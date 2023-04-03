from typing import List, Union
from typing import SupportsFloat as Numeric


class Matrix:
    def __init__(self, base: List[List[float]]):
        self.rows = len(base)
        if isinstance(base[0], list):
            self.cols = len(base[0])
            for row in base:
                assert len(row) == self.cols, 'Invalid dimensionality'
        elif isinstance(base[0], Numeric):
            self.cols = 1
            for num in base:
                assert isinstance(num, Numeric), 'Invalid elements in vector'
        self.matrix = base

    def __getitem__(self, index):
        if isinstance(index, tuple):
            row, col = index
            if isinstance(row, slice) and isinstance(col, int):
                return Matrix([[self.matrix[i][col] for i in range(row.start or 0, row.stop or self.rows, row.step or 1)]]).T
            elif isinstance(row, int) and isinstance(col, slice):
                return self.matrix[row][col]
            elif isinstance(row, slice) and isinstance(col, slice):
                rowed = self.matrix[row]
                return Matrix([rowed[i][col] for i in range(row.start or 0, row.stop or self.rows, row.step or 1)])
            else:
                return self.matrix[row][col]
        elif isinstance(index, int):
            if self.rows == 1:
                return self.matrix[0][index]
            else:
                return Matrix([self.matrix[index]])
        else:
            raise TypeError("Invalid argument type")

    def __setitem__(self, index, value):

        if isinstance(index, tuple):
            row, col = index
            if isinstance(row, slice) and isinstance(col, int):
                for i, v in zip(range(row.start or 0, row.stop or self.rows, row.step or 1), value):
                    self.matrix[i][col] = v
            elif isinstance(row, int) and isinstance(col, slice):
                self.matrix[row][col] = value
            else:
                self.matrix[row][col] = value
        elif isinstance(index, int):
            self.matrix[index] = value.matrix[0]
        else:
            raise TypeError("Invalid argument type")

    @property
    def T(self):
        return Matrix([list(x) for x in zip(*self.matrix)])

    def __add__(self, other: 'Matrix'):
        assert (self.rows, self.cols) == (other.rows, other.cols), 'Impossible to add matrices of different dimensions'
        return Matrix([[v1 + v2 for v1, v2 in zip(a, b)] for a, b in zip(self.matrix, other.matrix)])

    def __sub__(self, other: 'Matrix'):
        assert (self.rows, self.cols) == (other.rows, other.cols), 'Impossible to add matrices of different dimensions'
        return Matrix([[v1 - v2 for v1, v2 in zip(a, b)] for a, b in zip(self.matrix, other.matrix)])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __truediv__(self, divisor):
        if isinstance(divisor, Numeric):
            return self.__mul__(1/divisor)

    def __mul__(self, other: Union['Matrix', Numeric]):
        # by constant
        if isinstance(other, Numeric):
            return Matrix([[other * a for a in row] for row in self.matrix])

        elif isinstance(other, Matrix):
            assert self.cols == other.rows, 'Matrix cannot be multiplied'
            return Matrix([[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*other.matrix)] \
                           for A_row in self.matrix])
        else:
            raise TypeError(f'unsupported operand type for *: {type(other)}')

    def __rmul__(self, other: Union['Matrix', Numeric]):
        if isinstance(other, Numeric):
            return self.__mul__(other)
        else:
            raise TypeError(f'unsupported operand type for *: {type(other)}')

    def concat(self, other: 'Matrix', axis=0):
        if axis == 0:
            assert self.cols == other.cols, 'Invalid Dimensionality'
            return Matrix(self.matrix + other.matrix)
        elif axis == 1:
            assert self.rows == other.rows, 'Invalid Dimensionality'
            return Matrix([a + b for a, b in zip(self.matrix, other.matrix)])
        else:
            raise AttributeError('Wrong axis')

    def twist(self):
        return Matrix([a[::-1] for a in self.matrix][::-1])


if __name__ == '__main__':
    m = Matrix([[1, 2, 3], [5, 2, 1]])
    print(m.twist())



