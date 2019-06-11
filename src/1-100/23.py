def divisors(n):
    result = []
    for i in range(1, n):
        if n % i == 0:
            result.append(i)
    return result

def divisors_sum(n):
    return sum(divisors(n))

def is_abundant(n):
    return divisors_sum(n) > n

def is_abundant_sum(n, abundants):
    for i in abundants:
        left = n - i
        if left in abundants:
            return True
    return False

abundants = set()
for i in range(1, 28124):
    if is_abundant(i):
        abundants.add(i)

print(len(abundants))

s = 0
for i in range(1, 28124):
    if not is_abundant_sum(i, abundants):
        s += i

print(s)
