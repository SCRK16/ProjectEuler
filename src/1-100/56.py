import sys
sys.path.append("..")
from euler import digits

best = 0
for a in range(100):
    for b in range(100):
        s = sum(digits(a ** b, convert=True))
        if s > best:
            best = s

print(best)
