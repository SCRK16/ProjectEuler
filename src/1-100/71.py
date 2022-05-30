from math import gcd

upper = 3/7
lower = 2/5
prev_n = 2
prev_d = 5
n = 2
d = 5
while d <= 1000000:
	if n/d <= lower:
		n += 1
	else:
		d += 1
	if gcd(n, d) == 1:
		if lower < n/d < upper:
			lower = n/d
			prev_n = n
			prev_d = d
print(prev_n)