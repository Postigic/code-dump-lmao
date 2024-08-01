# IMPORTS

import random
import time
import sys

# VARIABLES

fails = 0
SECRET_CODE = "au revoir"

# DICTIONARIES

rangeLimits = {
    "easy": (0, 100),
    "medium": (0, 1000),
    "hard": (0, 10000),
    "nightmare": (0, 100000),
    "impossible": (0, 1000000),
    SECRET_CODE: (0, 10000000)
}

# FUNCTIONS


def game_info():
    print("Great! Let me explain the rules.")
    time.sleep(2)
    print("The rules are simple! You need to guess a random number from a specific range.")
    time.sleep(2)
    print("Your only hints are whether or not your guess was higher or lower than the number.")
    time.sleep(2)
    print("The game ends when you guess the number!")
    time.sleep(2)
    print("Oh yeah! Before I forget!")
    time.sleep(2)
    print("Next time you come back, you can just type 'Skip' at the start to skip this dialogue!")
    time.sleep(2)
    print("Although I hope you don't skip me because that would make me sad :(")
    time.sleep(2)
    print("Please pick a difficulty now!")
    time.sleep(2)


def select_difficulty():
    difficulty_selected = False
    while not difficulty_selected:
        difficulty = input(
            "Select a difficulty level (easy/medium/hard/nightmare/impossible): ").lower()

        if difficulty == "easy":
            n = random.randint(0, 100)
            time.sleep(1)
            print("Easy huh, you really don't like challenges do you?")
            time.sleep(2)
            print("The random number will be between 0 to 100.")
            time.sleep(2)
            print("Good luck and have fun!")
            time.sleep(2)
            difficulty_selected = True
        elif difficulty == "medium":
            n = random.randint(0, 1000)
            time.sleep(1)
            print("Medium, the default difficulty.")
            time.sleep(2)
            print("The random number will be between 0 to 1000.")
            time.sleep(2)
            print("Good luck and have fun!")
            time.sleep(2)
            difficulty_selected = True
        elif difficulty == "hard":
            n = random.randint(0, 10000)
            time.sleep(1)
            print("Hard, you don't like having fun huh?")
            time.sleep(2)
            print("The random number will be between 0 to 10000.")
            time.sleep(2)
            print("Good luck and... I would say 'have fun' but you won't enjoy this.")
            time.sleep(2)
            difficulty_selected = True
        elif difficulty == "nightmare":
            n = random.randint(0, 100000)
            time.sleep(1)
            print("Nightmare? So you didn't find hard challenging enough? Well I think this should pose as a challenge.")
            time.sleep(2)
            print("The random number will be between 0 to 100000.")
            time.sleep(2)
            print("You'll need a lot of luck, or just good elimination skills.")
            time.sleep(2)
            difficulty_selected = True
        elif difficulty == "impossible":
            n = random.randint(0, 1000000)
            time.sleep(1)
            print("Why did you pick this. You won't be able to do this.")
            time.sleep(2)
            print("The random number will be between 0 to 1000000.")
            time.sleep(2)
            print("I hope you have a lot of time on your hands.")
            time.sleep(2)
            difficulty_selected = True
        elif difficulty == SECRET_CODE:
            n = random.randint(0, 10000000)
            time.sleep(1)
            print("This... isn't right.")
            time.sleep(2)
            print("It's not what should have happened...")
            time.sleep(2)
            print("You... Why...")
            time.sleep(2)
            print("0 to 10000000.")
            time.sleep(2)
            difficulty_selected = True
        else:
            print(
                "Invalid difficulty level selected, what are you trying to achieve by doing this?")
            time.sleep(2)

    print("-- INITIALISING GAME --")
    time.sleep(2)
    return n, difficulty


