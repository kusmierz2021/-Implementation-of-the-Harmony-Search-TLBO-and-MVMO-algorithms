from evolutionary_algorithm import EvolutionaryAlgorithm
import numpy as np
from numpy.random import randint
from optimization_functions import rastrigins_function


class HS(EvolutionaryAlgorithm):
    def __init__(self, iterations: int, dimensions: int, boundaries: tuple[float, float], hmcr: float = None,
                 par: float = None):
        super().__init__(iterations, dimensions, boundaries)
        self.hmcr = hmcr
        self.par = par

    def evaluation(self, population: list[np.ndarray], fitness_function: callable, child: np.ndarray):
        population = population + [child]
        best_population = sorted([(ind, fitness_function(ind)) for ind in population], key=lambda ind: ind[1], reverse=True).copy()[:len(population) - 1]
        return best_population

    def reproduction(self, population: list[np.ndarray]) -> np.ndarray:
        child = np.empty(self.dimensions, dtype=float)
        for ind in range(self.dimensions):
            child[ind] = population[randint(0, len(population))][ind]
        return child

    def optimize(self, population: list[np.ndarray]):

        pass

if __name__ == '__main__':
    boundaries = (-5.12, 5.12)
    optimizer = HS(10000, 6, boundaries)
    population = optimizer.init_population(5)
    child = optimizer.reproduction(population)
    for ind in population:
        print(ind)

    print('\n')
    print('\n')
    print(child)
    print('\n')
    print('\n')
    population = optimizer.evaluation(population, rastrigins_function, child)
    for ind in population:
        print(ind)

