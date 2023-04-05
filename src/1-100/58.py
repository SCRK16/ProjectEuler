from math import sqrt

# Only works for n > 2
def is_prime(n):
	for i in range(2, int(sqrt(n))+1):
		if n % i == 0:
			return False
	return True

# Start with diagonals filled with 1, 3, 5, 7, 9
diagonal_count = 5
prime_count = 3
n = 2
current = 9

while prime_count / diagonal_count >= 0.1:
	for i in range(4):
		current = current + 2*n
		diagonal_count += 1
		# i = 3 -> current is a square number, which are never prime
		if i != 3 and is_prime(current): 
			prime_count += 1
	n += 1
print(2*n-1)