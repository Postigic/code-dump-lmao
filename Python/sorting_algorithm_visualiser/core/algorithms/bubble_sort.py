def bubble_sort(state):
    arr = state.arr
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            state.active = {j, j + 1}
            yield

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        state.sorted_.add(n - 1 - i)

def optimised_bubble_sort(state):
    arr = state.arr
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            state.active = {j, j + 1}
            yield

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        state.sorted_.add(n - 1 - i)

        if not swapped:
            for k in range(n):
                state.sorted_.add(k)
            break
