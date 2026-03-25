import random

def bogo_sort(state):
    arr = state.arr
    n = len(arr)

    while True:
        sorted_ = True

        for i in range(n - 1):
            state.active = {i, i + 1}
            yield

            if arr[i] > arr[i + 1]:
                sorted_ = False
                break
            
        if sorted_:
            break

        state.active.clear()
        random.shuffle(arr)
        yield

    for i in range(n):
        state.sorted_.add(i)
