from math import sqrt

def binets_formula(n):
    return round((1 / sqrt(5)) * ((((1 + sqrt(5)) / 2) ** n) - (((1 - sqrt(5)) / 2) ** n)))

n = int(input("Enter the value of n: "))
print(binets_formula(n))