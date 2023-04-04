from numeric.linear_algebra.matrix import Matrix
from numeric.linear_algebra.gauss_method import gauss
from typing import List
import numpy as np
import matplotlib.pyplot as plt



class Interpol1d:
    def __init__(self, x: List[float], y: List[float], kind='poly'):
        assert len(x) == len(y), 'Invalid lengths of arrays'
        self.x = x
        self.y = y
        self.kind = kind

    def _get_coefs(self):
        if self.kind == 'poly':
            # solving system of linear equations with phi_k(x) = x^k as base functions
            self.coefs = self.__poly_solver()

    def __poly_solver(self):
        vandermonde = Matrix([[1] * len(self.x)]).T
        x_vec = Matrix([self.x]).T
        for pow in range(1, len(vandermonde)):
            vandermonde = vandermonde.concat(vandermonde[:, -1].hadamard_prod(x_vec), axis=1)
        return gauss(vandermonde, Matrix([self.y])).matrix

    def __call__(self, point):
        if not hasattr(self, 'coefs'):
            self._get_coefs()
        return sum([c[0] * point ** i for i, c in enumerate(self.coefs)])


if __name__ == '__main__':
    x = [1, 2, 3, 6, -6]
    y = [2, 5, 6, 6, 0]
    f = Interpol1d(x, y, 'poly')
    pts = np.linspace(min(x)-1, max(x)+1, 100)
    plt.plot(x, y, 'ro', label='points')
    plt.plot(pts, f(pts), label='interpolation polynom')
    plt.legend()
    plt.show()
