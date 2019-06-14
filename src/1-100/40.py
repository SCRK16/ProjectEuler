from itertools import count
import sys
sys.path.append("..")
from euler import digits

wanted = [1, 10, 100, 1000, 10000, 100000, 1000000]

constant = []
for i in count():
    ds = digits(i, convert=True)
    constant.extend(ds)
    if len(constant) > wanted[-1]:
        break

result = 1
for w in wanted:
    result *= constant[w]

print(result)
