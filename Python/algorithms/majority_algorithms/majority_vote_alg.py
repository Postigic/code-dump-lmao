def find_majority(arr):
    candidate = -1
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    count = 0
    for num in arr:
        if num == candidate:
            count += 1

    if count > len(arr) // 2:
        return candidate
    else:
        return -1

print(find_majority([1, 2, 1, 1, 3, 4, 0, 1, 1]))  # 1
print(find_majority([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # -1
