from algorithm_tester import test_sort


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                swap(arr, i, j)

        partition_i = i + 1

        swap(arr, partition_i, high)

        quick_sort(arr, low, partition_i - 1)
        quick_sort(arr, partition_i + 1, high)

    return arr


test_sort(quick_sort)