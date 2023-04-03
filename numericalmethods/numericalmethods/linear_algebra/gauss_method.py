from matrix import Matrix
from typing import Union, List


def gauss_forward(A: Matrix):
    # search for the first non-zero element
    first_row = 0
    while A[first_row][0] == 0:
        first_row += 1

    assert first_row < A.rows, 'Extra variable'

    if first_row != 0:
        A[first_row], A[0] = A[0], A[first_row]
    for diagonal_elem in range(min(A.rows, A.cols)):
        for row_idx in range(diagonal_elem, A.rows-1):

            coef = A[row_idx + 1][diagonal_elem] / A[diagonal_elem][diagonal_elem]
            A[row_idx + 1] = A[row_idx + 1] - A[diagonal_elem] * coef
        A[diagonal_elem] = A[diagonal_elem] / A[diagonal_elem][diagonal_elem]
    return A


def gauss(A:Matrix, b:'Matrix'):
    assert A.cols == A.rows, 'Matrix is not squared'
    system = A.concat(b.T, axis=1)
    upper = gauss_forward(system).twist()
    assert A[A.cols-1][A.cols-1] != 0, 'Singular matrix'
    upper = upper[:, 1:].concat(upper[:, 0], axis=1)
    e_x = gauss_forward(upper)
    return e_x[:, -1].twist()

if __name__ == '__main__':
    A = Matrix([[0, 2, 3], [3, 4, 5], [6, 7, 8]])
    b = Matrix([[5, 5, 5]])
    print(gauss(A, b))
