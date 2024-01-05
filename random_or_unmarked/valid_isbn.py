def is_valid(isbn):
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
    rc_isbn = isbn_list[::-1]
    total = 0
    for index, value in enumerate(rc_isbn):
        total += int(value) * (10 - index)
    return total % 11 == 0


is_valid("3-598-21507-X")
# 10, 14, 0, 20, 5, 12, 56, 72, 45, 30
# 264
