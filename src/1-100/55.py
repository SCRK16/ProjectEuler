import sys
sys.path.append("..")
from euler import digits, is_palindrome

def is_lychrel(n):
    i = 0
    while i < 50:
        n += int(''.join(list(reversed(digits(n)))))
        if is_palindrome(digits(n)):
            return False
        i += 1
    return True

print(len(list(filter(is_lychrel, range(10000)))))
