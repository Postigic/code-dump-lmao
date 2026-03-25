# what the hell is this?
def merge_sort(state):
    arr = state.arr
    n = len(arr)

    yield from _top_down(state, arr, 0, n - 1)

    for i in range(n):
        state.sorted_.add(i)

def bottom_up_merge_sort(state):
    arr = state.arr
    n = len(arr)
    size = 1

    while size < n:
        for left in range(0, n, size * 2):
            mid = min(left + size, n) - 1
            right = min(left + size * 2, n) - 1

            if mid < right:
                yield from _merge(state, arr, left, mid, right)

        size *= 2

    for i in range(n):
        state.sorted_.add(i)

def _top_down(state, arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    yield from _top_down(state, arr, left, mid)
    yield from _top_down(state, arr, mid + 1, right)
    yield from _merge(state, arr, left, mid, right)

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
