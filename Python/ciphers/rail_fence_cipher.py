def encrypt(text, key=3):
    if key == 1:
        return text

    rails = [""] * key
    direction = 1
    rail = 0

    for char in text:
        rails[rail] += char
        rail += direction

        if rail == 0 or rail == key - 1:
            direction = -direction

    return "".join(rails)


def decrypt(cipher_text, key=3):
    if key == 1:
        return cipher_text

    n = len(cipher_text)
    rail_pattern = [[] for _ in range(key)]
    direction = 1
    rail = 0

    for i in range(n):
        rail_pattern[rail].append(i)
        rail += direction

        if rail == 0 or rail == key - 1:
            direction = -direction

    rail_lengths = [len(rail) for rail in rail_pattern]
    rails = []
    start = 0

    for length in rail_lengths:
        rails.append(cipher_text[start:start + length])
        start += length

    result = [""] * n
    for rail, indices in zip(rails, rail_pattern):
        for i, idx in enumerate(indices):
            result[idx] = rail[i]

    return "".join(result)


if __name__ == "__main__":
    plain_text = "Hello World!"

    encrypted_text = encrypt(plain_text)
    decrypted_text = decrypt(encrypted_text)

    print(f"Original Text:   {plain_text}")
    print(f"Encrypted Text:  {encrypted_text}")
    print(f"Decrypted Text:  {decrypted_text}")
