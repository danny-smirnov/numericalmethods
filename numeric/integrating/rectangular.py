from typing import Callable
import math


def left_rectangles(func: Callable, a: float, b: float, eps=1e-4):
    N = 100
    h = (b - a) / N

    integral_sum = 0
    for i in range(N):
        integral_sum += func(a + h * i) * h

    return integral_sum


def right_rectangles(func: Callable, a: float, b: float, eps=1e-4):
    N = 100
    h = (b - a) / N

    integral_sum = 0
    for i in range(N):
        integral_sum += func(a + h * (i+1)) * h

    return integral_sum




if __name__=='__main__':

    f = lambda x: math.cos(x)
    print(math.pi/2)
    print(left_rectangles(f, 0, math.pi/2))