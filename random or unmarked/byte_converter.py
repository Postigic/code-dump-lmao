def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError as ve:
            print(f"Value Error: {ve}")


def get_unit(prompt, valid_units):
    while True:
        unit = input(prompt)
        if unit.upper() in valid_units:
            return unit.upper()
        print("Invalid unit. Enter a valid unit.")


def get_conversion_factor(prompt, valid_factors):
    while True:
        try:
            factor = float(input(prompt))
            if factor in valid_factors:
                return factor
            else:
                print("Invalid conversion factor. Enter a valid conversion factor.")
        except ValueError:
            print("Invalid conversion factor. Enter a valid conversion factor.")


def calculate_bytes(data_size, initial_unit, conversion_unit, conversion_factor):
    units = {
        "B": 1,
        "KB": conversion_factor,
        "MB": conversion_factor ** 2,
        "GB": conversion_factor ** 3,
        "TB": conversion_factor ** 4,
    }
    initial_bytes = units[initial_unit]
    conversion_bytes = units[conversion_unit]
    return data_size * initial_bytes / conversion_bytes


def main():
    data_size = get_float_input("Enter data size: ")
    valid_units = ["B", "KB", "MB", "GB", "TB"]
    initial_unit = get_unit(
        "Enter data unit (B, KB, MB, GB, TB): ", valid_units)
    conversion_unit = get_unit(
        "Enter conversion unit (B, KB, MB, GB, TB): ", valid_units)
    valid_factors = [1000, 1024]
    conversion_factor = get_conversion_factor(
        "Enter conversion factor (1000 or 1024): ", valid_factors)
    result = calculate_bytes(data_size, initial_unit,
                             conversion_unit, conversion_factor)
    print(f"Result: {result:.6f} {conversion_unit}")


if __name__ == "__main__":
    main()
