import random
import requests

style = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "RESET": "\033[0m"
}


def get_random_word(length):
    reponse = requests.get(f"https://random-word-api.herokuapp.com/word?length={length}")
    if reponse.status_code == 200:
        return reponse.json()[0]
    else:
        raise Exception(f"Failed to get a random word: {reponse.status_code}")


def validate_difficulty():
    while True:
        choice = input("Choose a difficulty (1 - Easy, 2 - Hard): ")
        if choice in ["1", "2"]:
            return choice
        else:
            print(style["RED"] + "Invalid input." + style["RESET"])
            continue


def validate_guess():
    while True:
        guess = input("Guess a character: ").lower()

        if not guess.isalpha():
            print(style["RED"] + "You can only guess letters." + style["RESET"])
            continue
        elif len(guess) != 1:
            print(style["RED"] + "You can only guess one letter at a time." + style["RESET"])
            continue
        else:
            return guess


choice = validate_difficulty()

if choice == "1":
    length = random.randint(3, 5)
else:
    length = random.randint(6, 12)

print(style["YELLOW"] + "*"*50 + style["RESET"])


turns = 10
word = get_random_word(length)
guesses = ""

while turns > 0:
    remaining_letters = len(word)

    print("\n", end="")
    for char in word:
        if char in guesses:
            print(style["CYAN"] + char, end="")
            remaining_letters -= 1
        else:
            print(style["CYAN"] + "_", end="")
    print("\n" + style["RESET"], end="")
    
    if remaining_letters == 0:
        print(style["YELLOW"] + "\nYou win!" + style["RESET"])
        print(f"The word is: {word}")
        break
    
    guess = validate_guess()

    if guess in guesses:
        print(style["GREEN"] + "You have already guessed that letter." + style["RESET"])
    elif guess not in word:
        guesses += guess
        turns -= 1
        print(style["GREEN"] + "That letter is not in the word." + style["RESET"])
        print(f"You have {turns} more guesses.")
    else:
        guesses += guess

    if turns == 0:
        print(style["RED"] + "\nYou lose." + style["RESET"])
        print(f"The word was: {word}")
