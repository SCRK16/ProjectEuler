from collections import deque

last = 1
index = 2
fibs = deque([1,1], 2)

while len(str(last)) < 1000:
    last = sum(fibs)
    fibs.append(last)
    index += 1

print(index)
