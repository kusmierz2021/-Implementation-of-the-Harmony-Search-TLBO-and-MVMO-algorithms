from hs import HS
from mvmo import MVMO
from tlbo import TLBO
import threading
from optimization_functions import *


if __name__ == '__main__':
    rastrigins_boundaries = (-5.12, 5.12)
    zakharov_boundaries = (-5, 10)
    rosenbrock_boundaries = (-10, 10)


    # tlbo_optimizer = TLBO(100_000, 6, rastrigins_boundaries, True)
    # tlbo_population = tlbo_optimizer.init_population(100)
    # tlbo_optimizer.optimize(tlbo_population, rastrigins_function)

    # hs in this case is so much better with 100 as init population size
    # hs_optimizer = HS(10_000, 6, rastrigins_boundaries, True, hmcr=0.9)
    # hs_population = hs_optimizer.init_population(100)
    # hs_optimizer.optimize(hs_population, rastrigins_function)

    # mvmo_optimizer = MVMO(10_000, 6, rastrigins_boundaries, True, mutation_size=3)
    # mvmo_population = mvmo_optimizer.init_population(100)
    # mvmo_optimizer.optimize(mvmo_population, rastrigins_function)

    # it was totally surprising result!
    # tlbo_optimizer = TLBO(100_000, 6, zakharov_boundaries, False)
    # tlbo_population = tlbo_optimizer.init_population(10)
    # tlbo_optimizer.optimize(tlbo_population, zakharov_function)

    # hs_optimizer = HS(100_000, 6, zakharov_boundaries, False, hmcr=0.9)
    # hs_population = hs_optimizer.init_population(100)
    # hs_optimizer.optimize(hs_population, zakharov_function)

    # mvmo_optimizer = MVMO(10_000, 6, zakharov_boundaries, False, mutation_size=3)
    # mvmo_population = mvmo_optimizer.init_population(100)
    # mvmo_optimizer.optimize(mvmo_population, zakharov_function)


    # hs_optimizer = HS(10_000_000, 6, rosenbrock_boundaries, False, hmcr=0.9)
    # hs_population = hs_optimizer.init_population(10)
    # hs_optimizer.optimize(hs_population, rosenbrock_function)

    # mvmo_optimizer = MVMO(10_000_000, 6, rosenbrock_boundaries, False, mutation_size=3)
    # mvmo_population = mvmo_optimizer.init_population(10000)
    # mvmo_optimizer.optimize(mvmo_population, rosenbrock_function)