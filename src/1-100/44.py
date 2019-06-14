import numpy as np

def generate_ngonals(upper, formula):
    ngonals = set()
    i = 1
    next = formula(i)
    while next < upper:
        ngonals.add(next)
        i += 1
        next = formula(i)
    return ngonals

upper = 10000000

pentagon_formula = lambda n: n * (3*n - 1) // 2
pentagonals = generate_ngonals(upper, pentagon_formula)

best = np.inf

for pi in pentagonals:
    for pj in pentagonals:
        s = pi + pj
        d = abs(pi - pj)
        if d < best and s in pentagonals and d in pentagonals:
            best = d

print(best)
