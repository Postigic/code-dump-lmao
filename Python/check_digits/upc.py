upc = input("Enter first 11 digits of UPC-A: ")

odd_sum = 0
even_sum = 0

for index in range(11):
    digit = int(upc[index])

    if (index + 1) % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit

check_digit = (odd_sum * 3 + even_sum) % 10

if check_digit != 0:
    check_digit = 10 - check_digit
    
print(check_digit)