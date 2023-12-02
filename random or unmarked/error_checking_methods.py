# IMPORTS

import random

# VARIABLES

NOISE_PROBABILITY = 0.5

# USER INPUT


def binary_string_input():
    while True:
        user_input = input(
            "Enter a valid binary string or generate a random one: ").lower()
        if user_input == "random":
            while True:
                length = input("Enter desired binary string length: ")
                if length.isdigit():
                    return generate_random_binary_string(int(length))
                else:
                    print("Invalid input. Length must be a number.")
        elif user_input.isdigit() and set(user_input).issubset({"0", "1"}):
            return user_input
        else:
            print("Invalid input. Please enter 'random' or a valid binary string.")


def error_check_choice():
    while True:
        check_type = input(
            "Select an error-checking method (parity, checksum): ")
        if check_type.lower() not in {"parity", "checksum"}:
            print("Invalid error-checking method.")
            continue
        return check_type

# PARITY CHECK


def get_parity():
    while True:
        parity_choice = input(
            "Choose between Even or Odd parity check (e, o): ")
        if parity_choice.lower() not in {"e", "o"}:
            print("Invalid input.")
            continue
        return parity_choice


def add_parity_bit(binary_data, parity):
    count_of_ones = binary_data.count("1")
    if parity == "e":
        parity_bit = "0" if count_of_ones % 2 == 0 else "1"
    else:
        parity_bit = "1" if count_of_ones % 2 == 0 else "0"
    return parity_bit + binary_data


def parity_check_data(binary_data, parity):
    total_sum = sum(int(bit) for bit in binary_data)
    if (total_sum % 2 == 0 and parity == 'e') or (total_sum % 2 == 1 and parity == 'o'):
        return "No corruption detected."
    return "Corruption detected."

# CHECKSUM


def calculate_checksum(binary_data):
    checksum = int(binary_data, 2)
    if checksum > 255:
        checksum = checksum % 256
    return f"{binary_data}, {str(checksum)}"


def checksum_check_data(binary_data):
    received_data, checksum_str = binary_data.split(", ")
    recalculated_checksum = calculate_checksum(received_data)
    if int(checksum_str) == int(recalculated_checksum.split(", ")[1]):
        return "No corruption."
    return "Corruption detected."


# MAIN


def generate_random_binary_string(length):
    return ''.join(random.choice('01') for _ in range(length))


def add_noise(binary_data):
    probability = random.random()
    if probability < NOISE_PROBABILITY:
        index = random.randint(0, len(binary_data) - 1)
        binary_data = binary_data[:index] + ("0" if binary_data[index] ==
                                             "1" else "1") + binary_data[index+1:]
    return binary_data


if __name__ == "__main__":
    binary_string = binary_string_input()
    error_check_type = error_check_choice()

    if error_check_type == "parity":
        parity_choice = get_parity()
        parity_data = add_parity_bit(binary_string, parity_choice)
        received_data = add_noise(parity_data)
        # ------------------------------------------------------ #
        print(f"Original data: {binary_string}")
        print(f"Data with parity bit: {parity_data}")
        print(f"Received data: {received_data}")
        print(parity_check_data(received_data, parity_choice))

    elif error_check_type == "checksum":
        checksum_data = calculate_checksum(binary_string)
        received_data = add_noise(checksum_data)
        # ------------------------------------------------------ #
        print(f"Original data: {binary_string}")
        print(f"Data with checksum: {checksum_data}")
        print(f"Received data: {received_data}")
        print(checksum_check_data(checksum_data))
