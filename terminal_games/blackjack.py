# IMPORTS

import random
import time
import sys

# FUNCTIONS


def game_info():
    print("Great! Let me explain the rules.")
    time.sleep(2)
    print("The rules are simple! You and the computer get two random cards at the start.")
    time.sleep(2)
    print("You can choose to draw or end the game during your turn.")
    time.sleep(2)
    print("If the sum of all the cards goes over 21, you lose.")
    time.sleep(2)
    print("You win when all your cards add up to 21 or the computer goes over 21!")
    time.sleep(2)
    print("Oh yeah! Before I forget!")
    time.sleep(2)
    print("Next time you come back, you can just type 'Skip' at the start to skip this dialogue!")
    time.sleep(2)
    print("Although I hope you don't skip me because that would make me sad :(")
    time.sleep(2)
    print("Anyways, let's begin!")
    time.sleep(2)
    print("-- INITIALISING GAME --")
    time.sleep(2)


def deal_card():
    return random.randint(1, 11)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def blackjack_game():
    player_cards = []
    dealer_cards = []
    game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        time.sleep(1)
        print(f"Your cards: {player_cards}")
        time.sleep(1)
        print(f"Total: {player_score}")
        time.sleep(1)
        print(f"Dealer's first card: {dealer_cards[0]}")
        time.sleep(1)

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            print("Do you want to draw a card?")
            shouldContinue = input("Yes/No: ").lower()
            if shouldContinue in ["yes", "y", "yeah"]:
                player_cards.append(deal_card())
            elif shouldContinue in ["no", "n", "nope"]:
                game_over = True
            else:
                print("Type 'Yes' or 'No' you moron! >:(")

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    time.sleep(1)
    print("-- GAME OVER --")
    time.sleep(1)
    print(f"Your final hand: {player_cards}")
    time.sleep(1)
    print(f"Total: {player_score}")
    time.sleep(1)
    print(f"Dealer's final hand: {dealer_cards}")
    time.sleep(1)
    print(f"Total: {dealer_score}")
    time.sleep(1)

    if player_score > 21:
        print("Bust! You went over 21. You lose!")
    elif dealer_score > 21:
        print("Dealer busts! You win!")
    elif player_score == dealer_score:
        print("It's a draw!")
    elif player_score == 0:
        print("Blackjack! You win!")
    elif dealer_score == 0:
        print("Dealer got a Blackjack. You lose!")
    elif player_score > dealer_score:
        print("You win!")
    else:
        print("You lose!")

    sys.exit()

# seperation line for the funnies


print("Hello! Do you want to play my game?")

while True:
    start_prompt = input("Yes/No: ").lower()
    if start_prompt in ["yes", "y", "yeah"]:
        game_info()

    elif start_prompt in ["no", "n", "nope"]:
        print("Aww... Hope you come play next time then!")
        time.sleep(1)
        sys.exit()

    elif start_prompt in ["skip", "s"]:
        print("Ah! Welcome back! I hope you had fun last time!")
        time.sleep(2)
        print("Let's get right to the game!")
        time.sleep(2)
        print("-- INITIALISING GAME --")
        time.sleep(2)

    else:
        print("You need to type 'Yes' or 'No'. >:(")
        time.sleep(1)
        continue

    blackjack_game()
