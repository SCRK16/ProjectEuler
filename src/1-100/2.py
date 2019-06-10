from collections import deque

fibs = deque([1, 1], 2)
result = 0

while True:
    new = sum(fibs)
    if new > 4000000:
        break
    fibs.append(new)
    if new % 2 == 0:
        result += new

print(result)
