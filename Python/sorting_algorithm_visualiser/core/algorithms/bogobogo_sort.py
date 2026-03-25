import random

def bogobogo_sort(state):
    arr = state.arr
    n = len(arr)

    yield from _bogobogo(state, arr, n)

    for i in range(n):
        state.sorted_.add(i)

def _bogobogo(state, arr, k):
    if k <= 1:
        return

    while True:
        arr[:k] = random.sample(arr[:k], k)

        state.active.clear()
        yield

        yield from _bogobogo(state, arr, k - 1)

        state.active.clear()
        yield

        sorted_ = True

        for i in range(k - 1):
            state.active = {i, i + 1}
            yield

            if arr[i] > arr[i + 1]:
                sorted_ = False
                break

        if sorted_:
            break
