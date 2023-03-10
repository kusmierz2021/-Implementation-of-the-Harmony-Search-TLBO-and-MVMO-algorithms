import numpy as np
import math


class MVMO:
    def __init__(self, iterations: int, population_size: int, dimensions: int, num_mutation: int,
                 shaping_scaling_factor_fs=1.0, asymmetry_factor_af=1.0, init_val_shape_factor_sd=75.0):
        self.iterations = iterations
        self.population_size = population_size
        self.dimensions = dimensions
        self.num_mutation = num_mutation
        self.shaping_scaling_factor_fs = shaping_scaling_factor_fs
        self.asymmetry_factor_af = asymmetry_factor_af
        self.init_val_shape_factor_sd = init_val_shape_factor_sd

    def optimize(self, boundaries: tuple[int, int]):
        pass

    def init_population(self, dim: int, size: int = 2, low=0.0, high=1.0) -> list[np.ndarray]:
        """
        Initialize population of given size with individuals of given dimension and constraints
        :param dim: dimension of every individual
        :param size: size of initialized population
        :param low: lower limit of the range of every gene
        :param high: higher limit of the range of every gene
        :return: population (list) of individuals (numpy arrays)
        """
        return [np.random.uniform(low=low, high=high, size=(dim,)) for _ in range(size)]

    def normalize_population(self, population: list[np.ndarray], low, high):
        """
        Normalizes the input population
        :param population: population to normalize
        :param low: lower limit of the range of every gene
        :param high: higher limit of the range of every gene
        :return: normalized population (list)
        """
        return [(ind - low) / (high - low) for ind in population]

    def denormalize_population(self, population: list[np.ndarray], low, high):
        """
        Denormalizes the input population
        :param population: population to denormalize
        :param low: lower limit of the range of every gene
        :param high: higher limit of the range of every gene
        :return: denormalized population (list)
        """
        return [(ind * (high - low)) + low for ind in population]

    @staticmethod
    def transformation(random_gene, mean_gene, si1, si2):
        def transform(ui):
            return mean_gene * (1 - math.exp(-1 * ui * si1)) + (1 - mean_gene) * math.exp((ui - 1) * si2)

        return transform(random_gene) + (1 - transform(1) + transform(0)) * random_gene - transform(0)


if __name__ == '__main__':
    optimizer = MVMO(10000, 100, 5, 3)
