from logic import *
from input_validation import *

def main():
    options = {
        "hexadecimal": get_hex_string,
        "tiles": get_tiles_string,
        "mathematics": get_mathematics_string,
        "timing": get_timing_string,
        "multi_buttons": get_multi_buttons_string,
        "binary": get_binary_string,
        "colour_code": get_colour_code_string,
        "keypad": get_keypad_string
    }

    while True:
        print("Defusal Automation Program",
              end="\n\n-------------------------------\n\n")
        choice = input("Select module: ").lower()
        print("\n-------------------------------\n")

        found_match = False
        for key in options:
            if key.startswith(choice):
                options[key]()
                found_match = True
                break

        if not found_match:
            print("Invalid choice. Please try again.",
                  end="\n\n-------------------------------\n\n")


def get_hex_string():
    hex_string = get_valid_hex_string()
    print(f"Alpha string: {hex_to_alpha(hex_string)}",
          end="\n\n-------------------------------\n\n")


def get_tiles_string():
    tiles_string = get_valid_tiles_string()
    print(f"Number: {tiles_to_num(tiles_string)}",
          end="\n\n-------------------------------\n\n")


def get_mathematics_string():
    math_string = get_valid_mathematics_string()
    print(f"Number: {letters_to_num(math_string)}",
          end="\n\n-------------------------------\n\n")


def get_timing_string():
    timing_string = get_valid_timing_string()
    print(f"Colour: {string_to_colour(timing_string)}",
          end="\n\n-------------------------------\n\n")


def get_multi_buttons_string():
    multi_buttons_string = get_valid_multi_buttons_string()
    print(f"Sequence: {numbers_to_sequence(multi_buttons_string)}",
          end="\n\n-------------------------------\n\n")


def get_binary_string():
    binary_string = get_valid_binary_string()
    print(f"Number: {binary_to_num(binary_string)}",
          end="\n\n-------------------------------\n\n")


def get_colour_code_string():
    light_colours = get_valid_light_colours()
    display_colours = get_valid_display_colours()
    print(f"Number: {colours_to_num(light_colours, display_colours)}",
          end="\n\n-------------------------------\n\n")


def get_keypad_string():
    keypad_string = get_valid_keypad_string()
    print(f"Sequence: {keypad_to_sequence(keypad_string)}",
          end="\n\n-------------------------------\n\n")


if __name__ == "__main__":
    main()
