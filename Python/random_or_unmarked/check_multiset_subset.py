from collections import Counter

def check_multiset_subset(s1: str, s2: str) -> bool:
    print(Counter(s1))
    print(Counter(s2))
    print(Counter(s1) - Counter(s2))
    return not (Counter(s1) - Counter(s2))

print(check_multiset_subset("ab", "eidbaooo"))  # True
print(check_multiset_subset("ab", "eidboaoo"))  # True
print(check_multiset_subset("ab", "eidbocoo"))  # False
