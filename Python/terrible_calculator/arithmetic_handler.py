import random
from utils import STYLE

def perform_addition(x, y):
    if x == 0 or y == 0:
        print(STYLE["RED"] + "\nWow, real funny." + STYLE["RESET"])
    
    return x + y

def perform_subtraction(x, y):
    return x - y

def perform_multiplication(x, y):
    if y == 0:
        print(STYLE["RED"] + "\nMultiplying by zero? How original." + STYLE["RESET"])
        return 0
    
    return x * y

def perform_division(x, y):
    if y == 0:
        print(STYLE["RED"] + "\nDividing by zero? Nice try. Here's a random number instead because you just can't behave yourself." + STYLE["RESET"])
        y = random.randint(1, 100)

    return x / y

def perform_exponentiation(x, y):
    return x ** y

def perform_modulus(x, y):
    if y == 0:
        print(STYLE["RED"] + "\nModulus by zero? Really? Here's a random number instead." + STYLE["RESET"])
        y = random.randint(1, 100)

    return x % y

def format_as_peano(n):
    return "S(" * n + "0" + ")" * n

def format_as_riddle(n):
    riddles = {
        0: "The void. Emptiness. Just like your brain.",
        1: "The loneliest number.",
        2: "The number of shoes most beings require.",
        3: "The crowd becomes odd when one leaves this trio.",
        4: "The number of walls in a room.",
        5: "A hand's worth of digits.",
        6: "The number of sides on a cube.",
        7: "Days it takes to doom a soul.",
        8: "The number of bits in a byte.",
        9: "Almost perfect, yet not quite ten.",
        10: "Two hand's worth of digits.",
        12: "The number of months in a year.",
        13: "The unlucky guest at dinner.",
        14: "The number of days in a fortnight.",
        15: "The number of minutes in a quarter hour.",    
        21: "Half of forty-two. Think about it.",
        42: "The answer to life... too bad your question is meaningless."
    }

    return riddles.get(n, format_as_peano(n))

def format_base(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if base > len(digits):
        raise ValueError("Base too large for available digits.")
    
    if n == 0:
        return "0"
    result = ""

    while n > 0:
        result = digits[n % base] + result
        n //= base

    return f"({result}){base}"

def format_as_roman(n):
    if n <= 0:
        return "nulla"
    
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
        (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"), (1, "I")
    ]
    result = ""

    for (number, numeral) in values:
        while n >= number:
            result += numeral
            n -= number

    return result

def format_as_morse(n):
    morse_code = {
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----."
    }
    return " ".join(morse_code[digit] for digit in str(n))

def format_as_emoji(n):
    emoji_digits = {
        "0": "0️⃣", "1": "1️⃣", "2": "2️⃣", "3": "3️⃣",
        "4": "4️⃣", "5": "5️⃣", "6": "6️⃣", "7": "7️⃣",
        "8": "8️⃣", "9": "9️⃣"
    }
    return " ".join(emoji_digits[digit] for digit in str(n))

def determine_format(num):
    formatters = [
        (format_as_peano, lambda n: n <= 100),
        (format_as_riddle, lambda n: True),
        (lambda n: format_base(n, random.choice(range(2, 15))), lambda n: True),
        (format_as_roman, lambda n: 1 <= n <= 3999),
        (format_as_morse, lambda n: True),
        (format_as_emoji, lambda n: True),
    ]

    valid_formatters = [f for f, cond in formatters if cond(num)]

    formatter = random.choice(valid_formatters)
    return formatter(num)
