from evolutionary_algorithm import EvolutionaryAlgorithm


class HS(EvolutionaryAlgorithm):
    def __init__(self, iterations: int, dimensions: int, boundaries: tuple[float, float], hmcr: float = None,
                 par: float = None):
        super().__init__(iterations, dimensions, boundaries)
        self.hmcr = hmcr
        self.par = par


if __name__ == '__main__':
    boundaries = (-5.12, 5.12)
    optimizer = HS(10000, 6, boundaries)
    population = optimizer.init_population(1000)

