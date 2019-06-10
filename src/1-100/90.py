from itertools import combinations

class Cube:
    def __init__(self, s):
        self.sides = s

    def __iter__(self):
        return self.sides.__iter__()

    def __hash__(self):
        return sum(hash(i) for i in self)

    def __str__(self):
        result = 'Cube('
        for i in self:
            result += str(i) + ', '
        return result[:-2] + ')'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.sides == other.sides

    def digits_as_strings(self):
        digits = {str(i) for i in self}
        if 6 in self:
            digits.add('9')
        if 9 in self:
            digits.add('6')
        return set(digits)

def possible_combinations(d1, d2):
    result = set()    
    for x in d1:
        for y in d2:
            result.add(x + y)
            result.add(y + x)
    return result

def cubes_make_squares(cube1, cube2, squares):
    digits1 = cube1.digits_as_strings()
    digits2 = cube2.digits_as_strings()
    comb = possible_combinations(digits1, digits2)
    return squares <= comb

squares = {str(i*i) for i in range(1, 10)}
squares = {'0' + i if len(i) < 2 else i for i in squares}

combinations = [set(i) for i in combinations(range(10), 6)]

result = 0
solution = set()

for c1 in combinations:
    cube1 = Cube(c1)
    for c2 in combinations:
        cube2 = Cube(c2)
        if (cube1, cube2) in solution or (cube2, cube1) in solution:
            pass
        elif cubes_make_squares(cube1, cube2, squares):
            solution.add((cube1, cube2))
            result += 1

print(result)
