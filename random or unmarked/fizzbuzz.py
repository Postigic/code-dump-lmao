def fizzbuzz(begin, finish):
    for i in range(begin, finish + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if i % 7 == 0:
            output += "Fuzz"
        if i % 11 == 0:
            output += "Bizz"
        if i % 13 == 0:
            output += "Biff"
        if output == "":
            output = i
        print(output)


if __name__ == "__main__":
    while True:
        begin = input("Enter the starting number: ")
        finish = input("Enter the ending number: ")
        try:
            begin, finish = int(begin), int(finish)
            if begin > finish:
                raise ValueError(
                    "Starting number cannot be greater than ending number.")
        except ValueError as ve:
            print(f"Value Error: {ve}")
            continue
        fizzbuzz(begin, finish)
        break
