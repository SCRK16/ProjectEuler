from collections import defaultdict

def factorize(n):
    factors = defaultdict(int)
    while n > 1:
        factor_found = False
        for i in range(2, n):
            if n % i == 0: # i is a factor of n
                factor_found = True
                factors[i] += 1
                n //= i
                break
        if not factor_found: # n is prime
            factors[n] += 1
            break
    return factors

#determine factors
upper = 20
factors = {}
for i in range(2, upper+1):
    factors[i] = factorize(i)

#find highest amount of times a factor divides a number
max_factors = {}
for factor in range(2, upper+1):
    max_factors[factor] = 0
    for i in range(2, upper+1):
        if (factors[i])[factor] > max_factors[factor]:
            max_factors[factor] = factors[i][factor]

#multiply all factors together
result = 1
for factor in range(2, upper+1):
    times = max_factors[factor]
    result *= factor ** times

print(result)
