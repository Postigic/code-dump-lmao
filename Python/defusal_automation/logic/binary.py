def binary_to_num(binary_string):
    if all(digit == "0" for digit in binary_string):
        return 1
    elif binary_string[1] == "1" and binary_string[6] == "0":
        return 2
    elif binary_string[:2] == "11":
        return 3
    elif binary_string[0] == "0" and binary_string[6] == "0":
        return 4
    elif binary_string[:3] == "111":
        return 5
    elif binary_string[:4] == "1111":
        return 6
    elif binary_string.count("0") > 3:
        return 7
    elif binary_string.count("1") > 5:
        return 8
    elif all(digit == "1" for digit in binary_string):
        return 9
    else:
        return 10
