import numpy as np
from mvmo import MVMO


def test_init_population():
    optimizer = MVMO(10000, 100, 5, 3)
    population_1 = optimizer.init_population(3, 3)
    population_2 = optimizer.init_population(2, 10, -5.12, 5.12)

    assert len(population_1) == 3
    assert len(population_1[0]) == 3
    assert 0 <= population_1[0][0] <= 1
    assert 0 <= population_1[1][1] <= 1
    assert 0 <= population_1[2][2] <= 1

    assert len(population_2) == 10
    assert len(population_2[0]) == 2
    assert -5.12 <= population_2[0][0] <= 5.12
    assert -5.12 <= population_2[1][1] <= 5.12


def test__de_normalize_population():
    optimizer = MVMO(10000, 100, 5, 3)
    population = optimizer.init_population(2, 10, -5.12, 5.12)
    normalized_population = optimizer.normalize_population(population, -5.12, 5.12)
    denormalized_population = optimizer.denormalize_population(normalized_population, -5.12, 5.12)

    assert np.array_equal(denormalized_population, population)
    assert max([ind.max() for ind in normalized_population]) <= 1.0
    assert min([ind.min() for ind in normalized_population]) >= 0.0
