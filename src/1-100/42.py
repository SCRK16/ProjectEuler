def word_value(word):
    result = 0
    for c in word:
        result += ord(c) - ord('A') + 1
    return result

def triangles(upper):
    t = set()
    current = 1
    add = 2
    while current < upper:
        t.add(current)
        current += add
        add += 1
    return t

with open("42.txt") as f:
    content = f.read()

content = [w.strip('"') for w in content.split(',')]
content[-1] = content[-1][:-2]

word_values = [(word, word_value(word)) for word in content]
max_word_value = max(word_values, key=lambda t: t[1])[1]
triangle = triangles(max_word_value)
triangle_words = [word for word in word_values if word[1] in triangle]

print(len(triangle_words))
