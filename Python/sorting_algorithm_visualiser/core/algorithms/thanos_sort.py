import random

def thanos_sort(state):
    arr = state.arr

    while not all(arr[i] <= arr[i+1] for i in range(len(arr) - 1)):
        half = len(arr) // 2

        if random.random() < 0.5:
            del arr[:half]
        else:
            del arr[half:]
        
        yield

    for i in range(len(arr)):
        state.sorted_.add(i)
