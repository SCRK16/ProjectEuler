from math import sqrt

def count_divisors(n):
    nod = 0
    root = int(sqrt(n))
    for i in range(1, root+1):
        if n % i == 0:
            nod += 2
    if root * root == n:
        nod -= 1
    return nod

n = 1
i = 2
while count_divisors(n) < 500:
    n += i
    i += 1

print(n)
