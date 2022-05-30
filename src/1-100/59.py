from string import ascii_lowercase
from itertools import permutations, cycle
from copy import deepcopy

forbidden = {"{", "}", "@", "#", "^", "*"} 

def find_key(content):
	for c1, c2, c3 in permutations(ascii_lowercase, 3):
		o1, o2, o3 = ord(c1), ord(c2), ord(c3)
		cypher = map(int, deepcopy(content))
		plain = [chr(cy ^ key) for cy, key in zip(cypher, cycle((o1, o2, o3)))]
		plain_set = set(plain)
		if not plain_set.intersection(forbidden):
			plain = ''.join(plain)
			if "and" in plain:
				print(c1, c2, c3, plain[:20])

if __name__ == "__main__":
	with open("p059_cipher.txt", 'r') as file:
		content = map(int, file.read().split(','))
	result = sum(cy ^ key for cy, key in zip(content, cycle((ord('e'), ord('x'), ord('p')))))
	print(result)

