import random

def bozo_sort(state):
    arr = state.arr
    n = len(arr)

    while not all(arr[i] <= arr[i+1] for i in range(n - 1)):
        i, j = random.sample(range(n), 2)

        state.active = {i, j}
        yield

        arr[i], arr[j] = arr[j], arr[i]

        yield

    for i in range(n):
        state.sorted_.add(i)
