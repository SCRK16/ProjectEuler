from collections import defaultdict

def prime_factors(upper):
    primes = set()
    composites = defaultdict(set)
    for i in range(2, upper):
        if i not in composites:
            primes.add(i)
            t = 2
            while t * i < upper:
                composites[t * i].add(i)
                t += 1
    return primes, composites

upper = 1000000
primes, factors = prime_factors(upper)

#Find numbers with 4 factors
factors = set(x[0] for x in filter(lambda x: len(x[1]) == 4, factors.items()))

#Determine consecutive integers which are all in factors
next_3_in_factors = lambda i: i + 1 in factors and i + 2 in factors and i + 3 in factors
result = sorted(filter(next_3_in_factors, factors))

print(result[0])
