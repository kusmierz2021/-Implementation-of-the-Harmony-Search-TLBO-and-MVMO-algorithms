from hs import HS
from optimization_functions import rastrigins_function
import numpy as np

    # def reproduction(self, population: list[np.ndarray]) -> np.ndarray:
    #     offspring = np.empty(self.dimensions, dtype=float)
    #     for ind in range(self.dimensions):
    #         offspring[ind] = population[randint(0, len(population))][ind]
    #     return offspring

def test_reproduction():
    dimensions = 6
    boundaries = (-5.12, 5.12)
    optimizer = HS(10000, dimensions, boundaries)
    population = optimizer.init_population(5)
    child = optimizer.reproduction(population)

    assert len(child) == dimensions
    assert all(boundaries[0] <= gene <= boundaries[1] for gene in child)


