import random


def generate_key(length):
    return bytes(random.randint(0, 255) for _ in range(length))


def xor_cipher(text, key):
    return bytes(x ^ y for x, y in zip(text, key))


if __name__ == "__main__":
    plain_text = b"Hello World! The quick brown fox jumps over the lazy dog."
    key = generate_key(len(plain_text))

    encrypted_text = xor_cipher(plain_text, key)
    decrypted_text = xor_cipher(encrypted_text, key)

    print(f"Original Text:  {plain_text}")
    print(f"Key:            {key}")
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Decrypted Text: {decrypted_text}")
