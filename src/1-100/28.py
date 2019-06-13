"""
Pattern: Currently positioned at top right corner
To get to the next corner you need to:
Right 1 + Down n = n + 1, arrive at bottom right
Left n + 1, arrive at bottom left
Up n + 1, arrive at top left
Right n + 1, arrive at top right
Increment n by 2
Repeat

Start at 1
Stop when hitting 1001 * 1001
"""

s = 0
current = 1
n = -1
cycle = 0
while current <= 1001*1001:
    s += current
    if cycle == 0:
        n += 2
    cycle = (cycle + 1) % 4
    current += n + 1
    
print(s)
