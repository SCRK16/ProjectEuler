def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_maximum_factor_exponent(n, upper):
    exponent = 1
    i = n
    while i < upper:
        i *= n
        exponent += 1
    return exponent-1

upper = 20
factors = {}
for i in range(2, upper+1):
    if is_prime(i):
        factors[i] = find_maximum_factor_exponent(i, upper)

result = 1
for factor in range(2, upper+1):
    if factor in factors:
        times = factors[factor]
        result *= factor ** times

print(result)
