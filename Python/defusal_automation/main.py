from operator import index

from logic import *
from input_validation import *

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

def display_result(message: str, color: str = YELLOW) -> None:
    print(f"{color if color else YELLOW}{message}{RESET}\n")

def get_hex_string() -> None:
    hex_string = get_valid_hex_string()
    display_result(f"\nAlpha string: {hex_to_alpha(hex_string)}")

def get_tiles_string() -> None:
    tiles_string = get_valid_tiles_string()
    display_result(f"\nNumber: {tiles_to_num(tiles_string)}")

def get_mathematics_string() -> None:
    math_string = get_valid_mathematics_string()
    display_result(f"\nNumber: {letters_to_num(math_string)}")

def get_timing_string() -> None:
    timing_string = get_valid_timing_string()
    display_result(f"\nColour: {string_to_colour(timing_string)}")

def get_multi_buttons_string() -> None:
    multi_buttons_string = get_valid_multi_buttons_string()
    display_result(f"\nSequence: {numbers_to_sequence(multi_buttons_string)}")

def get_binary_string() -> None:
    binary_string = get_valid_binary_string()
    display_result(f"\nNumber: {binary_to_num(binary_string)}")

def get_colour_code_string() -> None:
    light_colours = get_valid_light_colours()
    display_colours = get_valid_display_colours()
    display_result(f"\nNumber: {colours_to_num(light_colours, display_colours)}")

def get_keypad_string() -> None:
    keypad_string = get_valid_keypad_string()
    display_result(f"\nSequence: {keypad_to_sequence(keypad_string)}")

def get_divisibility_string() -> None:
    for _ in range(3):
        divisibility_string = get_valid_divisibility_string()
        display_result(f"\nNumber: {number_to_button(divisibility_string)}")

OPTIONS = {
    "hexadecimal": get_hex_string,
    "tiles": get_tiles_string,
    "mathematics": get_mathematics_string,
    "timing": get_timing_string,
    "multi_buttons": get_multi_buttons_string,
    "binary": get_binary_string,
    "colour_code": get_colour_code_string,
    "keypad": get_keypad_string,
    "divisibility": get_divisibility_string
}

MODULE_LIST = list(OPTIONS.keys())

def list_modules() -> None:
    print("\nAvailable modules:")
    for i, key in enumerate(MODULE_LIST, 1):    
        print(f"    {i}. {key}")

    print()

def resolve_choice(choice: str) -> str | None:
    if choice.isdigit():
        idx = int(choice) - 1

        if 0 <= idx < len(MODULE_LIST):
            return MODULE_LIST[idx]
        
        return None
    
    matches = [key for key in MODULE_LIST if key.startswith(choice)]
    return matches[0] if len(matches) == 1 else None

def main() -> None:
    print(f"{CYAN}{'-'*40}\nDefusal Automation\n{'-'*40}{RESET}")

    list_modules()

    while True:
        choice = input("Select module (index or name, 'modules' to list, 'quit'/'q' to quit): ").lower().strip()

        if choice in ("quit", "q"):
            break

        if choice == "modules":
            list_modules()
            continue

        key = resolve_choice(choice)

        if key:
            OPTIONS[key]()
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")
            
if __name__ == "__main__":
    main()
