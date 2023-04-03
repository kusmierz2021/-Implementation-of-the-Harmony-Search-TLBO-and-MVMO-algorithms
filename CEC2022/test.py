# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 17:14:04 2022

@author: Abhishek Kumar
"""

import numpy as np
from CEC2022 import cec2022_func

nx = 2  # dimensions
mx = 1  # population size
fx_n = 1  # function from 1 to 12

CEC = cec2022_func(func_num = fx_n)

# x = 200.0*np.random.rand(nx,mx)*0.0-100.0
x = 200.0*np.random.rand(nx,mx)-100.0
print(x)
F = CEC.values(x)
print(F.ObjFunc)


