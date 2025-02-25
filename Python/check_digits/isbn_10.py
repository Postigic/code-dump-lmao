def find_check_digit(isbn_chars: str) -> str:
    c_isbn = isbn_chars.replace('-', '')

    isbn_list = list(c_isbn)

    total = 0
    index = 0

    for value in isbn_list:
        total += int(value) * (10 - index)
        index += 1

    check_digit = (11 - (total % 11)) % 11

    if check_digit == 10:
        return 'X'
    else:
        return str(check_digit)
    

def validate_isbn(isbn: str) -> bool:
    c_isbn = isbn.replace('-', '')

    if len(c_isbn) != 10:
        return False
    
    if not c_isbn[:9].isdigit():
        return False
    
    if not (c_isbn[9] == 'X' or c_isbn[9].isdigit()):
        return False
    
    check_digit = find_check_digit(c_isbn[:9])

    return check_digit == c_isbn[9]


print(find_check_digit("0-8044-2957"))
print(find_check_digit("9971-5-0210"))

print(validate_isbn("0-8044-2957-X"))
print(validate_isbn("0-8044-2955-X"))
print(validate_isbn("9971-5-0210-0"))
print(validate_isbn("9971-5-0230-0"))
