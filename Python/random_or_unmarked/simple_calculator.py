def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError as ve:
            print(f"Value Error: {ve}")


def get_operator(prompt):
    while True:
        operator = input(prompt)
        if operator in ["+", "-", "*", "/"]:
            return operator
        print("Invalid operator. Enter a valid operator.")


def calculate_result(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        return num1 / num2


def main():
    while True:
        num1 = get_float_input("Enter first number: ")
        num2 = get_float_input("Enter second number: ")
        operator = get_operator("Enter operator (+, -, *, /): ")
        try:
            result = calculate_result(num1, num2, operator)
            print(f"Result: {result}")
            break
        except ZeroDivisionError as zde:
            print(f"Zero Division Error: {zde}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()


"""""
Old code, ignore

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operator (+, -, *, /): ")

        if operation not in ["+", "-", "*", "/"]:
            raise ValueError("Invalid operator.")
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        else:
            result = num1 / num2

        print(f"Result: {result}")
        break

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Zero Division Error: {zde}")
    except Exception as e:
        print(f"An error occured: {e}")
"""""
