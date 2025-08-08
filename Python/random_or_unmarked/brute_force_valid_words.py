import nltk
from nltk.corpus import words
from itertools import permutations

try:
    d = set(w.lower() for w in words.words())
except LookupError:
    nltk.download("words")
    d = set(w.lower() for w in words.words())

valid_words = set()

letters = input("Enter letters (e.g. twerti): ").lower()

for i in range(1, len(letters) + 1):
    for perm in permutations(letters, i):
        word = "".join(perm)
        if word in d and (len(word) > 1 or word in ["a", "i"]):
            valid_words.add(word)

print(valid_words)
