from collections import defaultdict
from itertools import count

cubes = defaultdict(list)

for i in count():
    c = i ** 3
    digits = ''.join(sorted(str(c)))
    cubes[digits].append(c)
    if len(cubes[digits]) == 5:
        found = sorted(cubes[digits])
        break

roots = [round(x ** (1. / 3)) for x in found]
result = list(zip(roots, found))
print(result)

"""
Known bug:
This code finds the cube for which the largest permutation is smallest
Not:           the cube for which the smallest permutation is smallest
For n = 5, those two coincide, but for n > 5, this is not guaranteed

Fix:
Count the number of digits of the former cube
The latter cube needs to have the same number of digits
Stop searching when the number of digits in the cubes increase
"""
