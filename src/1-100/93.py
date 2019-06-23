import sys
sys.path.append("..")
from euler import concatenate
from copy import deepcopy
from itertools import count, permutations
import operator

def smallest_not_present(ns):
    for i in count(1):
        if i not in ns:
            return i

def possible_expression_results(ns):
    combiners = [operator.add, operator.add, operator.add,
                operator.sub, operator.sub, operator.sub,
                operator.mul, operator.mul, operator.mul,
                operator.truediv, operator.truediv, operator.truediv]
    perms = permutations(ns)
    combs = set(permutations(combiners, 3))
    results = set()
    for perm in perms:
        for comb in deepcopy(combs):
            intermediate =((comb[0](perm[0], perm[1]), perm[2], perm[3]),
                            (perm[0], comb[0](perm[1], perm[2]), perm[3]),
                            (perm[0], perm[1], comb[0](perm[2], perm[3])))
            for i in intermediate:
                try:
                    result1 = comb[2](comb[1](i[0], i[1]), i[2])
                except ZeroDivisionError:
                    result1 = -1    
                try:            
                    result2 = comb[2](i[0], comb[1](i[1], i[2]))
                except ZeroDivisionError:
                    result2 = -1
                if float(result1).is_integer() and result1 > 0:
                    results.add(int(result1))
                if float(result2).is_integer() and result2 > 0:
                    results.add(int(result2))
    return results

best = None
best_smallest = 0

for a in range(1, 10):
    for b in range(a+1, 10):
        for c in range(b+1, 10):
            for d in range(c+1, 10):
                results = possible_expression_results([a, b, c, d])
                smnp = smallest_not_present(results)
                if smnp > best_smallest:
                    best = (a, b, c, d)
                    best_smallest = smnp

print(concatenate(best))
