import sys
sys.path.append("..")
from euler import sieve

def num_digits(n):
    return len(str(n))

def is_pandigital(n, l):
    digits = set(str(n))
    return digits == {str(i) for i in range(1, l+1)}

primes = sieve(10000000)

for p in sorted(primes, reverse=True):
    if is_pandigital(p, num_digits(p)):
        print(p)
        break
