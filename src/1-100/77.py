from collections import defaultdict

def sieve(upper):
	primes = set()
	composites = set()
	for i in range(2, upper):
		if i not in composites:
			primes.add(i)
			t = 2
			while t * i < upper:
				composites.add(t * i)
				t += 1
	return primes
	
upper = 100
primes = sorted(sieve(upper))
primes_count = len(primes)-1

"""
count[n][i] is the number of ways n can be written as the sum of primes with index >= i
i.e. count[n][2] is the number of ways n can be written as the sum of primes without using 2 or 3 (so only primes >= 5)
count[n][0] is the total number of ways n can be written as the sum of primes
"""
count = defaultdict(lambda: defaultdict(int))
count[0] = defaultdict(lambda: 1)
count[2][0] = 1

n = 2
while count[n][0] <= 5000:
	n += 1
	for i in range(primes_count, -1, -1):
		count[n][i] = count[n - primes[i]][i] + count[n][i+1]
print(n)
