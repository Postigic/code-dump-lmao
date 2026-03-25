def heap_sort(state):
    arr = state.arr
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        yield from _heapify(state, arr, n, i)

    for i in range(n - 1, 0, -1):
        state.active = {0, i}
        yield
        
        arr[0], arr[i] = arr[i], arr[0]
        
        state.sorted_.add(i)
        yield from _heapify(state, arr, i, 0)

    state.sorted_.add(0)

def _heapify(state, arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        state.active = {i, left}
        yield
        
        if arr[left] > arr[largest]:
            largest = left

    if right < n:
        state.active = {i, right}
        yield
        
        if arr[right] > arr[largest]:
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        state.active = {i, largest}
        yield

        yield from _heapify(state, arr, n, largest)
