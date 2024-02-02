while True:
    date = input("Enter date (DD/MM/YYYY): ").split("/")
    days_in_month = {
        "01": 31,
        "02": 28,
        "03": 31,
        "04": 30,
        "05": 31,
        "06": 30,
        "07": 31,
        "08": 31,
        "09": 30,
        "10": 31,
        "11": 30,
        "12": 31
    }
    if len(date) == 3 and all(component.isdigit() for component in date):
        day = int(date[0])
        month = date[1]
        year = int(date[2])

        if month in days_in_month and 1 <= day <= days_in_month[month] and 0 < year <= 2024:
            print("Valid date.")
            break
        else:
            print("Invalid date.")
    else:
        print("Invalid date format. Please use DD/MM/YYYY.")
