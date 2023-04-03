from typing import Callable


def simple_iteration(func: Callable, eps: float = 1e-4,
                     max_iter=100, initial_point=1 + 1e-4,
                     verbose: float = 0):
    """ Simple Iteration method for finding roots of the functional x=phi(x)

    Convergence conditions of the method:
    1) |phi'(x_n)| < 1, where x_n - value at current interation
    2) |phi'(x*)| = 0, where x* - real root of the functional

    Stopping criterion - |(X_{n+1} - X_{n}) / (1 - (X_{n+1} - X_{n})/(X_{n} - X_{n-1}))| < eps
    Assumed that |phi'(x_n)| = q (q < 1) that criterion can reflect the real error

    :param func: callable function
    :param eps: error
    :param max_iter: number of iterations
    :param initial_point: any point where function is defined
    :param verbose: intermediate steps are printed, in case the variable is not equal to zero
    :return: point: x*
    """

    curr_iter = 0

    x0 = initial_point
    x1 = func(x0)
    x2 = func(x1)

    criterion = abs((x2 - x1) / (1 - (x2 - x1) / (x1 - x0)))

    while curr_iter < max_iter and criterion > eps:
        new_val = func(x2)
        x0, x1, x2 = x1, x2, new_val
        criterion = abs((x2 - x1) / (1 - (x2 - x1) / (x1 - x0)))
        curr_iter += 1

        if verbose:
            print(f'{curr_iter} iteration: curr_point: {x2}, relative_error: {criterion}')

    return x2


def root_to_find(a):
    def wrapper(func):
        def inner(*args, **kwargs):
            return func(a, *args, **kwargs)
        return inner
    return wrapper


@root_to_find(5)
def square_root_functional(a, x):
    """
    Functional for the method of simple iterations, helping to find the root of a number

    x = sqrt(a)
    x^2 = a
    2x^2 = x^2+a
    x = 1/2(x+a/x)

    This functional guarantees the convergence of the method, since the derivative of the functional is equal to zero:
        x = sqrt(a)
        phi'(x) = 1/2(1-a/x^2)
        phi'(sqrt(a)) = 1/2(1-a/a) = 0

    """
    return 1/2*(x + a/x)

if __name__ == '__main__':
    print(simple_iteration(square_root_functional, verbose=1, eps=1e-6))

