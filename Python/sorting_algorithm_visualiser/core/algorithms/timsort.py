MIN_RUN = 32

def timsort(state):
    arr = state.arr
    n = len(arr)

    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN, n)
        yield from _insertion(state, arr, start, end)

    size = MIN_RUN

    while size < n:
        for start in range(0, n, size * 2):
            mid = min(start + size, n)
            end = min(start + size * 2, n)

            if mid < end:
                yield from _merge(state, arr, start, mid - 1, end - 1)

        size *= 2

    for i in range(n):
        state.sorted_.add(i)

def _insertion(state, arr, lo, hi):
    for i in range(lo, hi):
        key = arr[i]
        j = i - 1

        while j >= lo and arr[j] > key:
            state.active = {j, j + 1}
            yield

            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

def _merge(state, arr, left, mid, right):
    l, r = arr[left:mid+1], arr[mid+1:right+1]
    i = j = 0
    k = left

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1

        state.active = {k}
        yield

        k += 1

    while i < len(l):
        arr[k] = l[i]
        state.active = {k}
        yield

        i += 1
        k += 1

    while j < len(r):
        arr[k] = r[j]
        state.active = {k}
        yield

        j += 1
        k += 1
