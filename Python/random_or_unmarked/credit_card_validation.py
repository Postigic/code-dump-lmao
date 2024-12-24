while True:
    digits = input("Enter credit card number: ").split("-")

    if len(digits) == 4 and all(i.isdigit() and len(i) == 4 for i in digits):
        print("Valid credit card number")
        break
    else:
        print("Invalid credit card number")
