word_list = ["palindrome", "effervescent",
             "tambourine", "synonyms", "ministrations"]
shortest_word = word_list[0]

for i in range(len(word_list)):
    shortest_word = word_list[i] if len(word_list[i]) < len(
        shortest_word) else shortest_word

print(shortest_word)
