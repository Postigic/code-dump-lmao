from word2number import w2n
from utils import STYLE

def confirm(prompt):
    while True:
        response = input(STYLE["GREEN"] + prompt + " (Y/N): " + STYLE["RESET"]).strip().upper()

        if response == 'Y':
            return True
        elif response == 'N':
            return False
        else:
            print(STYLE["RED"] + "Please respond with Y or N." + STYLE["RESET"])

def get_input(prompt):
    print(STYLE["CYAN"] + prompt + STYLE["RESET"])

    while True:
        sentence = input("Enter your prompt here: ")
        if not sentence:
            break
        if not confirm(f"You typed: '{sentence}'. Is that correct?"):
            print(STYLE["YELLOW"] + "Starting over...\n" + STYLE["RESET"])
            return get_input(prompt)
        return sentence


def parse_number_words(word):
    try:
        num = w2n.word_to_num(word)

        if 1 <= num <= 10:
            print(STYLE["YELLOW"] + "\nWow, real big numbers today huh?" + STYLE["RESET"])

        if num >= 1000000:
            print(STYLE["YELLOW"] + "\nCompensating for something?" + STYLE["RESET"])

        return num
    except ValueError:
        print(STYLE["RED"] + f"\n'{word}' isn't a number I recognise. Try again, genius." + STYLE["RESET"])
        return None
    except Exception:
        return None
