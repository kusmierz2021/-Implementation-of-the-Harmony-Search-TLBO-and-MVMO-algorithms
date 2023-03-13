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


def rosenbrock_function(vec: np.ndarray) -> float:
    """

    :param vec: real numbers vector, usually includes numbers from [-5, 10]
    :type vec: numpy.ndarray
    :return: value of function
    :rtype: float
    """
    return sum([100 * (x1**2 - x2)**2 + (x2 - 1)**2 for x1, x2 in zip(vec[:-1], vec[1:])])


def expanded_schaffers_function(vec: np.ndarray) -> float:
    """

    :param vec: real numbers vector, usually includes numbers from [-100, 100]
    :type vec: numpy.ndarray
    :return: value of function
    :rtype: float
    """
    def schaffers_function(x: float, y: float) -> float:
        return 0.5 + (np.sin((x**2 + y**2))**2 - 0.5) / (1 + 0.001 * (x**2 + y**2))**2

    return sum([schaffers_function(vec[ind % len(vec)], vec[(ind+1) % len(vec)]) for ind in range(len(vec))])


def bent_cigar_function(vec: np.ndarray) -> float:
    """

        :param vec: real numbers vector, usually includes numbers from [-100, 100]
        :type vec: numpy.ndarray
        :return: value of function
        :rtype: float
    """
    return vec[0]**2 + 10**6 * sum(x**2 for x in vec[1:])


def levy_function(vec: np.ndarray) -> float:
    """

        :param vec: real numbers vector, usually includes numbers from [-10, 10]
        :type vec: numpy.ndarray
        :return: value of function
        :rtype: float
    """
    vec_w = 1 + (vec - 1) / 4
    return np.sin(math.pi * vec_w[0])**2 + (vec_w[-1] - 1)**2 * (1 + np.sin(2 * math.pi * vec_w[-1])**2) + sum([(wi-1)**2 * (1 + 10 * np.sin(math.pi * wi + 1)**2) for wi in vec_w[:-1]])


def high_conditioned_elliptic_function(vec: np.ndarray) -> float:
    """

        :param vec: real numbers vector, usually includes numbers from [-100, 100]
        :type vec: numpy.ndarray
        :return: value of function
        :rtype: float
    """
    d = len(vec)
    return sum([(10**6)**(i/(d-1)) * vec[i]**2 for i in range(d)])


def happycat_function(vec: np.ndarray) -> float:
    """

        :param vec: real numbers vector, usually includes numbers from [-20, 20]
        :type vec: numpy.ndarray
        :return: value of function
        :rtype: float
    """
    d = len(vec)
    return abs(sum([x**2 for x in vec]) - d)**(1/4) + (0.5 * sum([x**2 for x in vec]) + sum(vec)) / d + 0.5

