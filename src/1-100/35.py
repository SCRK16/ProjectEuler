def sieve(upper):
    #Generate all primes below upper using the sieve of Eratosthenes
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

def is_circular_prime(p, primes):
    #Check if p is a circular prime
    as_string = ''.join([x for x in str(p)])
    rotated = as_string[1:] + as_string[:1]
    while rotated != as_string:
        if int(rotated) not in primes:
            return False
        rotated = rotated[1:] + rotated[:1]
    return True
    
    

upper = 1000000
primes = sieve(upper)
forbidden = {'2', '4', '5', '6', '8', '0'}
primes_optimized = [p for p in primes if not bool({x for x in str(p)} & forbidden)]

circular = {p for p in primes_optimized if is_circular_prime(p, primes_optimized)}
circular |= {2, 5}

print(len(circular))

"""
We know that (other than 2 and 5), no primes end in 2, 4, 5, 6, 8 and 0
So checking primes with those digits in them is of no use
Removing those brings the number of primes we need to check
from 78498 down to 1111

Runtime unoptimized: 1m24.735s
Runtime optimized: 0.990s
Quite the speed increase!

Further possible improvement:
If p is a circular prime, then all rotations of p are too
"""
