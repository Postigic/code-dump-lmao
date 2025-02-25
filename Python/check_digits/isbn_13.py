def find_check_digit(isbn_chars):
    c_isbn = isbn_chars.replace("-", "")

    isbn_list = list(c_isbn)

    total = 0
    index = 0

    for value in isbn_list:
        total += int(value) * (1 if index % 2 == 0 else 3)
        index += 1

    return str((10 - (total % 10)) % 10)


def validate_isbn(isbn):
    c_isbn = isbn.replace("-", "")

    check_digit = find_check_digit(c_isbn[:12])

    return check_digit == c_isbn[12]


print(find_check_digit("978-81-7525-766")) # 5

print(validate_isbn("978-81-7525-766-5")) # True
print(validate_isbn("978-81-7125-766-5")) # False
print(validate_isbn("978-1-234-56789-7")) # True
print(validate_isbn("979-1-234-56789-7")) # False