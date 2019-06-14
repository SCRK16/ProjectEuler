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

def left_truncatable(p, primes):
    digits = str(p)
    check = int(digits)
    while check in primes:
        digits = str(check)[1:]
        check = int(digits) if digits != '' else None
    return check is None

def right_truncatable(p, primes):
    digits = str(p)
    check = int(digits)
    while check in primes:
        digits = str(check)[:-1]
        check = int(digits) if digits != '' else None
    return check is None

def truncatable(p, primes):
    return left_truncatable(p, primes) and right_truncatable(p, primes)
    

upper = 1000000

primes = sieve(upper)

truncatable_primes = []

for p in primes:
    if p > 10 and truncatable(p, primes):
        truncatable_primes.append(p)

print(truncatable_primes)
print(len(truncatable_primes))
print(sum(truncatable_primes))
