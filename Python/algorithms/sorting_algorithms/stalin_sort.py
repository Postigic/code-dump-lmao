from algorithm_tester import test_sort

def stalin_sort(arr):
    if len(arr) == 0:
        return []

    sorted_arr = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] >= sorted_arr[-1]:
            sorted_arr.append(arr[i])
            
    return sorted_arr

test_sort(stalin_sort)
