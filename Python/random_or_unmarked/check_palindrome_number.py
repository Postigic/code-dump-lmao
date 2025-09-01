def check_palindrome_number(num):
    if num < 0:
        return False
    
    original = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    return rev == original

print(check_palindrome_number(121))  # True
print(check_palindrome_number(-121)) # False
print(check_palindrome_number(10))   # False
print(check_palindrome_number(12321)) # True
