import sys
sys.path.append("..")
from euler import wordscore
from euler import generate_polygonals

with open("42.txt") as f:
    content = f.read()

content = [w.strip('"') for w in content.split(',')]
content[-1] = content[-1][:-2]

triangle_formula = lambda n: n * (n + 1) // 2

word_values = [(word, wordscore(word)) for word in content]
max_word_value = max(word_values, key=lambda t: t[1])[1]
triangle = generate_polygonals(max_word_value, triangle_formula)
triangle_words = [word for word in word_values if word[1] in triangle]

print(len(triangle_words))
