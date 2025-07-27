from math import sqrt

def check_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

print(check_prime(2))
print(check_prime(5))
print(check_prime(8))
print(check_prime(10))
print(check_prime(11))
print(check_prime(15))
print(check_prime(1877))
print(check_prime(2000))
print(check_prime(2000000))
print(check_prime(1000003))
print(check_prime(200000000001))
