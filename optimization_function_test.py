import optimization_functions
import numpy as np


def test_rastrigins_function():
    assert round(optimization_functions.rastrigins_function(np.array([4.52299])), 5) == 40.35329
    assert round(optimization_functions.rastrigins_function(np.array([4.52299, 4.52299])), 5) == 80.70658
    assert round(optimization_functions.rastrigins_function(np.array([4.52299, 4.52299, 4.52299])), 5) == 121.05987
