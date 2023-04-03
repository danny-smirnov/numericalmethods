from typing import List, Union
from typing import SupportsFloat as Numeric


class Matrix:
    def __init__(self, base: List[List[float]]):
        self.rows = len(base)
        self.cols = len(base[0])
        for row in base:
            assert len(row) == self.cols, 'Invalid dimensionality'
        self.matrix = base

    @property
    def T(self):
        return Matrix([list(x) for x in zip(*self.matrix)])

    def __add__(self, other: 'Matrix'):
        assert (self.rows, self.cols) == (other.rows, other.cols), 'Impossible to add matrices of different dimensions'
        return Matrix([[v1 + v2 for v1, v2 in zip(a, b)] for a, b in zip(self.matrix, other.matrix)])

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


if __name__ == '__main__':
    m = Matrix([[1, 2, 3], [4, 5, 6]])

    res = m * m.T
    print(res.matrix)
