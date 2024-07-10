from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

BLOCK_SIZE = 16
iv = os.urandom(BLOCK_SIZE)
key = os.urandom(16)


def encrypt(pt, key):
    pt = pad(pt, BLOCK_SIZE)
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    ct = cipher.encrypt(pt)
    return ct


def decrypt(ct, key):
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    pt = cipher.decrypt(ct)
    pt = unpad(pt, BLOCK_SIZE)
    return pt


plaintext = b"Hello World! The quick fox jumps over the whatever."
ciphertext = encrypt(plaintext, key)

print(ciphertext)
print(decrypt(ciphertext, key))
