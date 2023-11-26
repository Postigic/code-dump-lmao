# IMPORTS

import random

# VARIABLES

NOISE_PROBABILITY = 0.5

# USER INPUT


def bin_str_input():
    while True:
        user_input = input(
            "Enter a valid binary string or generate a random one: ").lower()
        if user_input == "random":
            while True:
                length = input("Enter desired binary string length: ")
                if length.isdigit():
                    return gen_rand_bin_str(int(length))
                else:
                    print("Invalid input. Length must be a number.")
        elif user_input.isdigit() and set(user_input).issubset({"0", "1"}):
            return user_input
        else:
            print("Invalid input. Please enter 'random' or a valid binary string.")


def error_check_choice():
    while True:
        check_type = input("Select an error-checking method: ")
        if check_type.lower() not in {"parity", "checksum", "fcs", "crc"}:
            print("Invalid error-checking method.")
            continue
        return check_type

# PARITY CHECK


def get_parity_choice():
    while True:
        parity_choice = input(
            "Choose between Even or Odd parity check (e, o): ")
        if parity_choice.lower() not in {"e", "o"}:
            print("Invalid input.")
            continue
        return parity_choice


def add_parity_bit(data, parity_choice):
    if parity_choice == "e":
        parity_bit = "0" if data.count("1") % 2 == 0 else "1"
    else:
        parity_bit = "1" if data.count("1") % 2 == 0 else "0"
    return parity_bit + data


def parity_check_data(data, parity_choice):
    total = sum(int(bit) for bit in data)
    if (total % 2 == 0 and parity_choice == 'e') or (total % 2 == 1 and parity_choice == 'o'):
        return "No corruption."
    return "Corruption detected."

# CHECKSUM


def calculate_checksum(data):
    checksum = int(data, 2)
    if checksum > 255:
        checksum = checksum % 256
    return f"{data}, {str(checksum)}"


def checksum_check_data(data):
    split_data = data.split(", ")
    data, checksum = split_data
    recalculated_checksum = calculate_checksum(data)
    if int(checksum) == recalculated_checksum:
        return "No corruption."
    return "Corruption detected."

# FRAME CHECK SEQUENCE

# CYCLIC REDUNDANCY CHECK

# MAIN


def gen_rand_bin_str(length):
    return ''.join(random.choice('01') for _ in range(length))


def add_noise(data):
    probability = random.random()
    if probability < NOISE_PROBABILITY:
        index = random.randint(0, len(data) - 1)
        data_list = list(data)
        data_list[index] = "0" if data_list[index] == "1" else "1"
        data = "".join(data_list)
    return data


if __name__ == "__main__":
    original_data = bin_str_input()
    check_type = error_check_choice()

    if check_type == "parity":
        parity_choice = get_parity_choice()
        parity_data = add_parity_bit(original_data, parity_choice)
        received_data = add_noise(parity_data)
        # ------------------------------------------------------ #
        print(f"Original data: {original_data}")
        print(f"Data with parity bit: {parity_data}")
        print(f"Received data: {received_data}")
        print(parity_check_data(received_data, parity_choice))

    elif check_type == "checksum":
        checksum_data = calculate_checksum(original_data)
        received_data = add_noise(checksum_data)
        # ------------------------------------------------------ #
        print(f"Original data: {original_data}")
        print(f"Data with checksum: {checksum_data}")
        print(f"Received data: {received_data}")
        print(checksum_check_data(checksum_data))
