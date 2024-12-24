def test_sort(func):
    if func([1, 6, 4, 3, 7, 9, 10, 2, 4, 6, 5]) == [1, 2, 3, 4, 4, 5, 6, 6, 7, 9, 10]:
        print(f"{func.__name__}:\t Pass ✅")
    else:
        print(f"{func.__name__}:\t Fail ❌")


def bubble_sort(arr):
    size = len(arr)

    for i in range(size):
        for j in range(0, size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


test_sort(bubble_sort)


def selection_sort(arr):
    size = len(arr)

    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


test_sort(selection_sort)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


test_sort(insertion_sort)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


test_sort(merge_sort)


def count_sort(arr):
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

    return sorted_arr


test_sort(count_sort)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


test_sort(heap_sort)
