import sys
sys.path.append("..")
from euler import digits
from fraction import Fraction

c = 0
f = 1

for i in range(1000):
    f = (1 + Fraction(1, 1 + f)).reduce()
    num_digit = len(digits(f.numerator))
    den_digit = len(digits(f.denominator))
    if num_digit > den_digit:
        c += 1
    #print(i, ": ", f, " count: ", c)

print(c)
