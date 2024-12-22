word_list = []
vowels = "aeiou"
total = 0


def count_vowels(word):
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count


for _ in range(5):
    while True:
        word = input("Enter word: ").lower()
        if word.isalpha():
            break
        print("Invalid word.")
    vowel_count = count_vowels(word)
    if vowel_count > 2:
        word_list.append(word)
    total += vowel_count

max_vowels = 0

for word in word_list:
    num_vowels = count_vowels(word)
    if num_vowels > max_vowels:
        max_vowels = num_vowels
        word_with_max_vowels = word


print(f"Word with highest number of vowels: {word_with_max_vowels}")
print(f"Words with more than two vowels: {word_list}")
print(f"Total number of vowels in all five words: {total}")
