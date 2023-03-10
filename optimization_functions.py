import math
import numpy


def rastrigins_function(vec: numpy.ndarray) -> float:
    """
    :param vec: real numbers vector, includes numbers from [-5,12, 5,12]
    :return: value of function
    """
    return sum([x**2 - 10 * math.cos(2 * math.pi * x) + 10 for x in vec])
