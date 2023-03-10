import numpy as np
import math


class MVMO:
    def __init__(self, iterations: int, population_size: int, dimensions: int, num_mutation: int,
                 shaping_scaling_factor_fs=1.0, asymmetry_factor_af=1.0, val_shape_factor_sd=75.0):
        """

        :param iterations:
        :type iterations:
        :param population_size:
        :type population_size:
        :param dimensions:
        :type dimensions:
        :param num_mutation:
        :type num_mutation:
        :param shaping_scaling_factor_fs: between 0.9 and 1.0 for exploration, between 1.0 and 10.0 for exploitation
        :type shaping_scaling_factor_fs: float
        :param asymmetry_factor_af: between 1.0 and 10.0
        :type asymmetry_factor_af: float
        :param val_shape_factor_sd: between 10.0 and 90.0, by default 75.0
        :type val_shape_factor_sd: float
        """
        self.iterations = iterations
        self.population_size = population_size
        self.dimensions = dimensions
        self.num_mutation = num_mutation
        self.shaping_scaling_factor_fs = shaping_scaling_factor_fs
        self.asymmetry_factor_af = asymmetry_factor_af
        self.val_shape_factor_sd = val_shape_factor_sd
        self.kd = 0.0505 / self.dimensions + 1.0

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

    def count_si(self, best_gene, mean_gene, var_gene, last_no_zero_si):

        if not np.isfinite(var_gene):
            si1 = si2 = last_no_zero_si
            if last_no_zero_si < self.val_shape_factor_sd:
                self.val_shape_factor_sd = self.val_shape_factor_sd * self.kd
                si1 = self.val_shape_factor_sd
            elif last_no_zero_si > self.val_shape_factor_sd:
                self.val_shape_factor_sd = self.val_shape_factor_sd / self.kd
                si1 = self.val_shape_factor_sd
            return last_no_zero_si, si1, si2

        si = -1 * np.log(var_gene) * self.shaping_scaling_factor_fs

        if best_gene < mean_gene:
            si1 = si
            si2 = si * self.asymmetry_factor_af
        elif best_gene > mean_gene:
            si1 = si * self.asymmetry_factor_af
            si2 = si
        else:
            si1 = si2 = si
        return si, si1, si2


if __name__ == '__main__':
    optimizer = MVMO(10000, 100, 5, 3)
