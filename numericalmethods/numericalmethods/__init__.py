"""Top-level package for NumericalMethods."""

__author__ = """Smirnov Daniil """
__email__ = 'danu90_2016@mail.ru'
__version__ = '0.1.0'


from optimization_methods.bisection_method import bisection
from optimization_methods.simple_iteration_method import simple_iteration
from optimization_methods.newtons_method import newton

__all__ = [bisection, simple_iteration, newton]
