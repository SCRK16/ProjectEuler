n = 600851475143
factors = []
while n != 1:
    factor_found = False
    for i in range(2, n):
        if n % i == 0: # i is a factor of n
            factor_found = True
            factors.append(i)
            n //= i
            break
    if not factor_found: # n is prime
        factors.append(n)
        break
print(factors)
print(max(factors))
