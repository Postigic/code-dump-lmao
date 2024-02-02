while True:
    mark = input("Enter your mark: ")
    if mark.isdigit() and 0 <= (int(mark)) <= 100:
        break
    print("Invalid input. Please enter a valid integer between 0 and 100.")
