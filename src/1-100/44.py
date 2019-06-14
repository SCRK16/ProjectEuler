import numpy as np
import sys
sys.path.append("..")
from euler import generate_polygonals

upper = 10000000

pentagon_formula = lambda n: n * (3*n - 1) // 2
pentagonals = generate_polygonals(upper, pentagon_formula)

best = np.inf

for pi in pentagonals:
    for pj in pentagonals:
        s = pi + pj
        d = abs(pi - pj)
        if d < best and s in pentagonals and d in pentagonals:
            best = d

print(best)
