CONVERSION_FACTOR = 0.45359237


def kg_to_lb(x, conversion_factor=CONVERSION_FACTOR):
    return x / conversion_factor


def lb_to_kg(x, conversion_factor=CONVERSION_FACTOR):
    return x * conversion_factor


print("Select type:")
print("1. Kilograms to Pounds")
print("2. Pounds to Kilograms")

while True:
    choice = input("Enter choice (1/2): ")
    if choice in ['1', '2']:
        while True:
            try:
                x = float(input("Enter weight: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if choice == '1':
            print(f"{x} kg = {kg_to_lb(x):.10f} pounds")
        elif choice == '2':
            print(f"{x} pounds = {lb_to_kg(x):.10f} kg")

        next_calculation = input("Continue with calculations? (yes/no): ")
        if next_calculation.lower() == "no":
            break
    else:
        print("Invalid choice. Please enter 1 or 2.")
