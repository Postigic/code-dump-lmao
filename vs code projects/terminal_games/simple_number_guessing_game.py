# This one will be the more simple one, so you can digest the basics of this code I guess

# Importing important things

import random
import time
import sys

# Variables

fails = 0  # Amount of fails
n = random.randint(0, 100)  # Random number

# Everything above is preparation, the main game starts below this comment

while True:  # while True is basically a forever loop
    guess = input("Enter your guess: ")  # Prompts the player to guess a number

    # Error handling below, will mark the end of error handling

    try:
        # Basically this tries to convert the variable "guess" to an integer, eg: 6, 89, 45
        guess = int(guess)
    except ValueError:  # Check if int(guess) returns ValueError, this refers to when you're using the wrong type of value, eg: "hi" < 6 (This does not work because strings cannot be compared with numbers)
        print("Input a number, idiot! >:(")
        time.sleep(1)
        continue  # This basically restarts the while loop from the beginning

    if (guess < 0 or guess > 100):  # Check if the guessed number is below 0 or above 100
        print("Guess is out of range! It should be between 0 and 100.")
        time.sleep(1)
        continue  # Read above for def

    # Error handling is above, below are checks

    if guess < n:  # If guess is less than n
        print(str(guess) + " is too low, try again!")
        fails += 1  # Add 1 to fails
        time.sleep(1)
    elif guess > n:  # If guess is greater than n
        print(str(guess) + " is too high, try again!")
        fails += 1  # Read above for def
        time.sleep(1)
    elif guess == n:  # If guess is equal to n
        if fails == 0:  # If fails is equal to 0
            print("Congrats! The number was " + str(guess) +
                  "! You got it on your first try!")
        elif fails == 1:  # If fails is equal to 1
            print("Congrats! The number was " + str(guess) +
                  "! It took you 1 fail to get the right answer.")
        else:  # If fails is not equal to 0 or 1
            print("Congrats! The number was " + str(guess) +
                  "! It took you " + str(fails) + " fails to get the right answer.")
        time.sleep(2)
        sys.exit()  # End program
