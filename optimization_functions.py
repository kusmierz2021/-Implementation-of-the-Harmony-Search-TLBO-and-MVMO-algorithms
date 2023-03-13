import math
import numpy as np


def rastrigins_function(vec: np.ndarray) -> float:
    """
    :param vec: real numbers vector, includes numbers from [-5,12, 5,12]
    :return: value of function
    """
    return sum([x**2 - 10 * np.cos(2 * math.pi * x) + 10 for x in vec])


def zakharov_function(vec: np.ndarray) -> float:
    """

    :param vec: real numbers vector, usually includes numbers from [-5, 10]
    :type vec: numpy.ndarray
    :return: value of function
    :rtype: float
    """
    return sum([x**2 for x in vec]) + sum([0.5 * x for x in vec])**2 + sum([0.5 * x for x in vec])**4
