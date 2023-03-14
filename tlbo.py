from evolutionary_algorithm import EvolutionaryAlgorithm
import numpy as np
from random import random, choice


class TLBO(EvolutionaryAlgorithm):
    def __init__(self, iterations: int, dimensions: int, boundaries: tuple[float, float], maximize: bool):
        """

        :param iterations:
        :type iterations:
        :param dimensions:
        :type dimensions:
        :param boundaries:
        :type boundaries:
        :param maximize:
        :type maximize:
        """
        super().__init__(iterations, dimensions, boundaries, maximize)

    def optimize(self, population: list[np.ndarray], optimize_function: callable):
        evaluated_mutated_population = self.mutation(population, optimize_function)
        return evaluated_mutated_population

    def mutation(self, population: list[np.ndarray], fitness_function: callable):

        evaluated_population, best_individual, mean_individual = self.evaluation(population, fitness_function)
        # TODO: Tf parameter missed in mutagen, for now Tf = 1 constantly
        mutagen = np.array([random() * (best - mean) for (best, mean) in zip(best_individual, mean_individual)])
        mutated_population = list(map(lambda ind: ind + mutagen, population))
        evaluated_mutated_population = self.evaluation(mutated_population, fitness_function)[0]

        if self.maximize:
            return [mutated_ind if mutated_ind[1] > ind[1] else ind for mutated_ind, ind
                    in zip(evaluated_mutated_population, evaluated_population)]
        else:
            return [mutated_ind if mutated_ind[1] < ind[1] else ind for mutated_ind, ind
                    in zip(evaluated_mutated_population, evaluated_population)]

    def evaluation(self, population: list[np.ndarray], fitness_function: callable):
        evaluated_population = [(ind, fitness_function(ind)) for ind in population]
        best_individual = sorted(evaluated_population, key=lambda ind: ind[1], reverse=self.maximize)[0][0]
        mean_individual = np.mean(population, axis=0)

        return evaluated_population, best_individual, mean_individual

    def crossover(self, evaluated_population: list[tuple[np.ndarray, float]]) -> list[np.ndarray]:
        crossed_population: list[np.ndarray] = []
        for ind in evaluated_population:
            while ind[1] == (ind_to_cross := choice(evaluated_population))[1]: pass

            if self.maximize:
                if ind[1] > ind_to_cross[1]:
                    new_ind = np.array([g1 + random() * (g1 - g2) for g1, g2 in zip(ind[0], ind_to_cross[0])])
                else:
                    new_ind = np.array([g1 + random() * (g2 - g1) for g1, g2 in zip(ind[0], ind_to_cross[0])])
            else:
                if ind[1] < ind_to_cross[1]:
                    new_ind = np.array([g1 + random() * (g1 - g2) for g1, g2 in zip(ind[0], ind_to_cross[0])])
                else:
                    new_ind = np.array([g1 + random() * (g2 - g1) for g1, g2 in zip(ind[0], ind_to_cross[0])])

            crossed_population.append(new_ind)
        return crossed_population


if __name__ == '__main__':
    boundaries = (-100, 100)
    optimizer = TLBO(1, 2, boundaries, False)
    population = optimizer.init_population(5)
    optimizer.optimize(population, lambda x: x[0]**2 + x[1]**2)
