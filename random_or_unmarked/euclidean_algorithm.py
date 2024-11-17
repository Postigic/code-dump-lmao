def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(gcd(num1, num2))
