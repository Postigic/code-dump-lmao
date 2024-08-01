import random
import sys


def main():
    user_wins = 0
    computer_wins = 0
    options = ["rock", "paper", "scissors"]
    win_conditions = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    while True:
        prompt = input("Do you want to play? (Y/N): ").strip().lower()

        if prompt == "n":
            print("Exiting...")
            sys.exit()
        elif prompt == "y":
            user_wins, computer_wins = game(
                user_wins, computer_wins, options, win_conditions)
        else:
            print("Invalid input.")


def game(user_wins, computer_wins, options, win_conditions):
    while True:
        user_choice = input(
            "Type rock, paper or scissors (Q to quit): ").strip().lower()

        if user_choice == "q":
            break
        if user_choice not in options:
            print("Invalid input.")
            continue

        computer_choice = random.choice(options)
        print(f"\nUser picked {user_choice}.")
        print(f"Computer picked {computer_choice}.")

        if (user_choice == computer_choice):
            print("Draw!")
        elif win_conditions[user_choice] == computer_choice:
            print("User wins!")
            user_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

        print(f"User: {user_wins} wins.")
        print(f"Computer: {computer_wins} wins.\n")

    return user_wins, computer_wins


if __name__ == "__main__":
    main()
