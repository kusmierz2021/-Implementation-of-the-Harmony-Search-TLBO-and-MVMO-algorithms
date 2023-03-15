from evolutionary_algorithm import EvolutionaryAlgorithm
import numpy as np
from random import random, choice
from tqdm import tqdm


class TLBO(EvolutionaryAlgorithm):
    def __init__(self, iterations: int, dimensions: int, boundaries: tuple[float, float], maximize: bool):
        """
        Teaching Learning Based Optimization Algorithm
        :param iterations: number of iterations during optimization
        :type iterations: int
        :param dimensions: number of dimensions of optimization function
        :type dimensions: int
        :param boundaries: lower and higher limit of the range of every gene
        :type boundaries: tuple of floats
        :param maximize: True for maximization, False for minimization
        :type maximize: bool
        """
        super().__init__(iterations, dimensions, boundaries, maximize)

    def optimize(self, population: list[np.ndarray], optimize_function: callable):
        best_individual = self.evaluation(population, optimize_function)[1]
        print(f"new best: {best_individual} -> {optimize_function(best_individual)}")

        for _ in tqdm(range(self.iterations)):
            evaluated_mutated_population = self.mutation(population, optimize_function)
            population = self.crossover(evaluated_mutated_population, optimize_function)
            potential_best_individual = self.evaluation(population, optimize_function)[1]

            if (optimize_function(potential_best_individual) > optimize_function(best_individual)) if self.maximize \
                    else (optimize_function(potential_best_individual) < optimize_function(best_individual)):
                best_individual = potential_best_individual
                print(f"new best: {best_individual} -> {optimize_function(best_individual)}")

    def mutation(self, population: list[np.ndarray], fitness_function: callable):

        evaluated_population, best_individual, mean_individual = self.evaluation(population, fitness_function)
        mutation_rate = round((random()+1))
        mutagen = np.array([random() * (best - mutation_rate * mean) for (best, mean)
                            in zip(best_individual, mean_individual)])
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

    def crossover(self, evaluated_population: list[tuple[np.ndarray, float]], fitness_function: callable) -> list[np.ndarray]:
        crossed_population: list[np.ndarray] = []
        for ind in evaluated_population:
            # TODO: caused endless loop
            # while ind[1] == (ind_to_cross := choice(evaluated_population))[1]: pass
            for _ in range(100_000):
                if ind[1] != (ind_to_cross := choice(evaluated_population))[1]:
                    break

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

            new_ind = new_ind if ((fitness_function(new_ind) > ind[1] and self.maximize) or ((fitness_function(new_ind) < ind[1] and not self.maximize))) else ind[0]
            new_ind = np.array([self.boundaries[0] if gene < self.boundaries[0] else
                                (self.boundaries[1] if gene > self.boundaries[1] else gene) for gene in new_ind])

            crossed_population.append(new_ind)
        return crossed_population


if __name__ == '__main__':
    boundaries = (-100, 100)
    optimizer = TLBO(1, 2, boundaries, False)
    population = optimizer.init_population(5)
    optimizer.optimize(population, lambda x: x[0]**2 + x[1]**2)
