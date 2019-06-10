primes = set()
composites = set()

# Sieve of Eratosthenes
i = 2
while i < 2000000:
    if i in composites:
        pass
    elif i * i > 2000000:
        primes.add(i)
    else:
        primes.add(i)
        j = 2
        while i * j < 2000000:
            composites.add(i * j)
            j += 1
    i += 1

result = sum(primes)
print(result)
