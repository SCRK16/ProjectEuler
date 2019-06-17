import sys
sys.path.append("..")
from euler import sieve
from collections import defaultdict

def consecutive_prime_sum(sums, primes, upper):
    primes_list = sorted(primes)
    index = 0
    current = []
    s = sum(current)
    starting_index = index
    while starting_index < len(primes_list):
        s = sum(current)
        while s < upper and index < len(primes_list):
            current.append(primes_list[index])
            s = sum(current)
            index += 1
            if s in primes:
                sums[s] = max(sums[s], len(current))
        starting_index += 1
        index = starting_index
        current = []
    return sums


upper = 1000000
primes = sieve(upper)
sums = defaultdict(lambda: 0)

sums = consecutive_prime_sum(sums, primes, upper)
result = max(sums.items(), key=lambda x: x[1])
print(result[0])
