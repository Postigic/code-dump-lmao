from logic import *
from input_validation import *

STYLE = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "RESET": "\033[0m"
}

def display_result(message: str, color: str = "YELLOW") -> None:
    print(f"{STYLE.get(color, STYLE['YELLOW'])}{message}{STYLE['RESET']}", end="\n\n-------------------------------\n\n")

def get_hex_string() -> None:
    hex_string = get_valid_hex_string()
    display_result(f"Alpha string: {hex_to_alpha(hex_string)}")

def get_tiles_string() -> None:
    tiles_string = get_valid_tiles_string()
    display_result(f"Number: {tiles_to_num(tiles_string)}")

def get_mathematics_string() -> None:
    math_string = get_valid_mathematics_string()
    display_result(f"Number: {letters_to_num(math_string)}")

def get_timing_string() -> None:
    timing_string = get_valid_timing_string()
    display_result(f"Colour: {string_to_colour(timing_string)}")

def get_multi_buttons_string() -> None:
    multi_buttons_string = get_valid_multi_buttons_string()
    display_result(f"Sequence: {numbers_to_sequence(multi_buttons_string)}")

def get_binary_string() -> None:
    binary_string = get_valid_binary_string()
    display_result(f"Number: {binary_to_num(binary_string)}")

def get_colour_code_string() -> None:
    light_colours = get_valid_light_colours()
    display_colours = get_valid_display_colours()
    display_result(f"Number: {colours_to_num(light_colours, display_colours)}")

def get_keypad_string() -> None:
    keypad_string = get_valid_keypad_string()
    display_result(f"Sequence: {keypad_to_sequence(keypad_string)}")

def show_modules() -> None:
    print("Available modules:")
    for key in ["hexadecimal", "tiles", "mathematics", "timing",
                "multi_buttons", "binary", "colour_code", "keypad"]:
        print(f"- {key}")
    print("\n-------------------------------\n")

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

def main() -> None:
    print(f"{STYLE['CYAN']}Defusal Automation Program{STYLE['RESET']}")
    print("\n-------------------------------\n")

    show_modules()

    while True:
        choice = input("Select module ('modules' to show available modules, 'quit' or 'q' to quit): ").lower().strip()

        print("\n-------------------------------\n")

        if choice in ("quit", "q"):
            print(f"{STYLE['GREEN']}Goodbye!{STYLE['RESET']}")
            break

        if choice == "modules":
            show_modules()
            continue

        found_match = False
        for key in options:
            if key.startswith(choice):
                options[key]()
                found_match = True
                break

        if not found_match:
            print(f"{STYLE['RED']}Invalid choice. Please try again.{STYLE['RESET']}",
                  end="\n\n-------------------------------\n\n")
            
if __name__ == "__main__":
    main()
