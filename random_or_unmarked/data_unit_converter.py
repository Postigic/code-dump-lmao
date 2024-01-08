def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError as ve:
            print(f"Value Error: {ve}")


def get_unit(prompt, valid_units):
    while True:
        unit = input(prompt).upper()
        if unit in valid_units:
            return unit
        print("Invalid unit. Enter a valid unit.")


def calculate_conversion(data_size, initial_unit, conversion_unit):
    units = {
        "B": 1,
        "KB": 1000,
        "KIB": 1024,
        "MB": 1000 ** 2,
        "MIB": 1024 ** 2,
        "GB": 1000 ** 3,
        "GIB": 1024 ** 3,
        "TB": 1000 ** 4,
        "TIB": 1024 ** 4,
        "PB": 1000 ** 5,
        "PIB": 1024 ** 5
    }
    initial = units[initial_unit]
    conversion = units[conversion_unit]
    return data_size * initial / conversion


def calculate_bits(data_size, unit):
    bytes_size = calculate_conversion(data_size, unit, "B")
    return bytes_size * 8


def main():
    while True:
        data_size = get_float_input("Enter data size: ")
        valid_units = ["B", "KB", "KIB", "MB", "MIB",
                       "GB", "GIB", "TB", "TIB", "PB", "PIB"]
        initial_unit = get_unit(
            "Enter data unit (B, KB, KIB, MB, MIB, GB, GIB, TB, TIB, PB, PIB): ", valid_units)
        conversion_unit = get_unit(
            "Enter conversion unit (B, KB, KIB, MB, MIB, GB, GIB, TB, TIB, PB, PIB): ", valid_units)

        result = calculate_conversion(
            data_size, initial_unit, conversion_unit)
        bits_result = calculate_bits(
            data_size, initial_unit)

        print(f"Result: {result:.6f} {conversion_unit}")
        print(f"Bits Result: {bits_result:.6f} b")


if __name__ == "__main__":
    main()
