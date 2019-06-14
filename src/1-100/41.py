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
    return primes

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
