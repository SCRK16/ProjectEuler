import sys
sys.path.append("..")
from euler import sieve

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
