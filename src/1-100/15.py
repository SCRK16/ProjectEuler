import sys
sys.path.append("..")
from euler import factorial

def nCk(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

result = nCk(40, 20)
print(result)
