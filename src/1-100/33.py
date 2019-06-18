import sys
sys.path.append("..")
from euler import sieve, digits

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        return str(self.numerator) + " / " + str(self.denominator)
    
    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def reduce(self):
        if self.numerator == 0:
            return Fraction(0, 1)
        primes = sieve(max(self.numerator, self.denominator))
        num = self.numerator
        den = self.denominator
        num_factors = []
        den_factors = []
        for p in primes:
            while num % p == 0:
                num_factors.append(p)
                num //= p
            while den % p == 0:
                den_factors.append(p)
                den //= p
        reduced_num = 1
        for x in num_factors:
            if x in den_factors:
                den_factors.remove(x)
            else:
                reduced_num *= x
        reduced_den = 1
        for y in den_factors:
            reduced_den *= y
        return Fraction(reduced_num, reduced_den)

    def __mul__(self, other):
        if type(other) == type(self):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        return Fraction(other * self.numerator, self.denominator)

    def __rmul__(self, other):
        return self * other

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