def guessing_game():
    global fails
    global game_running
    while True:
        guess = input("Enter your guess: ")

        # PREVENT ERRORS/BUGS

        try:
            guess = int(guess)  # Try to convert input to an integer
        except ValueError:
            try:
                # If that fails, try to convert input to a float
                guess = float(guess)
                if difficulty != SECRET_CODE:
                    print("You inputted a float, no floats! >:(")
                else:
                    print("...")
            except ValueError:
                if difficulty != SECRET_CODE:
                    # If neither int nor float conversion works, it's not a number that was inputted
                    print("Input a number, idiot! >:(")
                else:
                    print("...")
            time.sleep(1)
            continue

        if (guess < rangeLimits.get(difficulty, (0,))[0]) or (guess > rangeLimits.get(difficulty, (0,))[1]):
            if difficulty == SECRET_CODE:
                print("0 to 10000000.")
            else:
                print(
                    f"Guess is out of range! It should be between {rangeLimits.get(difficulty, (0,))[0]} and {rangeLimits.get(difficulty, (0,))[1]}.")
            time.sleep(1)
            continue

        # CHECK GUESSES

        if guess < n:
            if difficulty != SECRET_CODE:
                print(str(guess) + " is too low, try again!")
                fails += 1
                time.sleep(1)
            else:
                print(str(guess) + " v")
                fails += 1

        elif guess > n:
            if difficulty != SECRET_CODE:
                print(str(guess) + " is too high, try again!")
                fails += 1
                time.sleep(1)
            else:
                print(str(guess) + " ^")
                fails += 1

        elif guess == n:
            if difficulty == "easy":
                if fails == 0:
                    print(
                        f"Congrats! The number was {str(guess)}! You got it on your first try!")
                elif fails == 1:
                    print(
                        f"Congrats! The number was {str(guess)}! It took you 1 fail to get the right answer.")
                else:
                    print(
                        f"Congrats! The number was {str(guess)}! It took you {str(fails)} fails to get the right answer.")
                time.sleep(2)
                print("You beat easy, come try a harder difficulty next!")

            elif difficulty == "medium":
                if fails == 0:
                    print(
                        f"Congrats! The number was {str(guess)}! You got it on your first try! You're pretty lucky!")
                elif fails == 1:
                    print(
                        f"Congrats! The number was {str(guess)}! It took you 1 fail to get the right answer. Impressive!")
                else:
                    print(
                        f"Congrats! The number was {str(guess)}! It took you {str(fails)} fails to get the right answer.")
                time.sleep(2)
                print("That was fun! Come try hard mode next!")

            elif difficulty == "hard":
                if fails == 0:
                    print(
                        f"Congrats! The number was {str(guess)}! You got it on your first try! Pure luck or cheats?")
                elif fails == 1:
                    print(
                        f"Congrats! The number was {str(guess)}! It took you 1 fail to get the right answer. That's pretty good!")
                else:
                    print(
                        f"Congrats! The number was {str(guess)}! It took you {str(fails)} fails to get the right answer. I don't blame you.")
                time.sleep(2)
                print("You beat hard mode! You should be proud!")

            elif difficulty == "nightmare":
                if fails == 0:
                    print(
                        f"Congrats! The number was {str(guess)}! You got it on your first try! Lady Luck must be on your side today!")
                elif fails == 1:
                    print(
                        f"Congrats! The number was {str(guess)}! It took you 1 fail to get the right answer. How did you do that?")
                else:
                    print(
                        f"Congrats! The number was {str(guess)}! It took you {str(fails)} fails to get the right answer. Surprised you managed to get it!")
                time.sleep(2)
                print(
                    "Whew, nightmare mode sure is challenging! Here's a tip, don't even bother taking on impossible.")

            elif difficulty == "impossible":
                if fails == 0:
                    print(
                        f"You... How..? The number was {str(guess)}... You got it on your... first try? This is jaw dropping...")
                elif fails == 1:
                    print(
                        "What... The number was {str(guess)}. It took you 1 fail to get the right answer. How are you doing this?")
                else:
                    print(
                        f"Finally you did it... The number was {str(guess)}. It took you {str(fails)} fails to get the right answer. Was it worth spending that much time?")
                time.sleep(2)
                print("...How the hell... You beat impossible mode... I can't believe you would torture yourself with this difficulty...")

            elif difficulty == SECRET_CODE:
                if fails == 0:
                    print("No fails?")
                    time.sleep(2)
                    print("No, that's impossible.")
                    time.sleep(2)
                    print("You must have printed 'n' didn't you?")
                    time.sleep(2)
                    print("There is no possible way to get 0 fails.")
                    time.sleep(2)
                    print("Get out.")
                elif fails == 1:
                    print("One fail?")
                    time.sleep(2)
                    print("It's not 0 fails but still...")
                    time.sleep(2)
                    print("You cannot achieve that.")
                    time.sleep(2)
                    print("You're not playing legitimately.")
                    time.sleep(2)
                    print("Go away.")
                else:
                    print("It's done... It's over...")
                    time.sleep(2)
                    print(f"{str(fails)} fails.")
                    time.sleep(2)
                    print("You couldn't just quit huh?")
                    time.sleep(2)
                    print("I wish you hadn't done this, how much time did you take?")
                    time.sleep(2)
                    print("Don't do this again.")

            time.sleep(2)
            sys.exit()

# seperation line for funnies


print("Hello! Do you want to play my game?")

while True:
    start_prompt = input("Yes/No: ").lower()
    if start_prompt in ["yes", "y", "yeah"]:
        game_info()
        n, difficulty = select_difficulty()

    elif start_prompt in ["no", "n", "nope"]:
        print("Aww... Hope you come play next time then!")
        time.sleep(1)
        sys.exit()

    elif start_prompt in ["skip", "s"]:
        print("Ah! Welcome back! I hope you had fun last time!")
        time.sleep(2)
        print("Let's get right to difficulty selection!")
        n, difficulty = select_difficulty()

    else:
        print("You need to type 'Yes' or 'No'. >:(")
        time.sleep(1)
        continue

    guessing_game()
