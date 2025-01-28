def find_check_digit(isbn_chars):
    c_isbn = isbn_chars.replace("-", "")

    isbn_list = list(c_isbn)

    total = 0
    index = 0

    for value in isbn_list:
        total += int(value) * (1 if index % 2 == 0 else 3)
        index += 1

    return (10 - (total % 10)) % 10


def validate_isbn(isbn):
    c_isbn = isbn.replace("-", "")

    isbn_list = list(c_isbn)

    total = 0
    index = 0

    for value in isbn_list:
        total += int(value) * (1 if index % 2 == 0 else 3)
        index += 1

    return total % 10 == 0


print(find_check_digit("978-81-7525-766")) # 5

print(validate_isbn("978-81-7525-766-5")) # True
print(validate_isbn("978-81-7125-766-5")) # False