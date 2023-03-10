from mvmo import MVMO


def test_init_population():
    optimizer = MVMO(10000, 100, 5, 3)
    population_1 = optimizer.init_population(3, 3)
    population_2 = optimizer.init_population(2, 10, 0.12, 5.12)

    assert len(population_1) == 3
    assert len(population_1[0]) == 3
    assert 0 <= population_1[0][0] <= 1
    assert 0 <= population_1[1][1] <= 1
    assert 0 <= population_1[2][2] <= 1

    assert len(population_2) == 10
    assert len(population_2[0]) == 2
    assert -5.12 <= population_2[0][0] <= 5.12
    assert -5.12 <= population_2[1][1] <= 5.12