# IMPORTS

import random

# VARIABLES

NOISE_PROBABILITY = 0.5

# FUNCTIONS


def get_binary_string():
    while True:
        original_data = input("Enter a valid binary string: ")
        if not original_data.isdigit() or not set(original_data).issubset({'0', '1'}):
            print("Invalid binary string. Please enter a valid binary string.")
            continue
        break
    return original_data


def get_parity_choice():
    while True:
        parity_choice = input(
            "Choose between Even or Odd parity check (e, o): ")
        if parity_choice.lower() not in {"e", "o"}:
            print("Invalid input.")
            continue
        break
    return parity_choice


def add_parity_bit(data, parity_choice):
    if parity_choice == "e":
        parity_bit = "0" if data.count("1") % 2 == 0 else "1"
    else:
        parity_bit = "1" if data.count("1") % 2 == 0 else "0"
    return parity_bit + data


def add_noise(data):
    probability = random.random()
    if probability < NOISE_PROBABILITY:
        index = random.randint(0, len(data) - 1)
        data_list = list(data)
        data_list[index] = "0" if data_list[index] == "1" else "1"
        data = "".join(data_list)
    return data


def check_data(data, parity_choice):
    total = sum(int(bit) for bit in data)
    if (total % 2 == 0 and parity_choice == 'e') or (total % 2 == 1 and parity_choice == 'o'):
        return "No corruption."
    return "Corruption detected."


if __name__ == "__main__":
    original_data = get_binary_string()
    parity_choice = get_parity_choice()
    parity_data = add_parity_bit(original_data, parity_choice)
    received_data = add_noise(parity_data)
    # ------------------------------------------------------ #
    print(f"Original data: {original_data}")
    print(f"Data with parity bit: {parity_data}")
    print(f"Received data: {received_data}")
    print(check_data(received_data, parity_choice))
