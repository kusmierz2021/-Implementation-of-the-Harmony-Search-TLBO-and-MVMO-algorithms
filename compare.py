from hs import HS
from mvmo import MVMO
import threading
from optimization_functions import *


if __name__ == '__main__':
    rastrigins_boundaries = (-5.12, 5.12)
    zakharov_boundaries = (-5, 10)

    # hs in this case is so much better with 100 as init population size
    # hs_optimizer = HS(10_000, 6, rastrigins_boundaries, True, hmcr=0.9)
    # hs_population = hs_optimizer.init_population(100)
    # hs_optimizer.optimize(hs_population, rastrigins_function)


    # mvmo_optimizer = MVMO(10_000, 6, rastrigins_boundaries, True, mutation_size=3)
    # mvmo_population = mvmo_optimizer.init_population(100)
    # mvmo_optimizer.optimize(mvmo_population, rastrigins_function)
