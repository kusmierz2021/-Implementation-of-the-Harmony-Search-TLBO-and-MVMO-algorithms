import optimization_functions
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def test_rastrigins_function():
    # global maximum for different dimensions tested
    assert round(optimization_functions.rastrigins_function(np.array([4.52299])), 5) == 40.35329
    assert round(optimization_functions.rastrigins_function(np.array([4.52299, 4.52299])), 5) == 80.70658
    assert round(optimization_functions.rastrigins_function(np.array([4.52299, 4.52299, 4.52299])), 5) == 121.05987
    assert round(optimization_functions.rastrigins_function(np.array([4.52299, 4.52299, 4.52299,
                                                                      4.52299])), 5) == 161.41316
    assert round(optimization_functions.rastrigins_function(np.array([4.52299, 4.52299, 4.52299,
                                                                      4.52299, 4.52299])), 5) == 201.76645
    assert round(optimization_functions.rastrigins_function(np.array([4.52299, 4.52299, 4.52299,
                                                                      4.52299, 4.52299, 4.52299])), 5) == 242.11974
    assert round(optimization_functions.rastrigins_function(np.array([4.52299, 4.52299, 4.52299, 4.52299,
                                                                      4.52299, 4.52299, 4.52299])), 5) == 282.47303

    # plot Rastrigin's function (2D)
    # mpl.use('TkAgg')
    # x = np.linspace(-5.12, 5.12, 1000)
    # y = np.linspace(-5.12, 5.12, 1000)
    # x, y = np.meshgrid(x, y)
    # z = np.array([optimization_functions.rastrigins_function(np.array([x, y])) for x, y in zip(x, y)])
    #
    # ax = plt.axes(projection="3d")
    # ax.plot_surface(x, y, z, cmap="viridis")
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # ax.set_zlabel('f(x, y)')
    # ax.view_init(10, 10)
    # plt.title("Rastrigin's function (2D)")
    # plt.show()


def test_zakharov_function():
    # global minimum for different dimensions tested
    assert round(optimization_functions.zakharov_function(np.array([0, 0, 0, 0, 0, 0])), 2) == 0
    assert round(optimization_functions.zakharov_function(np.array([0, 0, 0, 0, 0])), 2) == 0
    assert round(optimization_functions.zakharov_function(np.array([0, 0, 0, 0])), 2) == 0
    assert round(optimization_functions.zakharov_function(np.array([0, 0, 0])), 2) == 0
    assert round(optimization_functions.zakharov_function(np.array([0, 0])), 2) == 0
    assert round(optimization_functions.zakharov_function(np.array([0])), 2) == 0

    # plot Zakharov function (2D)
    # mpl.use('TkAgg')
    # x = np.linspace(-5, 10, 1000)
    # y = np.linspace(-5, 10, 1000)
    # x, y = np.meshgrid(x, y)
    # z = np.array([optimization_functions.zakharov_function(np.array([x, y])) for x, y in zip(x, y)])
    #
    # ax = plt.axes(projection="3d")
    # ax.plot_surface(x, y, z, cmap="viridis")
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # ax.set_zlabel('f(x, y)')
    # ax.view_init(10, 10)
    # plt.title('Zakharov function (2D)')
    # plt.show()


def test_rosenbrock_function():
    # global minimum for different dimensions tested
    assert round(optimization_functions.rosenbrock_function(np.array([1, 1, 1, 1, 1, 1])), 2) == 0
    assert round(optimization_functions.rosenbrock_function(np.array([1, 1, 1, 1, 1])), 2) == 0
    assert round(optimization_functions.rosenbrock_function(np.array([1, 1, 1, 1])), 2) == 0
    assert round(optimization_functions.rosenbrock_function(np.array([1, 1, 1])), 2) == 0
    assert round(optimization_functions.rosenbrock_function(np.array([1, 1])), 2) == 0
    assert round(optimization_functions.rosenbrock_function(np.array([1])), 2) == 0

    # plot Rosenbrock's function (2D)
    # mpl.use('TkAgg')
    # x = np.linspace(-10, 10, 1000)
    # y = np.linspace(-10, 10, 1000)
    # x, y = np.meshgrid(x, y)
    # z = np.array([optimization_functions.rosenbrock_function(np.array([x, y])) for x, y in zip(x, y)])
    #
    # ax = plt.axes(projection="3d")
    # ax.plot_surface(x, y, z, cmap="viridis")
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # ax.set_zlabel('f(x, y)')
    # ax.view_init(10, 10)
    # plt.title('Zakharov function (2D)')
    # plt.show()


def test_expanded_schaffers_function():
    # global minimum for different dimensions tested
    assert round(optimization_functions.expanded_schaffers_function(np.array([0, 0, 0, 0, 0, 0])), 2) == 0
    assert round(optimization_functions.expanded_schaffers_function(np.array([0, 0, 0, 0, 0])), 2) == 0
    assert round(optimization_functions.expanded_schaffers_function(np.array([0, 0, 0, 0])), 2) == 0
    assert round(optimization_functions.expanded_schaffers_function(np.array([0, 0, 0])), 2) == 0
    assert round(optimization_functions.expanded_schaffers_function(np.array([0, 0])), 2) == 0

    # plot Expaned Schaffer's function (2D)
    # mpl.use('TkAgg')
    # x = np.linspace(-100, 100, 1000)
    # y = np.linspace(-100, 100, 1000)
    # x, y = np.meshgrid(x, y)
    # z = np.array([optimization_functions.expanded_schaffers_function(np.array([x, y])) for x, y in zip(x, y)])
    #
    # ax = plt.axes(projection="3d")
    # ax.plot_surface(x, y, z, cmap="viridis")
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # ax.set_zlabel('f(x, y)')
    # ax.view_init(10, 10)
    # plt.title("Expanded Schaffer's function (2D)")
    # plt.show()
