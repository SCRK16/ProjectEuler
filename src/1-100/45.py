import sys
sys.path.append("..")
from euler import generate_polygonals

upper = 10000000000

triangle_formula = lambda n: n * (n+1) // 2
pentagon_formula = lambda n: n * (3*n - 1) // 2
hexagon_formula  = lambda n: n * (2*n - 1)

triangles = generate_polygonals(upper, triangle_formula)
pentagonals = generate_polygonals(upper, pentagon_formula)
hexagonals = generate_polygonals(upper, hexagon_formula)

overlap = triangles & pentagonals & hexagonals

print(overlap)
