from typing import Callable
import math
import matplotlib.pyplot as plt


def left_rectangles(func: Callable, a: float, b: float, N=100):
    h = (b - a) / N

    integral_sum = 0
    for i in range(N):
        integral_sum += func(a + h * i) * h

    return integral_sum


def right_rectangles(func: Callable, a: float, b: float, N=100):
    h = (b - a) / N

    integral_sum = 0
    for i in range(N):
        integral_sum += func(a + h * (i + 1)) * h

    return integral_sum


def mid_rectangles(func: Callable, a: float, b: float, N=100):
    h = (b - a) / N

    integral_sum = 0
    for i in range(N):
        integral_sum += func(a + h * (i + 1 / 2)) * h

    return integral_sum


def trap_rectangles(func: Callable, a: float, b: float, N=100):
    h = (b - a) / N

    integral_sum = 0
    for i in range(N):
        integral_sum += (func(a + h * i) + func(a + h * (i + 1))) / 2 * h

    return integral_sum


if __name__ == '__main__':
    f = lambda x: math.cos(x)
    res = {'left':[],
           'right':[],
           'mid':[],
           'trap':[]}
    for n in range(10, 10000):
        res['left'].append(abs(1 - left_rectangles(f, 0, math.pi/2, N=n)))
        res['right'].append(abs(1 - right_rectangles(f, 0, math.pi/2, N=n)))
        res['mid'].append(abs(1 - mid_rectangles(f, 0, math.pi/2, N=n)))
        res['trap'].append(abs(1 - trap_rectangles(f, 0, math.pi/2, N=n)))


    for key in res:
        plt.plot(res[key], label=key)
    plt.legend()
    plt.show()