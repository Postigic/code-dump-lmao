def stooge_sort(state):
    arr = state.arr
    n = len(arr)

    yield from _stooge(state, arr, 0, n - 1)

    for i in range(n):
        state.sorted_.add(i)

def _stooge(state, arr, lo, hi):
    if arr[lo] > arr[hi]:
        state.active = {lo, hi}
        yield
        
        arr[lo], arr[hi] = arr[hi], arr[lo]
        yield
    
    if hi - lo + 1 > 2:
        third = (hi - lo + 1) // 3

        yield from _stooge(state, arr, lo, hi - third)
        yield from _stooge(state, arr, lo + third, hi)
        yield from _stooge(state, arr, lo, hi - third)
