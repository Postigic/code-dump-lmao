def get_valid_hex_string() -> str:
    while True:
        hex_string = input("Enter hex string (e.g. 62 6F 6F 70): ").upper()
        stripped_hex_string = hex_string.replace(" ", "")

        if all(char in "0123456789ABCDEF" for char in stripped_hex_string) and len(stripped_hex_string) == 8:
            return hex_string
        else:
            print("Invalid hex string. Please enter a valid hex string.")

def get_valid_tiles_string() -> str:
    while True:
        tiles_string = input("Enter tiles string (e.g. R G): ").upper().replace(" ", "")

        if all(char in "RGBYPW" for char in tiles_string) and len(tiles_string) == 2:
            return tiles_string
        else:
            print("Invalid tiles string. Please enter a valid tiles string.")

def get_valid_mathematics_string() -> str:
    while True:
        math_string = input(
            "Enter math string (e.g. AB DH): ").upper().replace(" ", "")
        if all(char in "ABCDEFGHIJ" for char in math_string) and len(math_string) == 4:
            return math_string
        else:
            print("Invalid math string. Please enter a valid math string.")

def get_valid_timing_string() -> str:
    while True:
        timing_string = input("Enter timing string (e.g. 16 BC): ").upper().replace(" ", "")
        pair1, pair2 = timing_string[:2], timing_string[2:]

        if all(char in "01234567890" for char in pair1) and all(char in "ABCD" for char in pair2) and len(pair1) == 2 and len(pair2) == 2:
            return timing_string
        else:
            print("Invalid timing string. Please enter a valid timing string.")

def get_valid_multi_buttons_string() -> str:
    while True:
        multi_buttons_string = input("Enter multi buttons string (e.g. 128587): ")
        
        if multi_buttons_string.isdigit() and len(multi_buttons_string) == 6:
            return multi_buttons_string
        else:
            print("Invalid multi buttons string. Please enter a valid multi buttons string.")

def get_valid_binary_string() -> str:
    while True:
        binary_string = input("Enter binary string (e.g. 1001110): ")

        if all(char in "01" for char in binary_string) and len(binary_string) == 7:
            return binary_string
        else:
            print("Invalid binary string. Please enter a valid binary string.")

def get_valid_light_colours() -> str:
    while True:
        light_colours = input("Enter light colours (e.g. RGBYW): ").upper()

        if len(light_colours) == 5 and all(char in "RGBYW" for char in light_colours):
            return light_colours
        else:
            print("Invalid light colours. Please enter valid light colours.")

def get_valid_display_colours() -> str:
    while True:
        display_colours = input("Enter display colours (e.g. GGWYB): ").upper()

        if len(display_colours) == 5 and all(char in "RGBYW" for char in display_colours):
            return display_colours
        else:
            print("Invalid display colours. Please enter valid display colours.")

def get_valid_keypad_string() -> str:
    while True:
        keypad_string = input("Enter keypad string (e.g. 12 85 87 0): ").upper()
        spaces = keypad_string.count(" ")

        if spaces == 3 and all(char in "0123456789" for char in keypad_string.replace(" ", "")):
            return keypad_string
        else:
            print("Invalid keypad string. Please enter valid keypad string.")

def get_valid_divisibility_string() -> str: # don't question my naming conventions cause i dunno either okay
    while True:
        divisibility_string = input("Enter number: ")

        if divisibility_string.isdigit():
            return int(divisibility_string)
        else:
            print("Invalid input. Please enter a valid number.")
