def frac_to_deci(frac):
    return str(frac[0] / frac[1])


def next_approx(frac1, frac2, n):
    numerator = (n**2) * frac1[0] + (2 * n + 1) * frac2[0]
    denominator = (n**2) * frac1[1] + (2 * n + 1) * frac2[1]
    return [numerator, denominator]


first_approx = [4, 1]
second_approx = [12, 4]
n = int(input("Enter the value of n: "))
frac1 = first_approx
frac2 = second_approx

for i in range(2, n + 1):
    get_next_approx = next_approx(frac1, frac2, i)
    frac1 = frac2
    frac2 = get_next_approx
print(get_next_approx)

nth_approx = frac_to_deci(get_next_approx)
prev_approx = frac_to_deci(frac1)

duplicate_chars = ""
for i in range(len(nth_approx)):
    if nth_approx[i] == prev_approx[i]:
        duplicate_chars += nth_approx[i]
    else:
        break

print(duplicate_chars)
