# meh... MEH... wo bu ming bai ni zai shuo shen me...

import string
from collections import Counter

ENGLISH_FREQ = {
    'A': 0.0817, 'B': 0.0149, 'C': 0.0278, 'D': 0.0425, 'E': 0.127,
    'F': 0.0223, 'G': 0.0202, 'H': 0.0609, 'I': 0.0697, 'J': 0.0015,
    'K': 0.0077, 'L': 0.0403, 'M': 0.0241, 'N': 0.0675, 'O': 0.0751,
    'P': 0.0193, 'Q': 0.0010, 'R': 0.0599, 'S': 0.0633, 'T': 0.0906,
    'U': 0.0276, 'V': 0.0098, 'W': 0.0236, 'X': 0.0015, 'Y': 0.0197,
    'Z': 0.0007
}

def chi_squared_score(text):
    n = len(text)
    count = Counter(text)
    score = 0
    
    for letter in string.ascii_uppercase:
        observed = count.get(letter, 0)
        expected = ENGLISH_FREQ[letter] * n
        score += (observed - expected) ** 2 / expected
        
    return score

def get_keyword(ciphertext, key_len):
    key = ""
    
    for i in range(key_len):
        segment = ciphertext[i::key_len]
        best_shift = 0
        best_score = float("inf")
        
        for shift in range(26):
            decrypted = "".join(chr((ord(c) - ord("A") - shift) % 26 + ord("A")) for c in segment)
            score = chi_squared_score(decrypted)
            
            if score < best_score:
                best_score = score
                best_shift = shift
            
        key_letter = chr(ord("A") + best_shift)
        key += key_letter
    
    return key
