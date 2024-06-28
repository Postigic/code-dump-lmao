import random
import string


def generate_key(alphabet, length):
    return "".join(random.choice(alphabet) for _ in range(length))


def cipher(text, key, encrypt=True):
    encrypted_text = []
    for t_char, k_char in zip(text, key):
        if t_char.isalpha():
            offset = ord("a") if t_char.islower() else ord("A")
            t_index = ord(t_char.lower()) - ord("a")
            k_index = ord(k_char) - ord("a")

            if encrypt:
                encrypted_index = (t_index + k_index) % 26
            else:
                encrypted_index = (t_index - k_index + 26) % 26

            encrypted_text.append(chr(encrypted_index + offset))
        else:
            encrypted_text.append(t_char)

    return "".join(encrypted_text)


if __name__ == "__main__":
    plain_text = "Hello World! The quick brown fox jumps over the lazy dog."
    alphabet = string.ascii_lowercase

    key = generate_key(alphabet, len(plain_text))

    encrypted_text = cipher(plain_text, key)
    decrypted_text = cipher(encrypted_text, key, encrypt=False)

    print(f"Original Text:  {plain_text}")
    print(f"Key:            {key}")
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Decrypted Text: {decrypted_text}")
