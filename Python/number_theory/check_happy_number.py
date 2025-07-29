def check_happy_number(n):
    while n != 1:
        if n in {4, 16, 37, 58, 89, 145, 42, 20}:
            return False
        n = sum(int(d) ** 2 for d in str(n))
    return True

results = [
    check_happy_number(19), # True
    check_happy_number(2), # False
    check_happy_number(7), # True
    check_happy_number(42), # False
    check_happy_number(111), # False
    check_happy_number(10342), # False
    check_happy_number(100), # True
    check_happy_number(1000), # True
]

print(*results, sep="\n")