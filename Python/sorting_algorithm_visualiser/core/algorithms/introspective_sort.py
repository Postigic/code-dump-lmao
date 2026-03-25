import math

def introspective_sort(state):
    arr = state.arr
    n = len(arr)
    max_depth = 2 * math.floor(math.log2(n))

    yield from _introspective(state, arr, 0, n - 1, max_depth)

def _introspective(state, arr, lo, hi, max_depth):
    size = hi - lo + 1

    if size <= 16:
        yield from _insertion(state, arr, lo, hi)
    elif max_depth == 0:
        yield from _heap(state, arr, lo, hi)
    else:
        mid = (lo + hi) // 2
        arr[mid], arr[hi] = arr[hi], arr[mid]

        state.pivot = {hi}
        state.active = {mid}
        yield

        p = yield from _partition(state, arr, lo, hi)
        state.pivot.clear()
        yield from _introspective(state, arr, lo, p - 1, max_depth - 1)
        yield from _introspective(state, arr, p + 1, hi, max_depth - 1)

def _insertion(state, arr, lo, hi):
    for i in range(lo + 1, hi + 1):
        key = arr[i]
        j = i - 1

        while j >= lo and arr[j] > key:
            state.active = {j, j + 1}
            yield
            
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

    for i in range(lo, hi + 1):
        state.sorted_.add(i)

def _heap(state, arr, lo, hi):
    n = hi - lo + 1

    for i in range(n // 2 - 1, -1, -1):
        yield from _heapify(state, arr, lo, n, lo + i)

    for i in range(n - 1, 0, -1):
        state.active = {lo, lo + i}
        yield
        
        arr[lo], arr[lo + i] = arr[lo + i], arr[lo]

        state.sorted_.add(lo + i)
        yield from _heapify(state, arr, lo, i, lo)

    state.sorted_.add(lo)

def _heapify(state, arr, base, n, i):
    local_i = i - base
    largest = local_i
    left = 2 * local_i + 1
    right = 2 * local_i + 2

    if left < n:
        state.active = {base + largest, base + left}
        yield
        
        if arr[base + left] > arr[base + largest]:
            largest = left

    if right < n:
        state.active = {base + largest, base + right}
        yield
        
        if arr[base + right] > arr[base + largest]:
            largest = right

    if largest != local_i:
        arr[i], arr[base + largest] = arr[base + largest], arr[i]

        state.active = {i, base + largest}
        yield

        yield from _heapify(state, arr, base, n, base + largest)

def _partition(state, arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1

    for j in range(lo, hi):
        state.active = {j, hi}
        yield

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

            state.active = {i, j}
            yield
        
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]

    state.active = {i + 1, hi}
    yield

    state.sorted_.add(i + 1)
    return i + 1
