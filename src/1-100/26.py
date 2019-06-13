def sieve(upper):
    primes = set()
    composites = set()
    for i in range(2, upper):
        if i not in composites:
            primes.add(i)
            t = 2
            while t * i < upper:
                composites.add(t * i)
                t += 1
    return sorted(primes)

upper = 1000
primes = sieve(upper)

#See wikipedia.org/wiki/Full_reptend_prime
# and wikipedia.org/wiki/Full_reptend_prime#Patterns_of_occurrence_of_full_reptend_primes
impossible = {1, 3, 9, 13, 27, 31, 37, 39}

best = 0

for p in reversed(primes):
    if (10 ** (p-1)) % p == 1 and p % 40 not in impossible:
        best = p
        break

print(best)
