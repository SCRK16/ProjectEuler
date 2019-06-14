import sys
sys.path.append("..")
from euler import is_palindrome

largest = 9009
for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        if product > largest and is_palindrome(product):
            largest = product
print(largest)
