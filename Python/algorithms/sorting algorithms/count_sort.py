from algorithm_tester import test_sort

def count_sort(arr):
    if not arr:
        return []

    min_num = min(arr)
    if min_num < 0:
        shift = -min_num
        arr = [num + shift for num in arr]
    else:
        shift = 0

    max_num = max(arr)
    count_arr = [0] * (max_num + 1)

    for num in arr:
        count_arr[num] += 1

    for i in range(1, max_num + 1):
        count_arr[i] += count_arr[i - 1]

    sorted_arr = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        sorted_arr[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1

    sorted_arr = [num - shift for num in sorted_arr]
    return sorted_arr

test_sort(count_sort)