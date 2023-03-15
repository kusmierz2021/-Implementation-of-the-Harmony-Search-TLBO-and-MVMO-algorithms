from evolutionary_algorithm import EvolutionaryAlgorithm
import numpy as np
from numpy.random import randint
from optimization_functions import rastrigins_function
from tqdm import tqdm
import random


class HS(EvolutionaryAlgorithm):
    def __init__(self, iterations: int, dimensions: int, boundaries: tuple[float, float], maximize: bool,
                 hmcr: float = None, par: float = None):
        # TODO: implement par parameter feature which seems to be optional
        """
        Harmony Search Algorithm
        :param iterations: number of iterations during optimization
        :type iterations: int
        :param dimensions: number of dimensions of optimization function
        :type dimensions: int
        :param boundaries: lower and higher limit of the range of every gene
        :type boundaries: tuple of floats
        :param maximize: True for maximization, False for minimization
        :type maximize: bool
        :param hmcr: ranges from 0.0 to 1.0
        :type hmcr: float
        :param par: ranges from 0.0 to 1.0, it is optional parameter
        :type par: float
        """
        super().__init__(iterations, dimensions, boundaries, maximize)
        self.hmcr = hmcr
        self.par = par

    def evaluation(self, population: list[np.ndarray], fitness_function: callable, child: np.ndarray):
        population = population + [child]
        best_population = sorted([(ind, fitness_function(ind)) for ind in population], key=lambda ind: ind[1],
                                 reverse=self.maximize).copy()[:len(population) - 1]
        return best_population

    def reproduction(self, population: list[np.ndarray]) -> np.ndarray:
        child = np.empty(self.dimensions, dtype=float)
        for ind in range(self.dimensions):
            if self.hmcr is not None:
                if random.random() > self.hmcr:
                    child[ind] = random.uniform(self.boundaries[0], self.boundaries[1])
                else:
                    child[ind] = population[randint(0, len(population))][ind]
        return child

    def optimize(self, population: list[np.ndarray], optimize_function: callable):
        best_individual = None
        for _ in tqdm(range(self.iterations)):

            child = self.reproduction(population)
            evaluated_population = self.evaluation(population, optimize_function, child)

            if best_individual is None:
                best_individual = evaluated_population[0]
            elif ((evaluated_population[0][1] > best_individual[1]) if self.maximize else (evaluated_population[0][1] < best_individual[1])):
                best_individual = evaluated_population[0]
                print(f"new best solution: {best_individual[0]} -> {best_individual[1]}")
            population = [ind[0] for ind in evaluated_population]


if __name__ == '__main__':
    boundaries = (-5.12, 5.12)
    optimizer = HS(10000, 6, boundaries, True, hmcr=0.9)
    population = optimizer.init_population(100)
    optimizer.optimize(population, rastrigins_function)
