def keypad_to_sequence(keypad_string):
    num1, num2, num3, num4 = map(int, keypad_string.split())
    x = 0
    y = (sum(int(number) for number in keypad_string.split()))/2

    if num1 < 10:
        x = 15
    elif 10 <= num1 <= 20:
        x = 20
    elif 20 < num1 <= 80:
        x = 30
    else:
        x = 10

    if num2 < 10:
        x += 10
    elif 10 <= num2 <= 20:
        x *= 2
    elif 20 < num2 <= 80:
        x *= 3
    else:
        x -= 10

    if num3 < 10:
        x *= 2
    elif 10 <= num3 <= 20:
        x *= 3
    elif 20 < num3 <= 80:
        x -= 5

    if num4 < 10:
        x *= 2
    elif 10 <= num4 <= 20:
        x += 20
    elif 20 < num4 <= 80:
        x += 50
    else:
        x *= 3

    z = x - y

    if z <= 0:
        return "Top Left, Top Right, Bottom Left, Bottom Right"
    elif 0.5 <= z <= 19.5:
        return "Top Left, Top Right, Bottom Right, Bottom Left"
    elif 20 <= z <= 49.5:
        return "Bottom Right, Bottom Left, Top Right, Top Left"
    elif 50 <= z <= 89.5:
        return "Bottom Left, Top Left, Bottom Right, Top Right"
    else:
        return "Top Right, Bottom Left, Top Left, Bottom Right"
