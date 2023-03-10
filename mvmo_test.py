import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
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


def test_transformation():
    # plt.show() commented
    mpl.use('TkAgg')

    x = [num / 100 for num in range(101)]

    # Effects of mean of dynamic population on the transformation function h
    y = [MVMO.transformation(random_xi, 0, si1=10, si2=10) for random_xi in x]
    y1 = [MVMO.transformation(random_xi, 0.25, si1=10, si2=10) for random_xi in x]
    y2 = [MVMO.transformation(random_xi, 0.5, si1=10, si2=10) for random_xi in x]
    y3 = [MVMO.transformation(random_xi, 0.75, si1=10, si2=10) for random_xi in x]
    y4 = [MVMO.transformation(random_xi, 1.0, si1=10, si2=10) for random_xi in x]

    assert all(0 <= v <= 1 for v in y)
    assert all(0 <= v <= 1 for v in y1)
    assert all(0 <= v <= 1 for v in y2)
    assert all(0 <= v <= 1 for v in y3)
    assert all(0 <= v <= 1 for v in y4)

    fig, ax = plt.subplots()
    ax.plot(x, y, "blue", label="mean_xi = 0")
    ax.plot(x, y1, "red", label="mean_xi = 0.25")
    ax.plot(x, y2, "green", label="mean_xi = 0.5")
    ax.plot(x, y3, "purple", label="mean_xi = 0.75")
    ax.plot(x, y4, "cyan", label="mean_xi = 1")
    ax.legend()
    plt.ylabel("xi")
    plt.xlabel("random x")
    plt.title("effects of mean of dynamic population on the transformation function \nfor shape si1 = si2 = 10")
    # plt.show()

    # Effects of shaping scaling factor on the transformation function h
    y = [MVMO.transformation(random_xi, 0.5, si1=0, si2=0) for random_xi in x]
    y1 = [MVMO.transformation(random_xi, 0.5, si1=5, si2=5) for random_xi in x]
    y2 = [MVMO.transformation(random_xi, 0.5, si1=10, si2=10) for random_xi in x]
    y3 = [MVMO.transformation(random_xi, 0.5, si1=15, si2=15) for random_xi in x]
    y4 = [MVMO.transformation(random_xi, 0.5, si1=50, si2=50) for random_xi in x]

    assert all(0 <= v <= 1 for v in y)
    assert all(0 <= v <= 1 for v in y1)
    assert all(0 <= v <= 1 for v in y2)
    assert all(0 <= v <= 1 for v in y3)
    assert all(0 <= v <= 1 for v in y4)

    fig, ax = plt.subplots()
    ax.plot(x, y, "blue", label="si1 = si2 = 0")
    ax.plot(x, y1, "red", label="si1 = si2 = 5")
    ax.plot(x, y2, "green", label="si1 = si2 = 10")
    ax.plot(x, y3, "purple", label="si1 = si2 = 15")
    ax.plot(x, y4, "cyan", label="si1 = si2 = 50")
    ax.legend()
    plt.ylabel("xi")
    plt.xlabel("random x")
    plt.title("effects of shaping scaling factor on the transformation function \nfor mean xi = 0.5")
    # plt.show()

    # Effects of different shape factors si1 =/= si2
    y = [MVMO.transformation(random_xi, 0.5, si1=10, si2=10) for random_xi in x]
    y1 = [MVMO.transformation(random_xi, 0.5, si1=10, si2=20) for random_xi in x]
    y2 = [MVMO.transformation(random_xi, 0.5, si1=20, si2=10) for random_xi in x]

    assert all(0 <= v <= 1 for v in y)
    assert all(0 <= v <= 1 for v in y1)
    assert all(0 <= v <= 1 for v in y2)

    fig, ax = plt.subplots()
    ax.plot(x, y, "green", label="si1 = si2 = 10", linestyle="--")
    ax.plot(x, y1, "red", label="si1 = 10, si2 = 20")

    ax.legend()
    plt.ylabel("xi")
    plt.xlabel("random x")
    plt.title("effects of different shape factors si1 =/= si2 \nfor mean xi = 0.5")
    # plt.show()

    fig, ax = plt.subplots()
    ax.plot(x, y, "green", label="si1 = si2 = 10", linestyle="--")
    ax.plot(x, y2, "red", label="si1 = 20, si2 = 10")

    ax.legend()
    plt.ylabel("xi")
    plt.xlabel("random x")
    plt.title("effects of different shape factors si1 =/= si2 \nfor mean xi = 0.5")
    # plt.show()


def test_count_si():
    optimizer = MVMO(10000, 100, 5, 3)
    last_no_zero_si = 20
    assert optimizer.count_si(0.5, 0.5, np.nan, last_no_zero_si)[0] == last_no_zero_si
    assert optimizer.count_si(0.5, 0.5, np.inf, last_no_zero_si)[0] == last_no_zero_si
