from typing import Callable
import numdifftools as nd
from sympy import symbols, zeros, diff
import math

def newton(func: Callable, eps: float = 1e-4,
           max_iter=1000, initial_point=1 + 1e-4,
           verbose: float = 0):
    """ Newton's method for finding the roots of the functional

    Convergence conditions of the method:
    1) |phi'(x_n)| < 1, where x_n - value at current interation
    2) |phi'(x*)| = 0, where x* - real root of the functional

    Stopping criterion - |(X_{n+1} - X_{n}) / (1 - (X_{n+1} - X_{n})/(X_{n} - X_{n-1}))| < eps
    Assumed that |phi'(x_n)| = q (q < 1) that criterion can reflect the real error

    To find the derivative, a package of numerical calculations is used

    :param func: callable function
    :param eps: error
    :param max_iter: number of iterations
    :param initial_point: any point where function is defined
    :param verbose: intermediate steps are printed, in case the variable is not equal to zero
    :return: point: x*
    """

    def next_step(x):
        return x - func(x)/nd.Derivative(func, 1)(x)

    curr_iter = 2

    x0 = initial_point
    x1 = next_step(x0)
    x2 = next_step(x1)

    criterion = abs((x2 - x1) / (1 - (x2 - x1) / (x1 - x0)))

    best_criterion = criterion
    best_x = x2

    while curr_iter < max_iter and criterion > eps:
        new_val = next_step(x2)
        x0, x1, x2 = x1, x2, new_val
        criterion = abs((x2 - x1) / (1 - (x2 - x1) / (x1 - x0)))
        curr_iter += 1

        if criterion < best_criterion:
            best_criterion = criterion
            best_x = x2

        if verbose:
            print(f'{curr_iter} iteration: curr_point: {x2}, relative_error: {criterion}')
    if curr_iter == max_iter:
        print(f'Method did not converge, best guess: {best_x}')
        return best_x
    return x2




if __name__ == '__main__':
    # f = lambda x: (x-1)*(x-2)**2*(x-3)**3
    f = lambda x: math.exp(x) - 2
    print(newton(f, eps=0.01, verbose=1, initial_point=-2))
