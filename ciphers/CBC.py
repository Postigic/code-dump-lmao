from pwn import xor
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

BLOCK_SIZE = 16
iv = os.urandom(BLOCK_SIZE)
key = os.urandom(16)


def encrypt(pt, key, iv):
    pt = pad(pt, BLOCK_SIZE)
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    ct_blocks = []
    previous_block = iv

    for i in range(0, len(pt), BLOCK_SIZE):
        block = pt[i: i + BLOCK_SIZE]
        ct_block = xor(block, previous_block)
        encrypted_block = cipher.encrypt(ct_block)
        ct_blocks.append(encrypted_block)
        previous_block = encrypted_block

    return iv + b"".join(ct_blocks)


def decrypt(ct, key, iv):
    cipher = AES.new(key=key, mode=AES.MODE_ECB)
    ct = ct[BLOCK_SIZE:]
    pt_blocks = []
    previous_block = iv

    for i in range(0, len(ct), BLOCK_SIZE):
        block = ct[i: i + BLOCK_SIZE]
        decrypted_block = cipher.decrypt(block)
        pt_block = xor(decrypted_block, previous_block)
        pt_blocks.append(pt_block)
        previous_block = block

    pt = b"".join(pt_blocks)
    return unpad(pt, BLOCK_SIZE)


plaintext = b"Hello World! The quick fox jumps over the whatever."
ciphertext = encrypt(plaintext, key, iv)

print(ciphertext)
print(decrypt(ciphertext, key, iv))
