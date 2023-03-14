import numpy as np
from tlbo import TLBO
from optimization_functions import rastrigins_function


def test_mutation():
    dimensions = 2
    boundaries = (-5.12, 5.12)
    sphere_function = lambda x: x[0] ** 2 + x[1] ** 2
    optimizer = TLBO(1, dimensions, boundaries, maximize=False)
    population = optimizer.init_population(5)
    mutated_population = optimizer.mutation(population, sphere_function)

    assert len(mutated_population) == len(population)
    assert len(mutated_population[0]) == len(population[0]) == dimensions

def test_evaluation():
    dimensions = 2
    boundaries = (-5.12, 5.12)
    sphere_function = lambda x: x[0] ** 2 + x[1] ** 2
    optimizer = TLBO(1, dimensions, boundaries, maximize=False)
    population = optimizer.init_population(5)
    evaluated_population, best_individual, mean_individual = optimizer.evaluation(population, sphere_function)

    assert len(best_individual) == dimensions
    assert len(mean_individual) == dimensions
    assert all(sphere_function(best_individual) <= ind[1] for ind in evaluated_population)


    optimizer = TLBO(1, dimensions, boundaries, maximize=True)
    population = optimizer.init_population(5)
    evaluated_population, best_individual, mean_individual = optimizer.evaluation(population, rastrigins_function)

    assert len(best_individual) == dimensions
    assert len(mean_individual) == dimensions
    assert all(rastrigins_function(best_individual) >= ind[1] for ind in evaluated_population)
