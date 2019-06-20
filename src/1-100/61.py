import sys
sys.path.append("..")
from euler import concatenate, digits, generate_polygonals

def find_cyclic_polygonals(polygonals, used, number, first="octagon"):
    if number == 0 and digits(used[0][1])[0:2] == digits(used[-1][1])[2:4]:
        return used, True
    if not used:
        ps = polygonals[first]
        for p in ps:
            used.append((first, p))
            used, found = find_cyclic_polygonals(polygonals, used, number-1)
            if found:
                return used, True
            used.pop()
        return used, False
    last = used[-1][1]
    last_ending = digits(last)[2:4]
    for f, ps in polygonals.items():
        if f not in {x[0] for x in used}:
            for new_ending in range(10, 100):
                new_polygonal = concatenate(last_ending + digits(new_ending))
                if new_polygonal in ps and new_polygonal not in {x[1] for x in used}:
                    used.append((f, new_polygonal))
                    used, found = find_cyclic_polygonals(polygonals, used, number-1)
                    if found:
                        return used, True
                    used.pop()
    return used, False
            

formulae = {"triangle": lambda n: n * (n + 1) // 2,
            "square": lambda n: n * n,
            "pentagon": lambda n: n * (3*n - 1) // 2,
            "hexagon": lambda n: n * (2*n - 1),
            "heptagon": lambda n: n * (5*n - 3) // 2,
            "octagon": lambda n: n * (3*n -2)}

upper = 10000
polygonals = {}
for polygon in formulae:
    polygonals[polygon] = {x for x in generate_polygonals(upper, formulae[polygon]) if x > 1000}

result, found = find_cyclic_polygonals(polygonals, [], 6)

print(result)
print(sum([x[1] for x in result]))
