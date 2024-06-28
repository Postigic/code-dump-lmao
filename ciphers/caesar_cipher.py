def cipher(text, shift=3):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result


if __name__ == "__main__":
    plain_text = "Hello World! The quick brown fox jumps over the lazy dog."
    encrypted_text = "Khoor Zruog! Wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj."
    print(cipher(plain_text))
    print(cipher(encrypted_text, -3))
