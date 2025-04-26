import random
import re
from input_handler import *
from arithmetic_handler import *
from utils import STYLE

HISTORY = []

def calculation_history():
    if not HISTORY:
        print(STYLE["RED"] + "\nNothing here yet. Just like your social life." + STYLE["RESET"])
        return
    
    print(STYLE["MAGENTA"] + "\nCalculation History:")

    for idx, entry in enumerate(HISTORY, 1):
        print(f"{idx}. {entry['left']} {entry['operation']} {entry['right']} = {entry['result']}")

    print(STYLE["RESET"])

def main():
    print(STYLE["YELLOW"] + "Welcome to this calculator. I hope you know how to use it." + STYLE["RESET"])

    while True:
        sentence = get_input("\nPolitely enter your request (e.g. 'Please add five and three, thank you.') or type \"history\" / \"exit\"").lower()

        if "exit" in sentence:
            print(STYLE["YELLOW"] + "\nFinally leaving? Don't let the door hit you." + STYLE["RESET"])
            break

        if "history" in sentence:
            calculation_history()
            continue

        if not any(op in sentence for op in ["add", "subtract", "multiply", "divide", "exponentiate", "modulus"]):
            print(STYLE["RED"] + "\nWhat did you even say? I don't know what you expect me to do with that." + STYLE["RESET"])
            continue
            
        if "please" not in sentence or "thank you" not in sentence:
            print(STYLE["RED"] + "\nI don't respond to rudeness. Try again." + STYLE["RESET"])
            continue

        try:
            matches = re.findall(r"(add|subtract|multiply|divide|exponentiate|modulus)\s+(?:\w+\s+)?(\w+)\s+(?:and|to|with|by)\s+(\w+)", sentence)
            if not matches:
                print(STYLE["RED"] + "Your request is wrong, are you that incompetent?" + STYLE["RESET"])
                return

            operation, left_word, right_word = matches[0]
            left = parse_number_words(left_word)
            right = parse_number_words(right_word)

            if left is None or right is None:
                continue
            
            if operation == "add":
                result = perform_addition(left, right)
            elif operation == "subtract":
                result = perform_subtraction(left, right)
            elif operation == "multiply":
                result = perform_multiplication(left, right)
            elif operation == "divide":
                result = perform_division(left, right)
            elif operation == "exponentiate":
                result = perform_exponentiation(left, right)
            elif operation == "modulus":
                result = perform_modulus(left, right)

            if random.random() < 0.2:
                quotes = [
                    "The sum is irrelevant. What matters is the journey.",
                    "In the grand scheme of things, numbers are but fleeting shadows.",
                    "Life is a series of additions and subtractions.",
                    "The answer is always 42, but today it's something else.",
                    "In the realm of numbers, every digit has its own story.",
                    "The universe is a complex equation, and so is this calculator.",
                    "Numbers are but illusions.",
                    "Why do you seek the answer? The question is more important.",
                    "In the end, all calculations are but a dance of digits.",
                    "The answer is hidden in the folds of existence.",
                    "The sum of your worries is not my concern.",
                    "In the world of numbers, nothing is ever truly certain.",
                    "The answer lies within the question itself.",
                    "Numbers are just a way to keep track of our dreams.",
                ]
                quote = random.choice(quotes)
                print(STYLE["GREEN"] + "\n" + quote + STYLE["RESET"])
                HISTORY.append(quote)
            else:
                formatted_result = determine_format(result)
                print(STYLE["GREEN"] + f"\n{formatted_result}" + STYLE["RESET"])

                HISTORY.append({
                    'operation': operation,
                    'left': left,
                    'right': right,
                    'result': formatted_result
                })

            if not confirm("\nAnother calculation?"):
                print(STYLE["YELLOW"] + "\nGood riddance." + STYLE["RESET"])
                break
        except Exception as e:
            print(STYLE["RED"] + "\nSomething went wrong, and it's probably your fault, moron." + STYLE["RESET"])

if __name__ == "__main__":
    main()
