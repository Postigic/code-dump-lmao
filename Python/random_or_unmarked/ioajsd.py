from random import randint

winning_conditions = {
    "r": "s",
    "p": "r",
    "s": "p"
}


player_choice = input("Enter your choice (r, p, s): ").lower()
computer_choice = randint(1, 3)

if computer_choice == 1:
    computer_choice = "r"
elif computer_choice == 2:
    computer_choice = "p"
else:
    computer_choice = "s"

print(f"Computer picked {computer_choice}.")

if player_choice == computer_choice:
    print("Draw.")
elif winning_conditions.get(player_choice) == computer_choice:
    print("You win!")
else:
    print("You lose.")
