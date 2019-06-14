import sys
sys.path.append("..")
from euler import sieve

upper = 1000
primes = sieve(upper)

#See wikipedia.org/wiki/Full_reptend_prime
# and wikipedia.org/wiki/Full_reptend_prime#Patterns_of_occurrence_of_full_reptend_primes
impossible = {1, 3, 9, 13, 27, 31, 37, 39}

best = 0

for p in reversed(sorted(primes)):
    if (10 ** (p-1)) % p == 1 and p % 40 not in impossible:
        best = p
        break

print(best)
