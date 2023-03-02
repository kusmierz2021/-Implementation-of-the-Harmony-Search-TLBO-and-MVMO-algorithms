

class MVMO:
    def __init__(self, iterations: int, population_size: int, dimensions: int, num_mutation: int, shaping_scaling_factor_fs=1.0, asymmetry_factor_af=1.0, init_val_shape_factor_sd=75.0):
        self.iterations = iterations
        self.population_size = population_size
        self.dimensions = dimensions
        self.num_mutation = num_mutation
        self.shaping_scaling_factor_fs = shaping_scaling_factor_fs
        self.asymmetry_factor_af = asymmetry_factor_af
        self.init_val_shape_factor_sd = init_val_shape_factor_sd





if __name__ == '__main__':
    optimizer = MVMO(10000, 100, 5, 3)

