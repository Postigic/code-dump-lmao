def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if arr[low] == arr[high]:
            if arr[low] == target:
                return low
            else:
                return -1
            
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

print(interpolation_search([1, 2, 3, 4, 5], 3))