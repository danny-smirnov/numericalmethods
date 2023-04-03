from typing import Callable
import math


def bisection_method(func: Callable, left_border: float,
                     right_border: float, eps: float = 1e-4,
                     max_iter=1000, verbose=0):
    assert func(right_border) * func(left_border) <= 0, 'The root may not be found between the bounds'

    curr_iter = 0

    while right_border - left_border > eps and curr_iter < max_iter:
        mid_point = (right_border + left_border) / 2
        right_val = func(right_border)
        mid_val = func(mid_point)

        if right_val*mid_val <= 0:
            left_border = mid_point
        else:
            right_border = mid_point

        curr_iter += 1
        if verbose:
            print(f'{curr_iter} iteration: val = {mid_val}, interval_length = {right_border - left_border}')
    return (right_border + left_border)/2


def func(x):
    return math.cos(x)

if __name__ == '__main__':
    x_0 = bisection_method(func, -2, 1, verbose=1)
    print(x_0)
