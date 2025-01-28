def find_check_digit(isbn_chars):
    c_isbn = isbn_chars.replace("-", "")

    isbn_list = list(c_isbn)

    total = 0
    index = 0

    for value in isbn_list:
        total += int(value) * (10 - index)
        index += 1

    check_digit = (11 - (total % 11)) % 11

    if check_digit == 10:
        return "X"
    else:
        return check_digit
    

def validate_isbn(isbn):
    c_isbn = isbn.replace("-", "")

    if len(c_isbn) != 10:
        return False
    
    if not c_isbn[:9].isdigit():
        return False
    
    isbn_list = list(c_isbn)

    if not (isbn_list[9] == 'X' or isbn_list[9].isdigit()):
        return False
    
    if isbn_list[9] == "X":
        isbn_list[9] = "10"

    total = 0
    index = 0

    for value in isbn_list:
        total += int(value) * (10 - index)
        index += 1
        
    return total % 11 == 0


print(find_check_digit("0-8044-2957"))
print(find_check_digit("9971-5-0210"))

print(validate_isbn("0-8044-2957-X"))
print(validate_isbn("9971-5-0230-0"))
