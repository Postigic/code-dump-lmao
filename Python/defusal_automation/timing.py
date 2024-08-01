letter_mapping = {
    "A": 4,
    "B": 3,
    "C": 7,
    "D": 9
}


def string_to_colour(timing_string):
    pair1, pair2 = timing_string[:2], timing_string[2:]
    sum1 = sum(int(num) for num in pair1)
    sum2 = sum(letter_mapping[letter] for letter in pair2)
    result = sum1 * sum2
    if 0 <= result <= 59:
        return "White"
    elif 60 <= result <= 99:
        return "Red"
    elif 100 <= result <= 199:
        return "Yellow"
    elif 200 <= result <= 299:
        return "Green"
    elif 300 <= result <= 399:
        return "Blue"
    elif 400 <= result <= 499:
        return "Yellow"
    elif 500 <= result <= 599:
        return "Red"
    else:
        return "White"
