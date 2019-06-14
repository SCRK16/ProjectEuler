import sys
sys.path.append("..")
from euler import factorial

f = factorial(100)
digits = [int(i) for i in str(f)]
result = sum(digits)
print(result)
