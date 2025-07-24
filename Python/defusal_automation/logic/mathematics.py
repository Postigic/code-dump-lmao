letter_number_mapping = {
    "A": 1,
    "B": 3,
    "C": 7,
    "D": 2,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 0,
    "I": 8,
    "J": 9
}

def letters_to_num(letter_string):
    numbers = int("".join([str(letter_number_mapping[letter])
                  for pair in letter_string for letter in pair]))
    num1 = numbers // 100
    num2 = numbers % 100
    return num1 * num2
