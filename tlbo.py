from evolutionary_algorithm import EvolutionaryAlgorithm


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

    def optimize(self):
        pass


if __name__ == '__main__':
    boundaries = (-5.12, 5.12)
    optimizer = TLBO(10_000, 6, boundaries, True)
    population = optimizer.init_population(1000)
    optimizer.optimize()
