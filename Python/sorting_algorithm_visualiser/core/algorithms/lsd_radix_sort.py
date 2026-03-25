def lsd_radix_sort(state):
    arr = state.arr
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        is_last = (max_num // (exp * 10) == 0)
        yield from _counting_sort(state, arr, exp, is_last)
        exp *= 10

def _counting_sort(state, arr, exp, is_last=False):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i, num in enumerate(arr):
        digit = (num // exp) % 10
        count[digit] += 1
        state.active = {i}
        yield
    
    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    for i in range(n):
        arr[i] = output[i]
        state.active = {i}
        
        if is_last:
            state.sorted_.add(i)
        
        yield
