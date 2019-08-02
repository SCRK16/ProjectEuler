import sys
sys.path.append("..")
from fraction import Fraction
from euler import sieve, digits

upper = 100
primes = sieve(upper)
valid = []

for den in range(10, upper):
    if den % 10 != 0:
        for num in range(10, den):
            q = Fraction(num, den)
            num_digits = digits(num, convert=True)
            den_digits = digits(den, convert=True)
            if len(set(num_digits) & set(den_digits)) == 1:
                same = (set(num_digits) & set(den_digits)).pop()
                num_digits.remove(same)
                den_digits.remove(same)
                num_fake = num_digits[0]
                den_fake = den_digits[0]
                fake = Fraction(num_fake, den_fake)
                if q == fake:
                    valid.append(q)

result = 1
for q in valid:
    result *= q.reduce()
print(result.reduce().denominator)

