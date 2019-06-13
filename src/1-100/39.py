from collections import defaultdict

def triangles(upper, squares):
    result = defaultdict(int)
    for a in range(1, upper):
        for b in range(a, upper-a):
            c_squared = a*a + b*b
            if c_squared in squares:
                c = squares[c_squared]
                if a + b + c <= upper:
                    result[a+b+c] += 1
    return result

upper = 1000
squares = [(i * i, i) for i in range(1, upper)]
squares = {square: root for (square, root) in squares}
t = triangles(upper, squares)

best = max(t.items(), key=lambda item: item[1])

print(best[0])
