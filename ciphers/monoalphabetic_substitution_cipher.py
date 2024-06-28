import string
import random


def generate_key(alphabet):
    key_list = list(alphabet)
    random.shuffle(key_list)
    return "".join(key_list)


def create_maps(alphabet, key):
    encryption_map = {}
    decryption_map = {}
    for i in range(len(alphabet)):
        encryption_map[alphabet[i]] = key[i]
        decryption_map[key[i]] = alphabet[i]
    return encryption_map, decryption_map


def cipher(text, mapping):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += mapping[char.lower()].upper()
            else:
                result += mapping[char]
        else:
            result += char

    return result


def frequency_analysis(text):
    frequencies = {letter: 0 for letter in string.ascii_lowercase}

    for char in text:
        char_lower = char.lower()
        if char_lower in string.ascii_lowercase:
            frequencies[char_lower] += 1

    frequencies = dict(
        sorted(frequencies.items(), key=lambda item: item[1], reverse=True))
    return frequencies


if __name__ == "__main__":
    plain_text = "Hello World! The quick brown fox jumps over the lazy dog."
    alphabet = string.ascii_lowercase

    key = generate_key(alphabet)

    encryption_map, decryption_map = create_maps(alphabet, key)

    encrypted_result = cipher(plain_text, encryption_map)
    decrypted_result = cipher(encrypted_result, decryption_map)

    encrypted_analysis = frequency_analysis(encrypted_result)
    decrypted_analysis = frequency_analysis(plain_text)

    print(f"Original Text:           {plain_text}")
    print(f"Key:                     {key}")
    print(f"Encrypted Text:          {encrypted_result}")
    print(f"Decrypted Text:          {decrypted_result}\n")

    print("Frequency Analysis:")
    for encrypted_freq, decrypted_freq in zip(encrypted_analysis.items(), decrypted_analysis.items()):
        print(
            f"{encrypted_freq[0]}: {encrypted_freq[1]} - {decrypted_freq[0]}: {decrypted_freq[1]}")
