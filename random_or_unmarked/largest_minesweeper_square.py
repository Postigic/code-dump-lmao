def get_dimension_input(prompt):
    while True:
        try:
            dimension = int(input(prompt))
            return dimension
        except ValueError as ve:
            print(f"Value Error: {ve}")


def calculate_largest_square(dimension):
    return 3 ** dimension - 1


def main():
    dimension = get_dimension_input("Enter dimension: ")
    largest = calculate_largest_square(dimension)
    print(largest)


if __name__ == "__main__":
    main()
