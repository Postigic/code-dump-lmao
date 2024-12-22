import string
import random
import time
import sys

style = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "RESET": "\033[0m"
}


def flip_sign(text):
    # Full set of printable characters (letters, digits, punctuation, and space)
    letters = string.printable  # This includes digits, punctuation, and whitespace
    result = ""  # Start with an empty result
    clear_screen = "\033[H\033[J"  # ANSI escape sequence to clear screen

    for letter in text:
        # Check if the character is a visible character (not whitespace or tab)
        if letter in string.whitespace:
            # If it's a whitespace, don't flip; just append it directly
            result += letter
            # Update the screen with the correct result
            sys.stdout.write(clear_screen + result)
            sys.stdout.flush()
            time.sleep(0.1)  # Slight pause before the next character
        else:
            # Randomly cycle through characters for a set amount of iterations
            for _ in range(10):  # Adjust this for speed control (number of random characters shown)
                random_letter = random.choice(letters)
                # Update the line with random letter
                sys.stdout.write(clear_screen + result + random_letter)
                sys.stdout.flush()  # Ensure the output is written immediately
                time.sleep(0.02)  # Shorter delay for quicker effect

            # After showing random letters, append the correct one
            result += letter
            # Update the screen with the correct result
            sys.stdout.write(clear_screen + result)
            sys.stdout.flush()
            time.sleep(0.05)  # Slight pause before the next character

    sys.stdout.write(clear_screen + result)  # Final correct text
    sys.stdout.flush()


def slow_print(text, speed, colour=""):
    for character in text:
        print(colour + character + style["RESET"], end="", flush=True)
        time.sleep(speed)


def transform_text(text):
    # Convert the text to binary
    binary_result = ''.join(format(ord(c), '08b') for c in text)
    # Convert the text to hexadecimal
    hex_result = ''.join(format(ord(c), '02x') for c in text)

    # Define the maximum length to clear the entire line
    max_len = max(len(binary_result), len(hex_result), len(text))

    # Print Binary first
    sys.stdout.write(
        style["CYAN"] + binary_result.ljust(max_len) + style["RESET"])
    sys.stdout.flush()
    time.sleep(1)

    # Clear the line by overwriting with spaces and print Hexadecimal
    # Clear the line by overwriting with spaces
    sys.stdout.write("\r" + " " * max_len)
    sys.stdout.write("\r" + style["MAGENTA"] +
                     hex_result.ljust(max_len) + style["RESET"])
    sys.stdout.flush()
    time.sleep(1)

    # Clear the line and print Plain Text
    sys.stdout.write("\r" + " " * max_len)  # Clear the line again
    sys.stdout.write("\r" + style["GREEN"] +
                     text.ljust(max_len) + style["RESET"])
    sys.stdout.flush()


def slow_print_with_random_speed(text, colour=""):
    for character in text:
        # Random speed between 0.02 and 0.1 seconds
        speed = random.uniform(0.02, 0.1)
        print(colour + character + style["RESET"], end="", flush=True)
        time.sleep(speed)


flip_sign("Welcome to...")
print("\n")
time.sleep(0.5)
slow_print("""
 ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗   ██╗████████╗██╗███╗   ██╗ ██████╗ ██╗
██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║   ██║╚══██╔══╝██║████╗  ██║██╔════╝ ██║
██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║   ██║   ██║██╔██╗ ██║██║  ███╗██║
██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║   ██║   ██║   ██║██║╚██╗██║██║   ██║╚═╝
╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ╚██████╔╝   ██║   ██║██║ ╚████║╚██████╔╝██╗
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝
                                                                               """, 0.005, style["YELLOW"])
print("\n")
transform_text("Data Representation!")
