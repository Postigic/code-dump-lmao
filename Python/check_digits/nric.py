weights = [2, 7, 6, 5, 4, 3, 2]
check_digits = {
    1: "A",              
    2: "B", 
    3: "C", 
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "Z",
    11: "J"
}


def find_check_digit(nric_chars):
    if nric_chars[0] == "T":
        total = 4
    else:
        total = 0

    for i in range(1, len(nric_chars)):
        total += int(nric_chars[i]) * weights[i - 1]

    index = 11 - (total % 11)

    return check_digits[index]


def validate_nric(nric):
    if nric[0] == "T":
        total = 4
    else:
        total = 0

    for i in range(1, len(nric) - 1):
        total += int(nric[i]) * weights[i - 1]

    index = 11 - (total % 11)
    calculated = check_digits[index]

    return nric[-1] == calculated


# print(find_check_digit("S9153184")) # D
# print(find_check_digit("T9153184")) # J

print(validate_nric("S9153184D")) # valid
print(validate_nric("T9153184E")) # not valid