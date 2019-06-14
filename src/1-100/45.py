def generate_ngonals(upper, formula):
    ngonals = set()
    i = 1
    next = formula(i)
    while next < upper:
        ngonals.add(next)
        i += 1
        next = formula(i)
    return ngonals

upper = 10000000000

triangle_formula = lambda n: n * (n+1) // 2
pentagon_formula = lambda n: n * (3*n - 1) // 2
hexagon_formula  = lambda n: n * (2*n - 1)

triangles = generate_ngonals(upper, triangle_formula)
pentagonals = generate_ngonals(upper, pentagon_formula)
hexagonals = generate_ngonals(upper, hexagon_formula)

overlap = triangles & pentagonals & hexagonals

print(overlap)
