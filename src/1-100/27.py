def formula(n, a, b):
    return n * (n + a) + b

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

def possible_a(b, primes):
    return (a for a in range(-999, 1000) if a + b + 1 in primes)

primes = sieve(100000)
possible_b = [p for p in primes if p < 1000]

best_a = 0
best_b = 0
best_count = 0

for b in possible_b:
    for a in possible_a(b, primes):
        n = 0
        p = formula(n, a, b)
        while p in primes:
            n += 1
            p = formula(n, a, b)
        if n > best_count:
            best_a = a
            best_b = b
            best_count = n

print("a:", best_a)
print("b:", best_b)
print("count:", best_count)
print("product:", best_a*best_b)


"""
Since we need to check n = 0, we know that for (a, b) to be good:
n * (n + a) + b = 0 * (0 + a) + b = b needs to be prime
So we only use b < 1000 prime

Also, since we need to check n = 1, we know that for (a, b) to be good:
n * (n + a) + b = 1 * (1 + a) + b = a + b + 1
So we only use a where abs(a) < 1000 and a + b + 1 is prime (for the b given above)

Naive implementation without above optimizations runs in 1.270s
With above optimizations, runtime is decreased to 0.182s

It is important to use sets for member checking!
If primes were a list instead of a set, runtime would be 39.719s
"""
