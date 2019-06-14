import sys
sys.path.append("..")
from euler import concatenate, digits

def is_pandigital(n):
    if not 99999999 <= n < 999999999:
        return False
    digits = set(str(n))
    return digits == {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

best = 0

for i in range(1, 10000):
    current = i
    mult = 2
    while len(digits(current)) < 9:
        current = concatenate((current, i * mult))
        mult += 1
    if is_pandigital(current) and current > best:
        best = current

print(best)
