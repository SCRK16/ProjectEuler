import sys
sys.path.append("..")
from euler import generate_polygonals, sieve
	
upper = 10000
primes = sieve(upper)
squares_doubled_formula = lambda n: 2 * n * n
squares_doubled = sorted(generate_polygonals(upper, squares_doubled_formula))

found = False

i = 9
while not found:
    if i not in primes:
        for sd in squares_doubled:
            if sd > i:
                found = i
                break
            if i - sd in primes:
                break
    i += 2
	
print(found)
