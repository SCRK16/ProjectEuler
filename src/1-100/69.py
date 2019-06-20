import sys
sys.path.append("..")
from euler import factorize, totient

upper = int(1e6)
factorizations = factorize(upper=upper)
phi = totient(upper, factorizations)
ratio = [(n, n/p) for n, p in phi.items()]
print(max(ratio, key=lambda x: x[1])[0])
