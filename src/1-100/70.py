import sys
sys.path.append("..")
from euler import factorize, totient

def is_permutation(n, m):
    return sorted(n) == sorted(m)

upper = int(1e7)
factorizations = factorize(upper=upper)
phi = totient(upper, factorizations)
phi = filter(lambda s: is_permutation(str(s[0]), str(s[1])), phi.items())
ratio = [(n, n/p) for n, p in phi]
print(min(ratio, key=lambda x: x[1])[0])
