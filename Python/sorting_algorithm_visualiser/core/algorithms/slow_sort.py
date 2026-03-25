def slow_sort(state):
    arr = state.arr
    n = len(arr)

    yield from _slow(state, arr, 0, n - 1)

    for i in range(n):
        state.sorted_.add(i)

def _slow(state, arr, lo, hi):
    if lo >= hi:
        return

    mid = (lo + hi) // 2

    yield from _slow(state, arr, lo, mid)
    yield from _slow(state, arr, mid + 1, hi)

    state.active = {mid, hi}
    yield

    if arr[mid] > arr[hi]:
        arr[mid], arr[hi] = arr[hi], arr[mid]
    
    yield from _slow(state, arr, lo, hi - 1)
