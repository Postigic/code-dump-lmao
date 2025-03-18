max_width = 100

for i in range(0, max_width, 2):
    print(" " * ((max_width - (i + 1)) // 2) + "*" * (i + 1))