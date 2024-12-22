def get_num_rounds():
    valid_input = False

    while not valid_input:
        s = input("Enter the number of shuffling rounds: ")
        if not s.isdigit():
            print("Input must be a positive integer. Please try again.")
        else:
            return int(s)


def get_n():
    valid_input = False

    while not valid_input:
        n = input("Enter the number of glasses from 6 to 26 inclusive: ")
        if not n.isdigit() or not (6 <= int(n) <= 26):
            print("Input must be between 6 and 26 inclusive. Please try again.")
        else:
            return int(n)


def fill_glasses(n):
    my_glasses = [chr(i) for i in range(65, 65 + n)]
    return my_glasses


def get_abg(n):
    valid_input = False

    while not valid_input:
        abg = input("Enter the positions of the glasses (a b g): ").split()

        if len(abg) != 3 or any(not x.isdigit() for x in abg):
            print("Input must be three integers separated by spaces. Please try again.")
            continue

        a, b, g = map(int, abg)

        if any(x < 0 or x >= n for x in (a, b, g)) or len({a, b, g}) != 3:
            print(
                f"All three inputs must be unique integers between 0 and {n - 1} inclusive. Please try again.")
        else:
            return a, b, g


def shuffle(glasses, a, b, g):
    glasses[a], glasses[b], glasses[g] = glasses[g], glasses[a], glasses[b]

    return glasses


s = get_num_rounds()
n = get_n()
glasses = fill_glasses(n)

for _ in range(s):
    a, b, g = get_abg(n)
    updated_glasses = shuffle(glasses, a, b, g)
    print(f"The glass in position 5 contains flavour {updated_glasses[4]}.")

unchanged_count = 0
for pos in range(len(glasses)):
    if glasses[pos] == updated_glasses[pos]:
        unchanged_count += 1

print(
    f"The number of glasses remaining in the same position is {unchanged_count}")


# O(n)
