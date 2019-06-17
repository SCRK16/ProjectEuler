import sys
sys.path.append("..")
from euler import sieve, concatenate
from collections import defaultdict
from itertools import combinations, chain

def is_valid(sequence):
    dif = sequence[1] - sequence[0]
    return sequence[2] - sequence[1] == dif

primes = sieve(10000)
primes = {x for x in primes if x > 1000}

perms = defaultdict(list)

for p in sorted(primes):
    p_string = ''.join(sorted(str(p)))
    perms[p_string].append(p)

perms = filter(lambda x: len(x) >= 3, perms.values())
perms = (list(combinations(x, r=3)) for x in perms)
perms = chain.from_iterable(perms)
valid = filter(is_valid, perms)
valid = list(filter(lambda x: x[0] != 1487, valid))
valid = concatenate(valid[0])

print(valid)
