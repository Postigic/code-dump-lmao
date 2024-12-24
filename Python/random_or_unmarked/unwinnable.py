import random
number = random.randint(1, 10) + 0.1
print(number)

guess = input("Guess a number from 1 to 10.")
guess = float(guess)
guess = int(guess)
print(guess)

if guess == number:
    print("Congratulations, you win.")
else:
    print("You lose.")
