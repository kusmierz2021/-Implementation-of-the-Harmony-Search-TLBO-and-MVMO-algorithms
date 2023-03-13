from evolutionary_algorithm import EvolutionaryAlgorithm
import numpy as np
from numpy.random import randint
from optimization_functions import rastrigins_function
from tqdm import tqdm

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

    def optimize(self, population: list[np.ndarray], optimize_function: callable):
        best_individual = None
        for _ in tqdm(range(self.iterations)):

            child = self.reproduction(population)
            evaluated_population = self.evaluation(population, optimize_function, child)

            if best_individual is None:
                best_individual = evaluated_population[0]
            elif evaluated_population[0][1] > best_individual[1]:
                best_individual = evaluated_population[0]
                print(f"new best solution: {best_individual[0]} -> {best_individual[1]}")
            population = [ind[0] for ind in evaluated_population]


if __name__ == '__main__':
    boundaries = (-5.12, 5.12)
    optimizer = HS(10000, 6, boundaries)
    population = optimizer.init_population(10_000)
    optimizer.optimize(population, rastrigins_function)

