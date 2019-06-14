import sys
sys.path.append("..")
from euler import sieve

upper = 2000000
primes = sieve(upper)
result = sum(primes)
print(result)
