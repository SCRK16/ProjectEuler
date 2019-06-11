def is_prime(n, primes):
    for i in primes:
        if n % i == 0:
            return False
    return True

number = 10001
primes = [2]
while len(primes) < number:
    i = primes[-1]
    while True:
        i += 1
        if is_prime(i, primes):
            primes.append(i)
            break

print(primes)
print(primes[-1])
