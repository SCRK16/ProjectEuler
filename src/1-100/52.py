import sys
sys.path.append("..")
from euler import digits

def valid(n):
    d = sorted(digits(n))
    t = 2
    m = t * n
    while sorted(digits(m)) == d:
        t += 1
        m = t * n
    return t >= 7

found = False
current = 0
while not found:
    current += 1
    if valid(current):
        found = current

print(found)
