import html5lib
import urllib

def wordscore(name):
    score = 0
    for char in name:
        value = ord(char) - ord('A') + 1
        score += value
    return score

#Read text from link
link = "https://projecteuler.net/project/resources/p022_names.txt"
f = urllib.request.urlopen(link)
text = f.read()
words = str(text)[2:-1].split(",")
words = [x[1:-1] for x in words]

#Sort words
words = sorted(words)

#Calculate scores
result = sum(wordscore(name) * (i+1) for i, name in enumerate(words))

print(result)

