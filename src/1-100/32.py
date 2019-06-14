def concatenate(ns):
    return int(''.join([str(n) for n in ns]))

def is_pandigital(n):
    if not 99999999 <= n < 999999999:
        return False
    digits = set(str(n))
    return digits == {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

seen = set()

result = 0

for a in range(100):
    for b in range(a, 10000):
        product = a * b
        if product not in seen:
            concatenated = concatenate([a, b, product])
            if is_pandigital(concatenated):
                result += product
                seen.add(product)

print(result)
